import sqlite3

conn = sqlite3.connect('Database/jobs.db')

c = conn.cursor()

c. execute("DROP TABLE vacation_employment")
c. execute("DROP TABLE casual")
c. execute("DROP TABLE fy_recruitment")
c. execute("DROP TABLE graduate_recruitment")
c. execute("DROP TABLE professional")
c. execute("DROP TABLE vacation")
c. execute("DROP TABLE intern")
c. execute("DROP TABLE on_campus")
c. execute("DROP TABLE independent")
c. execute("DROP TABLE vacation_employment")

#c.execute("DELETE FROM casual")

c.execute("SELECT * FROM casual ")
print("test")
print(c.fetchall())
for item in c.fetchall():
    print(str(item))
#print(str(c.fetchall()))