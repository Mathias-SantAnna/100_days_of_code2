class User:

    def __init__(self, user_id, username):
        self.id = user_id
        self.username = username
        self.followers = 0
        self.following = 0

    def follow(self, user):
        user.followers += 1
        self.following += 1

user_1 = User("1", "John")
user_2 = User("2", "Mary")

user_1.follow(user_1)
print(user_1.followers)
print(user_1.following)
print(user_2.followers)
print(user_2.following)