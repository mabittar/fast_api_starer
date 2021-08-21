from typing import Any, List, Tuple, Union

from orm.base_orm import BaseCRUD
from pydantic import BaseModel
from sqlalchemy import Column, asc, desc, or_
from sqlalchemy.orm.query import Query
from sqlalchemy.sql.schema import Column


class CRUDController(BaseCRUD):
    def __init__(self, model: BaseModel):
        BaseCRUD.__init__(self)
        self.model = model

    def add(self, data: Union[BaseModel, List[BaseModel]]) -> None:
        if not isinstance(data, list):
            data = [data]
        self.session.add_all(data)

    def delete(self, data: BaseModel) -> None:
        self.session.delete(data)

    def new_query(self) -> Query:
        return self.session.query(self.model)

    def lock(self, query: Query) -> Query:
        return query.with_for_update(of=self.model)

    def get_first(self, query: Query) -> BaseModel:
        return query.first()

    def get_all(self, query: Query) -> List[BaseModel]:
        return query.all()

    @staticmethod
    def __asc(query: Query, column: Column) -> Query:
        new_query = query.order_by(asc(column))
        return new_query

    @staticmethod
    def __desc(query: Query, column: Column) -> Query:
        new_query = query.order_by(desc(column))
        return new_query

    @staticmethod
    def _order_by(query: Query, column: Column, order: str) -> Query:
        method = {
            "asc": CRUDController.__asc,
            "desc": CRUDController.__desc,
        }
        return method[order](query, column)

    @staticmethod
    def _filter_or(
        query: Query, condition_tuple_list: List[Tuple[str, Column, Any]]
    ) -> Query:
        def build_condition(filter_type: str, column: Column, value):
            if filter_type == "like":
                if not isinstance(value, list):
                    value = [value]
                response = [column.like(f"%{single_value}%") for single_value in value]
            else:
                if not isinstance(value, list):
                    value = [value]
                response = [column.in_(value)]
            return response

        condition_list = []
        for condition_tuple in condition_tuple_list:
            condition_list.extend(
                build_condition(
                    filter_type=condition_tuple[0],
                    column=condition_tuple[1],
                    value=condition_tuple[2],
                )
            )

        new_query = query.filter(or_(*condition_list))

        return new_query
