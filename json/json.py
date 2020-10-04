import json
import requests

# Code demonstrating json loads, load, dump, dumps
data = '{"user": {"name": "grace", "age": 37}}'
data = json.loads(data)

with open("user.json", "w") as write_file:
    json.dump(data, write_file, indent=4)

with open("user.json", "r") as read_file:
    data = json.load(read_file)
    # print(json.dumps(data, indent=4))

# Yet another sample using the json data from jsonplacefolder site
response = requests.get("https://jsonplaceholder.typicode.com/todos")
todos = json.loads(response.text)
# print(json.dumps(todos, indent=4))

# calculate the todo completed count by user
todos_by_user = {}
for todo in todos:
    try:
        if todo["completed"]:
            todos_by_user[todo["userId"]] += 1
    except KeyError:
        todos_by_user[todo["userId"]] = 1
# print(json.dumps(todos_by_user, indent=4))

# users for the max todo count
top_users = sorted(todos_by_user.items(), key=lambda x: x[1], reverse=True)
# top_users is a sorted tuple of items
print(top_users)

max_todo_cnt = top_users[0][1]
top_userids = [str(user[0]) for user in top_users if user[1] == max_todo_cnt]
top_userid_str = " and ".join(top_userids)

print(f"Users {top_userid_str} have max count : {max_todo_cnt}")


def filter_users(todo):
    """ Find the list of completed items by the top users."""
    if str(todo['userId']) in top_userids and todo['completed']:
        return True
    else:
        return False


# write the filtered items to the json file
filtered_todos = list(filter(filter_users, todos))
with open('completed_items.json', 'w') as json_writer:
    json.dump(filtered_todos, json_writer, indent=4)
