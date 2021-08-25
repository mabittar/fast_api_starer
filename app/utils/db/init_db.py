from sqlalchemy.orm import Session

from utils.db.base_class import Base
from utils.db.session import engine

def init_db() -> None:
    Base.metadata.create_all(bind=engine)
