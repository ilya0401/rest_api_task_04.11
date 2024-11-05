import requests

from constants.status_codes import StatusCodes
from methods import get_url, get_status_code, UrlAddings, get_title
from models.posts import Post


url = "https://jsonplaceholder.typicode.com"

adress_for_test = get_url(url, UrlAddings.POST.value, UrlAddings.post_99.value)

response = requests.get(adress_for_test)

assert get_status_code(adress_for_test) == StatusCodes.Code_200.value
c = get_title(response.content, Post, 10, 99)
assert get_title(response, Post, 10, 99)
