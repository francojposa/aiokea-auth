from aiokea.repos.aiopg import AIOPGRepo
from aiopg.sa import Engine

from app.infrastructure.datastore.postgres.tables import AUTH_USER
from app.usecases.resources.auth_user import AuthUser


class UserRepo(AIOPGRepo):
    def __init__(self, engine: Engine):
        super().__init__(struct_class=AuthUser, engine=engine, table=AUTH_USER)
