import sqlite3

con = sqlite3.connect("test.db")
cur = con.cursor()
print("enter the names of 3 students: ")
name = [input() for i in range(3)]
print("Enter their usns ")
usn = [input() for i in range(3)]
n = len(name)

for i in range(n):
    cur.execute("INSERT into student VALUES (?,?)",name[i],usn[i])

cur.execute("SELECT * from student")
for row in cur:
    print("USN: ",row[0])
    print("\n")
    print("name: ",row[1])