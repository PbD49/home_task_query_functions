def delete_table(cur):
    cur.execute('''DROP TABLE IF EXISTS contact_info''')
    cur.execute('''DROP TABLE IF EXISTS clients''')


def create_db(cur):
    cur.execute('''
                CREATE TABLE IF NOT EXISTS clients (
                    id SERIAL PRIMARY KEY,
                    first_name VARCHAR(50) NOT NULL,
                    last_name VARCHAR(50) NOT NULL
                );
            ''')

    cur.execute('''
                CREATE TABLE IF NOT EXISTS contact_info (
                    id SERIAL PRIMARY KEY,
                    email VARCHAR(50),
                    phone_number INT NULL,
                    client_id INTEGER REFERENCES clients(id)
                );
            ''')
