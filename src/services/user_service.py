from sqlalchemy import select

from models import User
import db


class UserService:

    @staticmethod
    def get_all_users():
        with db.get_session() as session:
            users = session.execute(select(User).order_by(User.id))

            return users.all()
