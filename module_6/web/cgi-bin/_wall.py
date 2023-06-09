import json
import random
import time

class Wall:
    USERS = 'cgi-bin/users.json'
    WALL = 'cgi-bin/wall.json'
    COOKIES = 'cgi-bin/cookies.json'

    def __init__(self):
        
        try:
            with open(self.USERS, 'r', encoding='utf-8'):
                pass
        except FileNotFoundError:
            with open(self.USERS, 'w', encoding='utf-8') as f:
                json.dump({}, f)

        try:
            with open(self.WALL, 'r', encoding='utf-8'):
                pass
        except FileNotFoundError:
            with open(self.WALL, 'w', encoding='utf-8') as f:
                json.dump({"posts": []}, f)

        try:
            with open(self.COOKIES, 'r', encoding='utf-8'):
                pass
        except FileNotFoundError:
            with open(self.COOKIES, 'w', encoding='utf-8') as f:
                json.dump({}, f)

    def register(self, user, password):
    
        if self.find(user):
            return False  
        with open(self.USERS, 'r', encoding='utf-8') as f:
            users = json.load(f)
        users[user] = password
        with open(self.USERS, 'w', encoding='utf-8') as f:
            json.dump(users, f)
        return True

    def find(self, user, password=None):
       
        with open(self.USERS, 'r', encoding='utf-8') as f:
            users = json.load(f)
        if user in users and (password is None or password == users[user]):
            return True
        return False

    def publish(self, user, text):
        
        with open(self.WALL, 'r', encoding='utf-8') as f:
            wall = json.load(f)
        wall['posts'].append({'user': user, 'text': text})
        with open(self.WALL, 'w', encoding='utf-8') as f:
            json.dump(wall, f)

    def html_list(self):
        
        with open(self.WALL, 'r', encoding='utf-8') as f:
            wall = json.load(f)
        posts = []
        for post in wall['posts']:
            content = post['user'] + ' : ' + post['text']
            posts.append(content)
        return '<br>'.join(posts)