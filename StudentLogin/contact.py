import sqlite3

conn = sqlite3.connect('contact.db')
print "Opened database successfully";

conn.execute('CREATE TABLE contacts ( name TEXT,  email TEXT, message TEXT)')
print "Table created successfully";


conn.close()
