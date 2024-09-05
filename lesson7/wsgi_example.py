import logging
import time
import requests


logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)


def app(env, start_response):
    # time.sleep(3)
    t = requests.get("https://httpbin.org/delay/3").text

    start_response("200 OK", [("Content-Type", "text/html")])
    return [b"<h1>Hello, World!</h1>"]
