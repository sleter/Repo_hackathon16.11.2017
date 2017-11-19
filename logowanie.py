import pymysql.cursors

class LogIn:
    login = ''
    password = ''
    email = ''
  #  password_db = ''
    connection = pymysql.connect(
        host='mysql6001.site4now.net',
        user='a2dc82_recipes',
        password='conaobiad1',
        db='db_a2dc82_recipes',
    )
    cursor = connection.cursor()

    def CreateUser(self, name, password, email):
        self.login = name
        self.password = password
        self.email = email
        #self.password = base64.b64encode(bytes(password, 'utf-8'))

        user = "INSERT INTO LOGIN(NAME, PASSWORD, EMAIL)VALUES ('%s', '%s', '%s')" % (self.login, self.password, self.email)
        try:
            self.cursor.execute(user)
            self.connection.commit()
        except:
           self.connection.rollback()
        #tutatj musisz wpakować wpisywanie teo do bazy danych w sql



    def CheckUser(self):
        try:
            user = "SELECT * FROM LOGIN WHERE NAME = '%s'" % (self.login)
            self.cursor=self.connection.cursor()
            self.cursor.execute(user)
            result = self.cursor.fetchone()
            #self.password = base64.b64encode(bytes(self.password, 'utf-8'))
            if self.password == result[2]:
                return True
            else:
                return False
        except:
              return False

    def LogOut(self):
        self.connection.close()









