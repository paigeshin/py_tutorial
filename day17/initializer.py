class User :
    
    # This method gets called everytime 
    def __init__(self, user_id, username):
        self.id = user_id
        self.username = username
        self.followers = 0 # Provide Default Value
        print("new user being created...")
    
user_1 = User(user_id=3, username="Paige")
print(user_1.id)
print(user_1.username) 