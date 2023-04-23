import datetime
from typing import Dict

import sqlalchemy


class Database:
    POSTGRES_PROTOCOL = "postgres://"
    SA_POSTGRES_PROTOCOL = "postgresql://"

    def __init__(self, database_url: str):
        self._database_url = database_url
        if self.POSTGRES_PROTOCOL in self._database_url:
            self._database_url = self._database_url.replace(
                self.POSTGRES_PROTOCOL, self.SA_POSTGRES_PROTOCOL
            )
        self.db = sqlalchemy.create_engine(self._database_url)

    def __call__(self, *args, **kwargs):
        return self.db
