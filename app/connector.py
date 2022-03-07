from app.database.sql.connect import database_connector


def connect_mysql(app):
    """Connect MySQL database"""

    return database_connector(
        host=app.config['MYSQL_HOST'],
        db=app.config['MYSQL_DB'],
        user=app.config['MYSQL_USER'],
        password=app.config['MYSQL_PASSWORD'],
        pool_recycle=app.config['MYSQL_CONNECTION_POOL_RECYCLE_TIME'],
        pool_size=app.config['MYSQL_CONNECTION_POOL_SIZE'],
        max_overflow=app.config['MYSQL_MAX_OVERFLOW_LIMIT'])


def connect_redis():
    pass


def connect_elasticsearch():
    pass


def connect_rabbitmq():
    pass

