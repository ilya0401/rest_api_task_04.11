import json
import requests
from models.posts import Post
import enum


class UrlAddings(enum.Enum):
    POST = "posts"
    post_99 = "99"

url = "https://jsonplaceholder.typicode.com"

def get_url(initial_url, *addings):
    if addings:
        add_to_url = "/".join(addings)
        added_url = initial_url + add_to_url
        return added_url
    else:
        return initial_url

л = get_url(url)
n = get_url(url, UrlAddings.POST.value, UrlAddings.post_99.value, "insect")
k = 0


adress = get_url(url)

response = requests.get(adress)



def create_list_of_objects(page_content, needed_class):
    objects_list = json.loads(page_content.content)
    list_of_objects = [needed_class(**x) for x in objects_list]
    return list_of_objects


def get_object(page_content, needed_class, userID, id):
    a = create_list_of_objects(page_content, needed_class)
    obj = next((user for user in a if user.userId == userID and user.id == id), None)
    return obj

c = get_object(response, Post, 10, 99).title
d = get_object(response, Post, 10, 99).body
d = 7

def get_title(page_content, needed_class, userID, id):
    a = get_object(page_content, needed_class, userID, id).title
    return a

def get_body(page_content, needed_class, userID, id):
    a = get_object(page_content, needed_class, userID, id).body
    return a




#
# def get_title(text, needed_class, userID, id):
#     a = create_list_of_objects(text, needed_class)
#     obj = next((user for user in a if user.userId == userID and user.id == id), None)
#     return obj.title




def is_ascending_ids(posts):
    #is_sorted = all(users[i].id <= users[i + 1].id for i in range(len(users) - 1))
    list_of_id = [i.id for i in posts]
    if list_of_id == sorted(list_of_id): return True


def get_status_code(response):
    return response.status_code



def check_userid_10(posts):
    result = next((user for user in posts if user.userId == 10 and user.id == 99), None)
    a= len(result.title)
    b = len(result.body)
    if a * b == 0:
        return False
    else:
        return True
