"""GovernIQ: read-only presentation of the executed research evidence."""
from pathlib import Path
import json

import matplotlib.pyplot as plt
import pandas as pd
import streamlit as st

ROOT = Path(__file__).resolve().parent
METRICS = ROOT / 'outputs' / 'metrics'
VERSION = 'GovernIQ expert demo 1.0'

st.set_page_config(page_title='GovernIQ | Expert demonstration', page_icon='◎', layout='wide')


def table(name, processed=False):
    folder = ROOT / 'data' / 'processed' if processed else METRICS
    return pd.read_csv(folder / name, keep_default_na=False)


def download(frame, filename):
    st.download_button('Download displayed evidence', frame.to_csv(index=False).encode('utf-8-sig'),
                       filename, 'text/csv')


def overview():
    st.title('Understand the evidence behind a decision')
    st.write('Explore project dependencies, inspect model explanations and assess where human judgment is needed.')
    left, right = st.columns(2)
    with left:
        st.subheader('Real project dependencies')
        st.write('Eight source projects: inspect dependency paths, supporting source cells and inferred relationships.')
    with right:
        st.subheader('Synthetic risk benchmark')
        st.write('A separate modelling demonstration: examine correct predictions, false alarms and missed delays.')
    st.info('These datasets are separate. The model does not assign risk scores to the real portfolio projects.')
    st.subheader('Expert walkthrough')
    st.markdown('1. Open **Project dependencies** and inspect a path and its source evidence.\n'
                '2. Open **Risk explanations** and compare a correct prediction with a false alarm and missed delay.\n'
                '3. Review **Evaluation evidence**, including the confusion matrix and limitations.\n'
                '4. Use **Expert review** to access the questionnaire and record your observations externally.')
    st.caption('Research prototype. Graph reach is not a schedule forecast; model explanations are not causal recommendations.')


def graph_view():
    st.title('Project dependencies')
    projects = table('projects.csv', True).set_index('project_id')
    cases = bundle['graph_channel']['cases']
    project = st.selectbox('Real source project', [c['project_id'] for c in cases],
                           format_func=lambda p: f"{p} · {projects.loc[p, 'project_name']}")
    case = next(c for c in cases if c['project_id'] == project)
    structures = table('graph_project_structure.csv')
    row = structures[(structures.project_id == project) & (structures.variant == 'accepted')].iloc[0]
    cols = st.columns(4)
    for col, label, field in zip(cols, ['Task records', 'Dependency pairs', 'Isolated records', 'Cycle groups'],
                                ['tasks', 'dependency_pairs', 'isolated_tasks', 'cycle_groups']):
        col.metric(label, int(row[field]))
    st.caption('Records can include summary headings. An isolated heading is not automatically a data error.')
    st.subheader('Example dependency path')
    st.write(case['explanation'])
    evidence = table('relational_explanation_evidence.csv')
    evidence = evidence[evidence.path_id == case['path_id']].sort_values('step')
    st.caption('Arrows run from prerequisite to dependent. This is a connectivity path, not a calculated critical path. Dependency timing is not simulated.')
    # JSON quoting escapes identifiers safely for Graphviz's DOT representation.
    steps = st.slider('Path steps to display', 1, max(1, len(evidence)), min(6, len(evidence)))
    lines = ['digraph { rankdir=LR; node [shape=box, style=rounded];']
    for edge in evidence.head(steps).to_dict('records'):
        for key in ['prerequisite', 'dependent']:
            label = edge[key + '_name']
            lines.append(f'{json.dumps(edge[key])} [label={json.dumps(label[:65])}];')
        lines.append(f'{json.dumps(edge["prerequisite"])} -> {json.dumps(edge["dependent"])};')
    st.graphviz_chart('\n'.join(lines + ['}']))
    st.caption(f'Showing {steps} of {len(evidence)} steps. The table below contains the complete path.')
    st.dataframe(evidence.drop(columns=['source_declarations_json']), hide_index=True)
    step = st.selectbox('Inspect supporting source declarations for step', evidence.step.tolist())
    selected = evidence[evidence.step == step].iloc[0]
    st.json(json.loads(selected.source_declarations_json))
    st.caption('source_reciprocal = matching source declarations; reconciled_inference = inferred relationship. Pending review is not confirmation.')
    download(evidence, f'{project}_path_evidence.csv')
    with st.expander('Tasks and downstream reach'):
        features = table('graph_task_features.csv', True)
        features = features[(features.project_id == project) & (features.variant == 'accepted')]
        st.dataframe(features.sort_values('downstream_tasks', ascending=False), hide_index=True)
        st.write('Downstream reach measures connected task records, not the probability or duration of disruption.')


