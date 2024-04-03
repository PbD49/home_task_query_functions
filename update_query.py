def change_client(cur, client_id, first_name=None, last_name=None, email=None, phones=None):
    if first_name:
        cur.execute("UPDATE clients SET first_name = %s WHERE id = %s", (first_name, client_id))
    if last_name:
        cur.execute("UPDATE clients SET last_name = %s WHERE id = %s", (last_name, client_id))
    if email:
        cur.execute("UPDATE contact_info SET email = %s WHERE client_id = %s", (email, client_id))
    if phones:
        cur.execute("DELETE FROM contact_info WHERE client_id = %s AND email IS NULL", (client_id,))
        for phone in phones:
            cur.execute('''
                        INSERT INTO contact_info (phone_number, client_id)
                        VALUES (%s, %s);
                        ''', (phone, client_id))
