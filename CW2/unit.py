import unittest
from unittest.mock import patch, MagicMock, mock_open
from io import StringIO
from sqlifinder import main  # Replace 'your_script_name' with the actual name of your script

class TestMainFunction(unittest.TestCase):
    def test_main_function(self):
        # Mock the payloads file
        with patch('builtins.open', mock_open(read_data='mocked_payloads')):
            # Mock sys.argv to provide command-line arguments
            with patch('sys.argv', ['unit.py', '-d', 'example.com']):
                # Mock the spider function
                with patch('core.crawler.spider', return_value=['http://example.com']):
                    # Redirect stdout to capture printed output
                    with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
                        main()
                        # Add your assertions based on the output or other expectations
                        self.assertIn('http://example.com', mock_stdout.getvalue())

if __name__ == '__main__':
    unittest.main()
