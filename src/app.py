from flask import Flask, render_template

from services import UserService

app = Flask(
    __name__,
    static_url_path='',
    static_folder='static',
    template_folder='templates'
)


@app.route('/clicked', methods=['GET', 'POST'])
def clicked():
    users = UserService.get_all_users()
    users_repr = [
        user.__repr__() for user in users
    ]
    response = '<br />'.join(users_repr)

    return response


@app.route("/")
def root_path():
    return render_template("index.html")
