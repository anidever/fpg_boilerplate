import psycopg2
from urllib.parse import urlparse
from config import Config


if __name__ == "__main__":
    db_uri = Config.SQLALCHEMY_DATABASE_URI
    db = urlparse(db_uri)
    db_name = db.path.lstrip("/")

    con = psycopg2.connect(
        host=db.hostname,
        user=db.username,
        password=db.password,
        port=db.port,
        dbname=db_name,
    )
    con.set_isolation_level(psycopg2.extensions.ISOLATION_LEVEL_AUTOCOMMIT)
    cursor = con.cursor()

    try:
        cursor.execute(f"CREATE DATABASE {db_name}")
        cursor.commit()
    except Exception:
        pass
