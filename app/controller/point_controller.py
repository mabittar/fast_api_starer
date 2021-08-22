from sqlalchemy.orm.session import Session
from model.contracts.example_contract import PointContract
from orm.example_model import PointModel

from controller.base_controller import CRUDController


class PointController(CRUDController):
    def __init__(self, session: Session) -> None:
        super().__init__(model=PointModel)
        self.session = session

    def create(self, model: PointModel) -> PointContract:

        point = PointModel(**model.dict())
        self.session.add(point)
        self.session.commit()

        return point
