from class_iterator_for_select import ClientIterator
from logger import timer


@timer
def find_client(cur, first_name=None, last_name=None, email=None, phone=None):
    query = ("SELECT c.id, c.first_name, c.last_name, ci.email, ci.phone_number "
             "FROM clients c JOIN contact_info ci ON c.id = ci.client_id ")
    conditions = []
    if first_name:
        conditions.append(f"c.first_name = '{first_name}'")
    if last_name:
        conditions.append(f"c.last_name = '{last_name}'")
    if email:
        conditions.append(f"ci.email = '{email}'")
    if phone:
        conditions.append(f"ci.phone_number = '{phone}'")

    if conditions:
        query += "WHERE " + " AND ".join(conditions)
        cur.execute(query)
        result = cur.fetchall()
        return result
    return ClientIterator(cur, query)
