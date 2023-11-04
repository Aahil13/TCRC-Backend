import unittest
from lambda_function import lambda_handler
import boto3

aws_region = 'us-east-1' 

class TestLambdaHandler(unittest.TestCase):
    def test_lambda_handler(self):
        boto3.setup_default_session(region_name=aws_region)

        event = {
            'httpMethod': 'GET'
        }
        context = None

        response = lambda_handler(event, context)
        
        self.assertEqual(response['statusCode'], 200)

if __name__ == '__main__':
    unittest.main()
