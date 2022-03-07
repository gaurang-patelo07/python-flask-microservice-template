from enum import Enum

__all__ = ["DatabaseEnum", "DatabaseURLEnum"]


class DatabaseEnum(Enum):
    MYSQL = "MySQL"


class DatabaseURLEnum(Enum):
    MYSQL = "mysql+pymysql://{user}:{password}@{host}/{database}"

