from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from .enum import DatabaseEnum, DatabaseURLEnum


def get_database_url(database):
    """Get database url using database"""

    return {
        DatabaseEnum.MYSQL.value: DatabaseURLEnum.MYSQL.value
    }.get(database)


def database_connector(host: str, db: str, user: str, password: str,
                       pool_recycle: int,
                       pool_size: int,
                       max_overflow: int,
                       database='MySQL'):
    """
    This method is used to create SQL connection using SQLAlchemy ORM.

    :param host: Database host address
    :param db: Database name
    :param user: Database user name
    :param password: Database user password
    :param pool_recycle: Create new connection after given time
    :param pool_size: Minimum number of connections
    :param max_overflow: Maximum number of connections

    :param database: STRING:SQL database that you want to configure. Default it's MySQL.

    :return: DB <<Class engine>> and <<Class Session>>
    """

    url = get_database_url(database).format(user=user,
                                            password=password,
                                            host=host,
                                            database=db)
    engine = create_engine(url, pool_recycle=pool_recycle,
                           pool_size=pool_size,
                           max_overflow=max_overflow,
                           echo=False)

    Session = sessionmaker(bind=engine)

    return engine, Session


class SessionHandler(object):
    """
    This class is used to create new sessions. New session can be created using ``with`` statement.

    - At initialization, it will invoke ``__enter__`` method to acquire the connection
    - At the exit, it will invoke ``__exit__`` method to close the connection

    Steps to use:
        Step 1: Configure ORM
        Step 2: from DataAccessLib.database.connect import SessionHandler
        Step 3: Use ``SessionHandler`` with ``with`` statement to create the connection

    Example:
        with SessionHandler(Session) as session:
            ``Perform operations``

    """

    def __init__(self, session_maker):
        self.session = None
        self.session_maker = session_maker

    def __enter__(self):
        """It's invoking ``connect`` method to create the connection"""

        self.session = connect(self.session_maker)
        return self.session

    def __exit__(self, exc_type, exc_val, exc_tb):
        """It invoking ``close`` method to close the connection"""

        close(self.session)


def connect(session_maker):
    """Create DB connection object"""

    return session_maker()


def close(session):
    if session is not None:
        """Close DB connection"""

        session.close()
