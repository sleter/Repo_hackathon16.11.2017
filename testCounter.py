import pymysql


connection=pymysql.connect("mysql6001.site4now.net", "a2dc82_recipes", "conaobiad1", "db_a2dc82_recipes")
cursor=connection.cursor()

id = 1
try:
  przepis = "SELECT * FROM DINNER "
  cursor = connection.cursor()
  cursor.execute(przepis)
  result = cursor.fetchall()
  one=result[0][0]
  print(one)


except:
  connection.rollback()