from logger import timer


@timer
def delete_phone(cur, client_id, phone):
    cur.execute("DELETE FROM contact_info WHERE client_id = %s AND phone_number = %s", (client_id, phone))


@timer
def delete_client(cur, client_id):
    cur.execute("DELETE FROM contact_info WHERE client_id = %s", (client_id,))
    cur.execute("DELETE FROM clients WHERE id = %s", (client_id,))
