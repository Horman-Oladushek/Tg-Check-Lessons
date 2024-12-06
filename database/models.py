import sqlalchemy

from sqlalchemy.orm import DeclarativeBase

class Base(DeclarativeBase):
    pass

class Id_Users(Base):
    __tablename__ = 'id_users'

    telegram_id = sqlalchemy.Column(
        sqlalchemy.String(32),
        primary_key=True,
        unique=True
    )

    surname = sqlalchemy.Column(
        sqlalchemy.String(32)
    )

    last_timetable = sqlalchemy.Column(
        sqlalchemy.String(32)
    )