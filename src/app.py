from flask import Flask, render_template
from sqlalchemy import select
from sqlalchemy.orm import session

from models import User
from db import get_session

app = Flask(
    __name__,
    static_url_path='',
    static_folder='static',
    template_folder='templates'
)


@app.route("/clicked", methods=['GET', 'POST'])
def clicked():
    response = ""

    with get_session() as session:
        users = session.execute(select(User).order_by(User.id))
        for user in users.all():
            response += user.__repr__()
            response += "<br />"

    return response


@app.route("/")
def root_path():
    return render_template("index.html")
