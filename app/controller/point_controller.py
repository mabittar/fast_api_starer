from sqlalchemy.orm.session import Session
from controller.base_controller import CRUDBase
from model.contracts.example_contract import PointContract
from orm.example_model import PointModel


from utils.database import get_db


class PointController(CRUDBase):
    def __init__(self, session: Session) -> None:
        super().__init__(model=PointModel)
        self.session = session if session else get_db()

    def create(self, model: PointModel) -> PointContract:

        point = PointModel(**model.dict())
        self.session.add(point)
        self.session.commit()

        return point
