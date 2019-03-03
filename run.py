from flask import Flask, jsonify, make_response, request

app = Flask(__name__)


book_availabe = []
new_users = []
new_admin = []


@app.route('/books', methods=['GET'])
def books():
    return make_response(jsonify({
        "Title": book_availabe,
        "status": "OK"

    }), 200)


@app.route('/book/book_id', methods=['GET'])
def book():
    return 'Book found'


@app.route('/book/share', methods=['POST'])
def share():
    data = request.get_json()
    book_id = data['id']
    postedOn = data['postedOn']
    postedBy = data['postedBy']
    title = data['title']
    lecture = data['lecture']
    condition = data['condition']
    comment = data['comment']

    new_book = {
        "id": book_id,
        "postedOn": postedOn,
        "postedBy": postedBy,
        "title": title,
        "lecture": lecture,
        "condition": condition,
        "comment": comment

    }

    book_availabe.append(new_book)
    return make_response(jsonify({
        "message": "Book added succedfully",

    }), 201)


@app.route('/register/user', methods=['POST'])
def add_user():
    data = request.get_json()
    student_id = data['student_id']
    firstName = data['firstName']
    lastName = data['lastName']
    email = data['email']
    username = data['username']
    isAdmin = False

    new_user = {
        "student_id": student_id,
        "firstName": firstName,
        "lastName": lastName,
        "email": email,
        "username": username,
        "isAdmin": isAdmin,
    }

    new_users.append(new_user)
    return make_response(jsonify({
        "message": "user added succedfully",

    }), 201)


@app.route('/register/admin', methods=['POST'])
def add_admin():
    data = request.get_json()
    student_id = data['student_id']
    firstName = data['firstName']
    lastName = data['lastName']
    email = data['email']
    username = data['username']
    isAdmin = True

    new_user = {
        "student_id": student_id,
        "firstName": firstName,
        "lastName": lastName,
        "email": email,
        "username": username,
        "isAdmin": isAdmin,
    }

    new_admin.append(new_user)
    return make_response(jsonify({
        "message": "admin added succedfully",

    }), 201)


if __name__ == '__main__':
    app.run()
