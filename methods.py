



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


check_status_code()
