import json
import requests

from methods import get_status_code, is_ascending_ids, check_userid_10
from models.posts import Post
from constants.status_codes import StatusCodes


response = requests.get("https://jsonplaceholder.typicode.com/posts")

objects_list = json.loads(response.content)
posts = [Post(**x) for x in objects_list]

assert get_status_code(response) == StatusCodes.Code_200.value
assert is_ascending_ids(posts)

assert check_userid_10(posts)
