import unittest
from unittest.mock import patch
from crawler import spider, LinkParser

class TestWebCrawler(unittest.TestCase):

    @patch('crawler.urlopen')
    def test_spider(self, mock_urlopen):
        # Mocking the urlopen function
        mock_urlopen.return_value.read.return_value = b'<a href="http://example.com">Link</a>'
        mock_urlopen.return_value.getheader.return_value = 'text/html'

        # Testing spider function
        result = spider("http://vulnweb.com", 1)
        self.assertEqual(result, ["http://example.com"])

    @patch('crawler.urlopen')
    def test_link_parser(self, mock_urlopen):
        # Creating a test instance of LinkParser
        parser = LinkParser()

        # Mocking urlopen function for the module level
        mock_urlopen.return_value.read.return_value = b'<a href="http://example.com">Link</a>'
        mock_urlopen.return_value.getheader.return_value = 'text/html'

        # Testing LinkParser
        result, links = parser.getLinks("http://vulnweb.com")
        self.assertEqual(result, '<a href="http://example.com">Link</a>')
        self.assertEqual(links, ["http://example.com"])

if __name__ == '__main__':
    unittest.main()
