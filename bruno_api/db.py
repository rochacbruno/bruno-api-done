from sqlmodel import create_engine, SQLModel, Session

from .config import settings


engine = create_engine(
    settings.db.uri,
    echo=settings.db.echo,
    connect_args=settings.db.connect_args
)


def init_db():
    SQLModel.metadata.create_all(engine)


def drop_db():
    SQLModel.metadata.drop_all(engine)


def get_session():
    with Session(engine) as session:
        yield session