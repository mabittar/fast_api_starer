from sqlalchemy.orm.session import Session
from orm.point_model import PointModel

from controller.base_controller import CRUDController


class PointController(CRUDController):
    def __init__(self, session: Session) -> None:
        super().__init__(model=PointModel)
        self.session = session

    async def create(self, model: PointModel) -> PointModel:

        self.session.add(model)
        self.session.flush()

        return model
