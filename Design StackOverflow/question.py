from datetime import datetime

class Question:
    # for a new question posted
    def __init__(self, id, title, body, user, tags):
        self.__id = id
        self.__title = title
        self.__body = body
        self.__user = user
        self.__tags = tags # list 
        self.__timestamp = datetime.now()
        self.__answers = []
        self.__comments = []
        self.__votes = 0

    # add a new answer
    def add_answer(self, answer):
        self.__answers.append(answer)

    # add a new comment 
    def add_comment(self, comment):
        self.__comments.append(comment)

    # add a new tag 
    def add_tag(self, tag):
        self.__tags.append(tag)

    # upvote 
    def upvote_question(self):
        self.__votes += 1