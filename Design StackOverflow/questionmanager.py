import threading
from question import Question

# Singleton class
class QuestionManager:
    _lock = threading.Lock()  
    _instance =  None  
    
    def __init__(self):
        self.__questions = {}
        self.__next_question_id = 1
        self.__lock = threading.Lock()

    @staticmethod
    def get_instance():
        if QuestionManager._instance is None:
            with QuestionManager._lock:
                if QuestionManager._instance is None:
                    QuestionManager._instance = QuestionManager()
        return QuestionManager._instance

    def post_question(self, user, title, body, tags=None):
        with self.__lock:
            ques_id = self.__next_question_id
            new_ques = Question(ques_id, title, body, user, tags)
            self.__questions[ques_id] = new_ques
            return new_ques, "Question Posted"

    def upvote(self, ques_id):
        with self.__lock:
            self.__questions[ques_id].upvote_question()
            return f"Update Upvote Count for ques id {ques_id} is {self.__questions[ques_id].__votes}"
