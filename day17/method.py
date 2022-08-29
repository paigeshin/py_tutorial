class User :
    
    # This method gets called everytime 
    def __init__(self, user_id, username):
        self.id = user_id
        self.username = username
        self.followers = 0 # Provide Default Value
        self.following = 0 
        print("new user being created...")

    def follow(self, user):
        user.followers += 1 
        self.following += 1 

    
user_1 = User(user_id=3, username="Paige")
user_2 = User(user_id=5, username="Sunghee")

user_1.follow(user_1)