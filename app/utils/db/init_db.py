from sqlalchemy.orm import Session

from utils.db.base_class import Base, engine


def init_db(db: Session) -> None:
    Base.metadata.create_all(bind=engine)
