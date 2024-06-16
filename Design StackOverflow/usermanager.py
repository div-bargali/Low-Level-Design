import threading
from user import User

# Singleton class
class UserManager:
    _lock = threading.Lock()  
    _instance =  None  
    
    def __init__(self):
        self.__users = {}
        self.__sessions = {}
        self.__next_user_id = 1
        self.__lock = threading.Lock()

    @staticmethod
    def get_instance():
        if UserManager._instance is None:
            with UserManager._lock:
                if UserManager._instance is None:
                    UserManager._instance = UserManager()
        return UserManager._instance

    def register_user(self, name, email, password):
        with self.__lock:
            if email in self.__users:
                return False, "User already exists"

            user_id = self.__next_user_id
            new_user = User(user_id, name, email, password)
            self.__users[email] = new_user
            self.__next_user_id += 1
            return True, "User created successfully"

    def login(self, email, password):
        with self.__lock:
            user = self.__users[email]
            if user and user._password == password:
                session_id = email + "-session"
                self.__sessions[session_id] = user._id
                return user, session_id
            else:
                return None, "Invalid credentials"

    def logout(self, session_id):
        with self.__lock:
            if session_id in self.__sessions:
                del self.__sessions[session_id]

    def add_question(self, user, ques):
        with self.__lock:
            email = user._email
            _user = self.__users[email]
            _user.add_question(ques)
            self.__users[email] = _user
