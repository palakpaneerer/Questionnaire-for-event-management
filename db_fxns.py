# core package
import sqlite3

# set connect the datbase
conn = sqlite3.connect("data.db", check_same_thread=False)
c = conn.cursor()


# make a creating a new table function 
def create_event_table():
    c.execute('''
            CREATE TABLE IF NOT EXISTS event (
                name TEXT,
                address TEXT,
                start_day DATE,
                end_day DATE,
                indoor BOOLEAN,
                outdoor BOOLEAN,
                online BOOLEAN,
                main_category TEXT,
                sub_category TEXT
            )
        ''')


# make an adding data function
def add_data(name, address, start_day, end_day, indoor, outdoor, online, main_category, sub_category):
    c.execute('''
              INSERT INTO event(
                name,
                address,
                start_day,
                end_day,
                indoor,
                outdoor,
                online,
                main_category,
                sub_category
                )
                VALUES (?,?,?,?,?,?,?,?,?)
                ''', (
                name,
                address,
                start_day,
                end_day,
                indoor,
                outdoor,
                online,
                main_category,
                sub_category
                )
            )
    conn.commit()
    
    
# make a viewing all data function
def view_all_data():
    c.execute('SELECT * FROM event')
    data = c.fetchall()
    return data


# make an editing data function
def edit_data(new_name, new_address, new_start_day, new_end_day, new_indoor, new_outdoor, new_online, new_main_category, new_sub_category,
              name, address, start_day, end_day, indoor, outdoor, online, main_category, sub_category):
	c.execute("""UPDATE event 
                SET name=?, address=?, start_day=?, end_day=?, indoor=?, outdoor=?, online=?, main_category=?, sub_category=?
                WHERE name=? and address=? and start_day=? and end_day=? and indoor=? and outdoor=? and online=? and main_category=? and sub_category=?""",
                (new_name, new_address, new_start_day, new_end_day, new_indoor, new_outdoor, new_online, new_main_category, new_sub_category,
                 name, address, start_day, end_day, indoor, outdoor, online, main_category, sub_category))
	conn.commit()
	data = c.fetchall()
	return data


# make a searching and viewing specific data using event name function
def get_data_by_event_name(name):
    c.execute('SELECT * FROM event WHERE name = ?', (name,))  # must be taple formart in the last part such as (name,)
    data = c.fetchall()
    return data


# make a delete function
def delete_data(name):
    c.execute("DELETE FROM event WHERE name=?", (name,)) # must be tuple format in the last part such as (name,)
    conn.commit()