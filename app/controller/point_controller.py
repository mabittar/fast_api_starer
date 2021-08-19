from orm.point_model import PointModel

from controller.base_controller import BaseController


class PointController(BaseController):
    def __init__(self, session):
        self.session = session

    def create(self, data) -> PointModel:

        self.model.x = data.x
        self.model.y = data.y

        self.session.add(self.model)
        self.session.flush()

        return self.model
