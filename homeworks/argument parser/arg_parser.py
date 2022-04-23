import argparse
import json


class ErrorUsername(Exception):
    pass


class ErrorEmail(Exception):
    pass


parser = argparse.ArgumentParser()

parser.add_argument("--username", help="Enter username")
parser.add_argument("--email", help="Enter email")
args = parser.parse_args()
user_dict = {}

if args.username:
    user_dict['username'] = args.username

if args.email:
    user_dict['email'] = args.email

user_file = open('users.json', 'r')
users_data = json.loads(user_file.readline())
user_file.close()

try:
    for user in users_data:
        if user['username'] == user_dict['username']:
            raise ErrorUsername
        elif user['email'] == user_dict['email']:
            raise ErrorEmail

    users_data.append(user_dict)

except ErrorUsername:
    print("The username has been taken")
except ErrorEmail:
    print("The email has been taken")

user_file = open('users.json', 'w')
user_file.write(json.dumps(users_data))
user_file.close()