from usermanager import UserManager
from questionmanager import QuestionManager

def main():
    user_manager = UserManager.get_instance()
    ques_manager = QuestionManager.get_instance()

    _, message = user_manager.register_user("John", "john@email.com", "password")
    print(message)
    _, message = user_manager.register_user("Sam", "sam@email.com", "password12")
    print(message)

    user, message = user_manager.login("john@email.com", "password")
    if user is None:
        return 

    new_ques, message = ques_manager.post_question(user, "Ques 1", "Post first ques", ["new", "ques"])
    print(message)
    user_manager.add_question(user, new_ques)

if __name__ == "__main__":
    main()
