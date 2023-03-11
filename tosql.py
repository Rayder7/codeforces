import psycopg2
import psycopg2.extras
from config import host, user, password, db_name


# connect to exist database


def add_to_sql():
    connection = psycopg2.connect(
        host=host,
        user=user,
        password=password,
        database=db_name
    )
    connection.autocommit = True

    cur = connection.cursor()
    with open('data.csv', 'r', encoding="utf-8") as f:
        next(f)
        cur.copy_from(f, 'tasks', columns=(
            'number_task', 'name_task', 'rating', 'count_vin'), sep=",")

    with open('data_groups.csv', 'r', encoding="utf-8") as fa:
        next(fa)
        cur.copy_from(fa, 'groups_task', columns=(
            'groups_task'), sep=",")

    connection.commit()
