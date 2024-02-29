import unittest
from extractor import param_extract

class TestExtractor(unittest.TestCase):

    def test_param_extract_no_blacklist(self):
        response = "https://example.com/path?param1=value1&param2=value2"
        level = "low"
        black_list = []
        placeholder = "*****"
        
        result = param_extract(response, level, black_list, placeholder)
        
        expected_result = [
            "https://example.com/path?param1=*****",
            "https://example.com/path?param2=*****"
        ]
        self.assertEqual(result, expected_result)

    def test_param_extract_with_blacklist(self):
        response = "https://example.com/path?param1=value1&param2=value2&secret=hidden"
        level = "high"
        black_list = ["secret", "password"]
        placeholder = "*****"
        
        result = param_extract(response, level, black_list, placeholder)
        
        expected_result = [
            "https://example.com/path?param1=*****",
            "https://example.com/path?param2=*****"
        ]
        self.assertEqual(result, expected_result)

    def test_param_extract_high_level(self):
        response = "https://example.com/path?param1=value1&param2=value2&param3=value3"
        level = "high"
        black_list = []
        placeholder = "*****"
        
        result = param_extract(response, level, black_list, placeholder)
        
        expected_result = [
            "https://example.com/path?param1=*****",
            "https://example.com/path?param2=*****",
            "https://example.com/path?param3=*****"
        ]
        self.assertEqual(result, expected_result)

if __name__ == '__main__':
    unittest.main()