from utils.database import DBConnector
from typing import List, Union

from sqlalchemy.orm import Session
from pydantic import BaseModel


class BaseORM:
    def __init__(self) -> None:
        self.session: Session = DBConnector.create_session()

    def add(self, obj: Union[BaseModel, List[BaseModel]]) -> None:
        if isinstance(obj, list):
            self.session.add_all(obj)
        else:
            self.session.add(obj)

    def flush(self) -> None:
        self.session.flush()

    def commit(self) -> None:
        self.session.commit()

    def rollback(self) -> None:
        self.session.rollback()

    def close(self) -> None:
        self.session.close()
        self.session = None
