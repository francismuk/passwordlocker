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
    
    
