import mysql.connector
# import mysql.connector
#create user 'user'@'%' identified by 'password'
mydb = mysql.connector.connect(
  host="localhost",
  user="abc",
  password="password"
)
print(mydb)
cur = mydb.cursor()

cur.execute("SELECT COUNT(*) FROM glass_db.glass GROUP BY Class")

for item in cur:
    print(item)

