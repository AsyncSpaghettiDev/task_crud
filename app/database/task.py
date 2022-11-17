from app.database import get_db


def output_formatter(results):
    out = []
    for result in results:
        result_dict = {
            "id": result[0],
            "title": result[1],
            "subtitle": result[2],
            "body": result[3],
            "active": result[4]
        }
        out.append(result_dict)
    return out


def scan():
    conn = get_db()
    statement = """
        SELECT
            *
        FROM
            tasks
    """
    cursor = conn.execute(statement, ())
    results = cursor.fetchall()
    cursor.close()
    return output_formatter(results)


def scan_single(task_id):
    conn = get_db()
    statement = """
        SELECT
           *
        FROM
            tasks
        WHERE
            id = ?
    """
    cursor = conn.execute(statement, (task_id,))
    results = cursor.fetchall()
    cursor.close()
    return output_formatter(results)


def insert(raw_data):
    conn = get_db()
    task_data = (
        raw_data.get("title"),
        raw_data.get('subtitle'),
        raw_data.get('body'),
    )
    conn.execute(
        "INSERT INTO tasks (title, subtitle, body) VALUES (?, ?, ?)",
        task_data
    )
    conn.commit()
    return True


def update(task_id, raw_data):
    task_data = (
        raw_data.get("title"),
        raw_data.get('subtitle'),
        raw_data.get('body'),
        raw_data.get('active'),
        task_id
    )
    statement = """
    UPDATE 
        tasks
    SET 
        title = ?, 
        subtitle = ?, 
        body = ?, 
        active = ? 
    WHERE 
        id = ?
    """
    conn = get_db()
    conn.execute(statement, task_data)
    conn.commit()
    conn.close()
    return True


def delete(task_id):
    statement = """
    DELETE FROM
        tasks 
    WHERE
        id = ?
    """
    conn = get_db()
    conn.execute(statement, (task_id,))
    conn.commit()
    conn.close()
    return True
