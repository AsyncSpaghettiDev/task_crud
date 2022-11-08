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
    cursor = conn.execute("SELECT * FROM tasks WHERE active = 1", ())
    results = cursor.fetchall()
    cursor.close()
    return output_formatter(results)