def risk_view():
    st.title('Risk explanations')
    st.info('Synthetic benchmark only · Saved held-out examples · No live prediction for real projects')
    labels = {'TP': 'Correct delay prediction', 'TN': 'Correct no-delay prediction',
              'FP': 'False alarm', 'FN': 'Missed delay'}
    quadrant = st.selectbox('Example outcome', list(labels), format_func=labels.get)
    case = next(c for c in bundle['model_channel']['cases'] if c['quadrant'] == quadrant)
    st.subheader(f"{case['Project_ID']} · {labels[quadrant]}")
    cols = st.columns(3)
    cols[0].metric('Model score', f"{case['model_score']:.3f}")
    cols[1].metric('Predicted outcome', 'Delay' if case['predicted'] else 'No delay')
    cols[2].metric('Observed synthetic label', 'Delay' if case['actual'] else 'No delay')
    st.caption('Classification threshold: 0.5. Scores have not been validated as calibrated real-world probabilities. Cases were selected near each outcome group’s median score.')
    contributions = table('shap_local_contributions.csv')
    contributions = contributions[contributions.Project_ID == case['Project_ID']].copy()
    top = contributions.loc[contributions.shap_log_odds.abs().nlargest(10).index].sort_values('shap_log_odds')
    fig, ax = plt.subplots(figsize=(10, 5))
    ax.barh(top.feature.str.replace('_', ' '), top.shap_log_odds,
            color=['#b4553d' if n > 0 else '#287b83' for n in top.shap_log_odds])
    ax.axvline(0, color='#777777', linewidth=.8)
    ax.set_xlabel('SHAP contribution (log-odds): left decreases score; right increases score')
    fig.tight_layout()
    st.pyplot(fig)
    plt.close(fig)
    st.write('These contributions explain how the fitted model uses features relative to its training background. They do not establish causes or justify changing a project feature to obtain a better outcome.')
    st.caption('Chart shows the ten largest absolute contributions. The complete table contains all contributions, including original feature values.')
    st.dataframe(contributions[['feature', 'raw_value', 'was_missing', 'shap_log_odds']], hide_index=True)
    download(contributions, f"{case['Project_ID']}_explanation.csv")


def evaluation():
    st.title('Evaluation evidence')
    results = table('ml_test_metrics.csv')
    st.subheader('Saved model comparison')
    st.dataframe(results, hide_index=True)
    model = st.selectbox('Confusion matrix model', results.model.tolist(),
                         index=results.model.tolist().index(bundle['model_channel']['selected_model']))
    counts = table('ml_confusion_matrices.csv')
    matrix = counts[counts.model == model].pivot(index='actual', columns='predicted', values='count')
    matrix = matrix.reindex(index=[0, 1], columns=[0, 1], fill_value=0)
    matrix.index = ['Actual no delay', 'Actual delay']
    matrix.columns = ['Predicted no delay', 'Predicted delay']
    st.table(matrix)
    st.write('A false alarm predicts delay where the label is no delay. A missed delay predicts no delay where the label is delay. Both must be considered when assessing usefulness.')
    st.warning('The holdout was inspected before the later tuning exercise. These comparisons are descriptive, not a fresh confirmatory evaluation. Enterprise readiness has not been established.')
    with st.expander('Technical checks and research objectives'):
        st.dataframe(table('demo_evaluation_summary.csv'), hide_index=True)
        st.dataframe(table('demo_research_objective_coverage.csv'), hide_index=True)
        st.caption('Passing implementation checks does not demonstrate predictive validity or expert acceptance.')


def review():
    st.title('Expert review')
    st.write('Use the same walkthrough and record the demo version for both Modified Delphi rounds. Include the false-alarm and missed-delay examples in your review.')
    st.info('Questionnaire responses are collected separately. This app does not submit or store participant answers.')
    questionnaire = ROOT / 'EXPERT_REVIEW_QUESTIONNAIRE.md'
    st.download_button('Download two-round questionnaire', questionnaire.read_bytes(), questionnaire.name, 'text/markdown')
    st.subheader('Questions to keep in mind')
    st.markdown('- Can you follow a dependency back to its source evidence?\n'
                '- Can you distinguish source-supported relationships from inferred ones?\n'
                '- Can you explain why a model prediction occurred, including an incorrect prediction?\n'
                '- What could mislead a decision-maker, and which improvement is most urgent?')
    with st.expander('Dataset review register — separate from expert evaluation'):
        reviews = table('dependency_human_review.csv')
        st.write('This register tracks source-data review. Expert questionnaire ratings do not approve these records. Changes must be reviewed and applied through the research workflow.')
        st.dataframe(reviews, hide_index=True)
    st.caption('For Round 2, provide anonymised panel feedback and the refinement log alongside this demo. Persistent disagreement should be retained.')


st.sidebar.title('GovernIQ')
st.sidebar.caption('Explainable programme governance')
page = st.sidebar.radio('Explore', ['Overview', 'Project dependencies', 'Risk explanations', 'Evaluation evidence', 'Expert review'])
st.sidebar.divider()
st.sidebar.caption(VERSION)
st.sidebar.caption('Research demonstration · local session')
try:
    bundle = json.loads((METRICS / 'explanation_case_bundle.json').read_text(encoding='utf-8'))
    {'Overview': overview, 'Project dependencies': graph_view, 'Risk explanations': risk_view,
     'Evaluation evidence': evaluation, 'Expert review': review}[page]()
except (OSError, ValueError, KeyError, IndexError) as exc:
    st.error('The saved demonstration evidence is missing or inconsistent. Restore the notebook outputs before continuing.')
    st.code(str(exc))
    st.stop()
