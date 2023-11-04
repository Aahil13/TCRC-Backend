import unittest
from lambda_function import lambda_handler

class TestLambdaHandler(unittest.TestCase):
    def test_lambda_handler(self):
        event = {
            'httpMethod': 'GET'
        }
        context = None

        response = lambda_handler(event, context)
        
        self.assertEqual(response['statusCode'], 200)

if __name__ == '__main__':
    unittest.main()
