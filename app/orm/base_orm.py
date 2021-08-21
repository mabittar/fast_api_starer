from typing import List, Optional, Union

from pydantic import BaseModel
from sqlalchemy.orm import Session
from utils.database import DBConnector


class BaseCRUD:
    def __init__(self) -> None:
        self.session: Session = DBConnector.create_session()

    def add(self, obj: Union[BaseModel, List[BaseModel]]) -> Optional[Union[BaseModel, List[BaseModel]]]:
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
