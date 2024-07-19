import unittest
import requests
from config import TARGET_URL

class TestKurtosysAPI(unittest.TestCase):

    def test_kurtosys_api(self):
        #GET request for kurtosys URL
        response = requests.get(TARGET_URL)

        # Assert that the response status code is 200
        self.assertEqual(response.status_code, 200, "Expected status code to be 200")

        # Assert that the response time is less than 2 seconds
        response_time = response.elapsed.total_seconds()
        self.assertLess(response_time, 2, "Expected response time to be less than 2 seconds")

        # Assert that the server header has a value of 'Cloudflare'
        server_header = response.headers.get('Server')
        self.assertEqual(server_header, 'cloudflare', f"Expected server header to be 'cloudflare' but was '{server_header}'")

if __name__ == '__main__':
    unittest.main()
