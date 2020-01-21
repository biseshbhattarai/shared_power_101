import sqlite3
conn = sqlite3.connect('user.db')
c = conn.cursor()

c.execute( """CREATE TABLE invoices(
        username text,
        description text,
        quantity integer,
        price integer,
        delivery integer, 
        insurance integer,
        fine integer,
        total integer
    )""")


c.execute("""
        CREATE TABLE cart(
            username text, 
            tool_name text,
            FOREIGN KEY (username) REFERENCES users(username)
            FOREIGN KEY (tool_name) REFERENCES tools(tool_name)
            )
    """)

c.execute("""
            CREATE TABLE hirings(
                username text,
                tool_name text,
                hired_date timestamp,
                quantity integer,
                delivery integer,
                FOREIGN KEY(username) REFERENCES users(username),
                FOREIGN KEY (tool_name) REFERENCES tools(tool_name)
                
            )
""")
