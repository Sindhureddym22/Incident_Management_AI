import unittest
from ai__model import generate_response

class TestAIModel(unittest.TestCase):
    def test_generate_response(self):
        response = generate_response("What is the issue with my application?")
        self.assertIsInstance(response, str)

if __name__ == '__main__':
    unittest.main()