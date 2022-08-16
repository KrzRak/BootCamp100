# How to declare and use class in phyton

# Declaration

class User:

    def __init__(self, id, username):
        self.id = id
        self.username = username
        self.followers = 0
        self.following = 0

    def follow(self, user):
        user.followers += 1
        self.following += 1

# Declaration for users using one class
user_1 = User("001", "angela")
user_2 = User("002", "jack")

# Using function from class
user_1.follow(user_2)
user_1.follow(user_2)
user_1.follow(user_2)

# Output
print(user_1.followers)
print(user_1.following)
print(user_2.followers)
print(user_2.following)
