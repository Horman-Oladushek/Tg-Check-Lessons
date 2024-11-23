from .engine import EngineController
from .models import Id_Users


class Id_UsersRepo:
    database_controller = EngineController()


    @classmethod
    def create(cls, telegram_id:str, surname:str) -> None:
        session = cls.database_controller.create_session()
        user = session.query(Id_Users).filter_by(telegram_id=telegram_id).first()
        if user:
            user.surname = surname
        else:
            user = Id_Users(telegram_id=telegram_id, surname=surname)
            session.add(user)
        session.commit()
        session.close()