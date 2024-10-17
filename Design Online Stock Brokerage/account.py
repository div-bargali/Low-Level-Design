class Account:
    def __init__(self, id, name, email, password="password123", profile_pic="base64string"):
        self._id = id
        self._name = name
        self._email = email
        self._password = password
        self._profile_pic = profile_pic

    def change_profile_pic(self, profile_pic):
        self._profile_pic = profile_pic