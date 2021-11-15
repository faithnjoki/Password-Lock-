class User:
    """
    a class that generates new instances for user 
    """

    user_list = []

    def __init__(self,user_name, password):
        self.User_name = user_name
        self.Password = password 

    def save_user(self):
        """
        saves user to userlist
        """
        User.user_list.append(self)