class Credentials:

      credentials_list = []  # Empty credentials list


      def __init__(self, user_name, password):

         self.user_name = user_name
         self.password = password


      def save_credentials(self):
        '''
        save_credentials method saves user objects into credentials list
        '''

        Credentials.credentials_list.append(self)


      def delete_credentials(self):
        '''
        delete_credentials method deletes a saved credentials from the credentials_list
        '''

        Credentials.credentials_list.remove(self)


      @classmethod
      def find_by_password(cls, password):
        for credentials in cls.credentials_list:
                if credentials.password == password:
                       return credentials


      @classmethod
      def credentials_exist(cls, password):
        for credentials in cls.credentials_list:
                if credentials.password == password:
                 return True

                return False


      @classmethod
      def display_credentials(cls):
        return cls.credentials_list
