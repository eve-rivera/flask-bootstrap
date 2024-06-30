from sqlalchemy import create_engine
from sqlalchemy.orm import Session

engine = create_engine("postgresql://example:example@db:5432/example", echo=True)


def get_session():
    return Session(engine)
