import argparse
import os
import sys
import time
from urllib.parse import unquote
from unittest.mock import patch, mock_open, MagicMock
from core import requester
from core import extractor
from core import crawler
from huepy import *
from tqdm import tqdm

start_time = time.time()

def clear():
    if 'linux' in sys.platform or 'darwin' in sys.platform:
        os.system('clear')
    else:
        os.system('cls')



def concatenate_list_data(lst, result):
    for element in lst:
        result = result + "\n" + str(element)
    return result

def main():
    parser = argparse.ArgumentParser(description='xssfinder - a xss scanner tool')
    parser.add_argument('-d', '--domain', help='Domain name of the target [ex. example.com]', required=True)
    parser.add_argument('-s', '--subs', help='Set false or true [ex: --subs False]', default=False)
    args = parser.parse_args()

    if args.subs == True:
        url = f"http://web.archive.org/cdx/search/cdx?url=*.{args.domain}/*&output=txt&fl=original&collapse=urlkey&page=/"
    else:
        url = f"http://web.archive.org/cdx/search/cdx?url={args.domain}/*&output=txt&fl=original&collapse=urlkey&page=/"

    clear()
    

    response = requester.connector(url)
    crawled_urls = crawler.spider(f"http://{args.domain}", 10)
    
    if not crawled_urls or not response:
        return
    
    response = concatenate_list_data(crawled_urls, response)
    response = unquote(response)

    print("\n" + "[" + blue("INF") + "]" + f" Scanning sql injection for {args.domain}")

    exclude = ['woff', 'js', 'ttf', 'otf', 'eot', 'svg', 'png', 'jpg']
    final_uris = extractor.param_extract(response, "high", exclude, "")

    file_content = 'mocked_payloads\nmocked_payloads2\nmocked_payloads3'
    
    with patch('builtins.open', mock_open(read_data=file_content)) as mock_file:
        with patch('requests.get', return_value=MagicMock(text='Mocked SQL response')):
            main()

if __name__ == "__main__":
    clear()
    main()
