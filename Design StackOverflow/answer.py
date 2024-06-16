from datetime import datetime

class Answer:
    def __init__(self, id, body, user, question_id):
        self.__id = id
        self.__body = body
        self.__user = user
        self.__votes = 0
        self.__comments = []
        self.__timestamp = datetime.now()
        self.__question_id = question_id 

    # add a new comment 
    def add_comment(self, comment):
        self.__comments.append(comment)

    # upvote 
    def upvote_question(self):
        self.__votes += 1