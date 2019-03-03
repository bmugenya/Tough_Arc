

new_users = []
new_admin = []
book_availabe = []


class Books():

    def __init__(self):
        self.books = book_availabe

    def share(self, book_id, postedOn, postedBy, title, lecture, condition, comment):

        data = {
            "id": book_id,
            "postedOn": postedOn,
            "postedBy": postedBy,
            "title": title,
            "lecture": lecture,
            "condition": condition,
            "comment": comment

        }

        self.books.append(data)
        return self.books


class BuyBook():

    def __init__(self):
        self.books = book_availabe

    def buy(self, book_id, title, lecture, condition):

        data = {
            "id": book_id,
            "title": title,
            "lecture": lecture,
            "condition": condition

        }

        self.books.append(data)
        return self.books


class ViewBook():
    def __init__(self):
        self.books = book_availabe

    def get_books(self):
        return self.books


class AdminRegistration():
    def __init__(self):
        self.user = new_admin

    def save_admin(self, student_id, firstName, password, lastName, email, username):

        new_user = {
            "student_id": student_id,
            "firstName": firstName,
            "lastName": lastName,
            "password": password,
            "email": email,
            "username": username,
            "isAdmin": True,
        }
        self.user.append(new_user)
        return self.user


class UserRegistration():
    def __init__(self):
        self.user = new_users

    def save_users(self, student_id, firstName, password, lastName, email, username):

        new_user = {
            "student_id": student_id,
            "firstName": firstName,
            "lastName": lastName,
            "password": password,
            "email": email,
            "username": username,
            "isAdmin": False,
        }

        self.user.append(new_user)
        return self.user


class AdminLogin():

    def __init__(self):
        self.user = new_admin

    def login(self, email, password):

        users = {
            "email": email,
            "password": password
        }
        return users


class UserLogin():

    def __init__(self):
        self.user = new_users

    def login(self, email, password):

        users = {
            "email": email,
            "password": password
        }
        return users
