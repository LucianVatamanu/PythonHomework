from app.database import connection

def save_request(operation: str, input_data: str, result: float):
    cursor = connection.cursor()
    sql = """
        INSERT INTO api_requests (operation, input_data, result)
        VALUES (:1, :2, :3)
    """
    cursor.execute(sql, [operation, input_data, str(result)])
    connection.commit()
