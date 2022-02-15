class User:
    

    def __init__(self, userid, username):
        self.id =userid
        self.username = username
        self.followers = 0
        self.following = 0
    
    def follow(self, user):
        user.followers += 1
        self.following += 1
        print("new user being created...")


user_1 = User("001", "edith")
user_2 = User("002", "erika")

user_1.follow(user_2)
print(user_1.followers)
print(user_1.following)
print(user_2.followers)
print(user_2.following)

