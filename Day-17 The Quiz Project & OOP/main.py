class User:

    def __init__(self, user_id, username):
        self.id = user_id
        self.username = username
        self.followers = 0
        self.following = 0

    def follow(self, user):
        user.followers += 1
        self.following += 1


    
        

user_1 = User("001", "Erdem")
print(user_1.id)
print(user_1.following)
user_2 = User("002", "Armovski")
print(user_2.id)
print(user_2.followers)


user_1.follow(user_2)
print(f"{user_1.username} Following {user_1.following} Users")
print(f"{user_2.followers} Users following {user_2.username}")



