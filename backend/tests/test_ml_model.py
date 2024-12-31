import unittest
from ml_model import predict_issue

class TestMLModel(unittest.TestCase):
    def test_predict_issue(self):
        prediction = predict_issue([0, 1, 0])  # Dummy input
        self.assertIn(prediction, [0, 1])  # Assuming binary classification

if __name__ == '__main__':
    unittest.main()