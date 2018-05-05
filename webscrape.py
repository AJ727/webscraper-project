from requests import get
from requests.exceptions import RequestException
from contextlib import closing
from bs4 import BeautifulSoup

def simple_get(url):
    try:
        with closing(get(url, stream=True)) as resp:
            if response_correct(resp):
                return resp.content
            else:
                return None

    except RequestException as e:
        log_e("Error during requests to {0} : {1}".format(url, str(e)))
        return None


def response_correct(resp):
    # Get the content-type in <head></head>
    content_type = resp.headers['Content-Type'].lower()
    # return true if an HTTP response of 200 (means successful)
    # and there is not, nothing there
    # and the string html is found
    return (resp.status_code == 200
            and content_type is not None
            and content_type.find('html') > -1)


def log_e(e):
    print(e)
    # Have it write to txt file later
