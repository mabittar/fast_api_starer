import os
from os import pardir, path
from pathlib import Path
from types import MethodType

import pytest
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from utils.db.database import Base


@pytest.fixture
def in_memory_db():
    execution_options = {"schema_translate_map": {"example": None, "point": None}}
    engine = create_engine("sqlite:///:memory:", execution_options=execution_options)
    # TODO update all models with constraints, to create tables here
    Base.metadata.create_all(engine)

    raw_cursor = engine.raw_connection()
    try:
        # TODO create sql script with test data
        with open(
            Path(os.path.dirname(os.path.abspath(__file__))) / "../tests/test_db_data.sql", "r"
        ) as file:
            raw_cursor.executescript(file.read())
    except FileNotFoundError:
        pass

    return engine


class session_scope_mock:
    def __init__(self):
        self.session = session()

    def __enter__(self):
        return self.session

    def __exit__(self, exc_type, exc_val, exc_tb):
        pass


@pytest.fixture
def session(in_memory_db):
    def commit(self):
        self.committed = True

    def add(self, model, **kwargs):
        self.model_list.append(model)

    def _autoflush(self):
        pass

    session = sessionmaker(bind=in_memory_db)()
    session.model_list = list()
    session.add = MethodType(add, session)
    session.committed = False
    session.commit = MethodType(commit, session)
    session._autoflush = MethodType(_autoflush, session)
    yield session


@pytest.fixture
def env():
    service_root = path.abspath(path.dirname(__file__))
    project_root = path.abspath(path.join(path.join(service_root, pardir)))
    load_dotenv(dotenv_path=".../local.env".format(project_root))


@pytest.fixture()
def logger():
    class FakeLogger:
        def __init__(self):
            self.severity = None
            self.msg = None

        def error(self, msg, *args, **kwargs):
            print("ERROR:" + str(msg))
            self.severity = "error"
            self.msg = msg

        def debug(self, msg, *args, **kwargs):
            print("DEBUG:" + str(msg))
            self.severity = "debug"
            self.msg = msg

        def info(self, msg, *args, **kwargs):
            print("INFO:" + str(msg))
            self.severity = "info"
            self.msg = msg

        def warning(self, msg, *args, **kwargs):
            print("EARNING:" + str(msg))
            self.severity = "warning"
            self.msg = msg

        def fatal(self, msg, *args, **kwargs):
            print("FATAL:" + str(msg))
            self.severity = "fatal"
            self.msg = msg

    return FakeLogger()
