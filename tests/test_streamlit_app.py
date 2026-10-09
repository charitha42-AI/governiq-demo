"""Exercise every saved demo case and check the app leaves evidence unchanged."""
import hashlib
from pathlib import Path
import unittest

from streamlit.testing.v1 import AppTest

ROOT = Path(__file__).resolve().parents[1]


class DemoTests(unittest.TestCase):
    def test_all_pages_and_cases(self):
        paths = list((ROOT / 'outputs' / 'metrics').glob('*'))
        before = {p: hashlib.sha256(p.read_bytes()).hexdigest() for p in paths if p.is_file()}
        app = AppTest.from_file(str(ROOT / 'streamlit_app.py'), default_timeout=30).run()
        self.assertFalse(app.exception)
        for page in ['Project dependencies', 'Risk explanations', 'Evaluation evidence', 'Expert review']:
            app.sidebar.radio[0].set_value(page).run()
            self.assertFalse(app.exception, str(app.exception))
            self.assertFalse(app.error, str(app.error))
            if page == 'Project dependencies':
                for project in ['P01', 'P02', 'P03', 'P04', 'P05', 'P06', 'P17', 'P18']:
                    app.selectbox[0].set_value(project).run()
                    self.assertFalse(app.exception)
                    self.assertFalse(app.error)
                    self.assertEqual(len(app.metric), 4)
            elif page == 'Risk explanations':
                for quadrant in ['TP', 'TN', 'FP', 'FN']:
                    app.selectbox[0].set_value(quadrant).run()
                    self.assertFalse(app.exception)
                    self.assertFalse(app.error)
                    self.assertEqual(len(app.dataframe[0].value), 46)
            elif page == 'Evaluation evidence':
                matrix = app.table[0].value
                self.assertEqual(int(matrix.to_numpy().sum()), 800)
                self.assertEqual(int(matrix.iloc[1, 0]), 158)
        self.assertEqual(before, {p: hashlib.sha256(p.read_bytes()).hexdigest() for p in before})


if __name__ == '__main__':
    unittest.main()
