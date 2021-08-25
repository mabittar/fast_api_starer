from sqlalchemy.orm.session import Session
from controller.base_controller import CRUDBase
from schemas.example_contract import PointContract
from  models.example_model import Point


from utils.db.database import get_db


class PointController(CRUDBase):
    def __init__(self, session: Session) -> None:
        super().__init__(model=Point)
        self.session = session if session else get_db()

    def create(self, model: Point) -> PointContract:

        point = Point(**model.dict())
        self.session.add(point)

        return point
