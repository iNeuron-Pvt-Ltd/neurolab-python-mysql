import mysql.connector
from read_file import get_data
# import mysql.connector
#create user 'user'@'%' identified by 'password'
glass_db = mysql.connector.connect(
  host="localhost",
  user="abc",
  password="password"
)
print(glass_db)
cur = glass_db.cursor()


file_data = get_data("/config/workspace/data/glass.data.txt")
if len(file_data) > 0:
  file_data.pop(0) #to remove headers

data = []

for file_item in file_data:
  temp = file_item.split(",")
  lst = list()
  for cols in temp:
    lst.append(cols)
  data.append(lst)  
    
    
#print(data)
  #print(file_item.rstrip(",")[0])
  #data.append(tuple(file_item))

#print(data)
#cur.executemany(operation, seq_params)

#cur.execute("CREATE DATABASE glass_db")

#cur.execute("USE glass_db")

#cur.execute("""CREATE TABLE glass(indx VARCHAR(40),RI VARCHAR(40),Na VARCHAR(40),Mg VARCHAR(40),Al VARCHAR(40),Si VARCHAR(40),K VARCHAR(40),Ca VARCHAR(40),Ba VARCHAR(40),Fe VARCHAR(40),Class VARCHAR(40))""")


query = 'INSERT INTO glass_db.glass(indx,RI,Na,Mg,Al,Si,K,Ca,Ba,Fe,Class) VALUES(%s, %s, %s, %s,%s,%s,%s,%s,%s,%s,%s)'        

cur.executemany(query, data)

glass_db.commit()
cur.execute("SELECT * FROM glass_db.glass")

for item in cur:
  print(item)