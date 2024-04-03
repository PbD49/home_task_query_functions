def add_client(cur, first_name, last_name, email, phones):
    cur.execute('''
        INSERT INTO clients (first_name, last_name) 
        VALUES (%s, %s) 
        RETURNING id
    ''', (first_name, last_name))
    client_id = cur.fetchone()[0]

    for phone in phones:
        cur.execute('''
            INSERT INTO contact_info (client_id, email, phone_number) 
            VALUES (%s, %s, %s)
        ''', (client_id, email, phone))


def add_phone(cur, client_id, phone):
    cur.execute('''
                INSERT INTO contact_info (phone_number, client_id)
                VALUES (%s, %s);
                ''', (phone, client_id))
