def find_client(cur, first_name=None, last_name=None, email=None, phone=None):
    if first_name and last_name:
        cur.execute("SELECT c.id, c.first_name, c.last_name, ci.email, ci.phone_number "
                    "FROM clients c JOIN contact_info ci ON c.id = ci.client_id "
                    "WHERE c.first_name = %s AND c.last_name = %s", (first_name, last_name))
    elif first_name:
        cur.execute("SELECT c.id, c.first_name, c.last_name, ci.email, ci.phone_number "
                    "FROM clients c JOIN contact_info ci ON c.id = ci.client_id "
                    "WHERE c.first_name = %s", (first_name,))
    elif last_name:
        cur.execute("SELECT c.id, c.first_name, c.last_name, ci.email, ci.phone_number "
                    "FROM clients c JOIN contact_info ci ON c.id = ci.client_id "
                    "WHERE c.last_name = %s", (last_name,))
    elif email:
        cur.execute("SELECT c.id, c.first_name, c.last_name, ci.email, ci.phone_number "
                    "FROM clients c JOIN contact_info ci ON c.id = ci.client_id "
                    "WHERE ci.email = %s", (email,))
    elif phone:
        cur.execute("SELECT c.id, c.first_name, c.last_name, ci.email, ci.phone_number "
                    "FROM clients c JOIN contact_info ci ON c.id = ci.client_id "
                    "WHERE ci.phone_number = %s", (phone,))
    else:
        return None

    client = cur.fetchall()
    return client

