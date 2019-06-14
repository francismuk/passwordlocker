class User:
    
    user_list = []

    def __init__(self,f_name,l_name,password):
    
        self.f_name = f_name
        self.l_name = l_name
        self.password = password

    def save_user(self):
        '''
        save_user method saves user objects into users list
        '''
        
        User.user_list.append(self)
        
    @classmethod
    def find_by_password(cls,password):
        '''
        Method that takes the password
        Args:
            password: password to search for
        Returns:
            User
        '''
        for user in cls.user_list:
            if user.password == password:
                return user
            
