import pymysql
import random
import io
#from PIL import Image

class Przepis:
    ingredients = ''
    name = ''
    preparation = ''
    connection=pymysql.connect("mysql6001.site4now.net", "a2dc82_recipes", "conaobiad1", "db_a2dc82_recipes")
    cursor=connection.cursor()
    #user='Admin'
    def wyswietl_przepis(self):
        try:
            przepis = "SELECT * FROM DINNER "
            self.cursor = self.connection.cursor()
            self.cursor.execute(przepis)
            result = self.cursor.fetchall()
            #image = Image.open(io.BytesIO(result[5]))
            przepisy = [result[1], result[2], result[3]]
            return przepisy
        except:
            self.connection.rollback()


    def stworz_przepis(self, name, ingredients, preparation, user):
        self.ingredients = ingredients
        self.name=name
        self.preparation=preparation
        przepis = "INSERT INTO dinner(NAME, INGREDIENTS, PREPARING,USER ) VALUES ('%s','%s','%s', '%s')"%(self.name, self.ingredients, self.preparation, user)
        try:
            self.cursor.execute(przepis)
            self.connection.commit()
        except:
            self.connection.rollback()


        #z frontu trzeba po każdej linijce podawać ^ w ingredients i preparation
        # w takiej formie tu trzeba to tylko wrzucić do bazy danych


    def czyJestprzepis(self, nameDish):
        try:
            dish = "SELECT * FROM DINNER WHERE NAME = '%s'" % (nameDish)
            self.cursor = self.connection.cursor()
            self.cursor.execute(dish)
            result = self.cursor.fetchone()

            if nameDish==result[1] and self.user==result[4]:
                return True
            else:
                return False
        except:
            return False
    def znajdz_przepis(self, nameDish):
        try:
            dish = "SELECT * FROM DINNER WHERE NAME = '%s'" % (nameDish)
            self.cursor = self.connection.cursor()
            self.cursor.execute(dish)
            result = self.cursor.fetchone()
            name = str(result[1])
            ingredients = str(result[2])
            preparation = str(result[3])
            #image = Image.open(io.BytesIO(result[5]))
            danie = [name, ingredients, preparation]
            return danie
        except:
            self.connection.rollback()

    def usun_przepis(self, nameDish):
        if self.czyJestprzepis(nameDish):
            self.cursor = self.connection.cursor()
            try:
              sql = "DELETE FROM DINNER WHERE NAME ='%s'" % (nameDish)
              self.cursor.execute(sql)
              self.connection.commit()
            except:
                self.connection.rollback()
        else:
            self.connection.rollback()

    def mojePrzepisy(self, user):
        try:
            przepis = "SELECT * FROM DINNER WHERE USER ='%s'" %(user)
            self.cursor = self.connection.cursor()
            self.cursor.execute(przepis)
            result = self.cursor.fetchall()
            #print(result[1])
            #image = Image.open(io.BytesIO(result[5]))
            mojeprzepisy=result
            #for i in mojeprzepisy:
                #print(i[1])
            return mojeprzepisy
        except:
            self.connection.rollback()

    def czyJestID(self, id):
        try:
            dish = "SELECT * FROM DINNER WHERE ID = '%s'" % (id)
            self.cursor = self.connection.cursor()
            self.cursor.execute(dish)
            result = self.cursor.fetchone()
            if result[0]==id:
                return True
            else:
                return False
        except:
            return False


    def losowy_ID(self):
        try:
           sql = "SELECT * FROM DINNER "
           self.cursor = self.connection.cursor()
           self.cursor.execute(sql)
           result = self.cursor.fetchall()

           number_of_rows=len(result)

           maxID=result[number_of_rows-1][0]
           losid = random.randrange(1, maxID+1)

           while self.czyJestID(losid)!=True:
              losid = random.randrange(1, maxID + 1)


           return losid
        except:
            self.connection.rollback()
          #Pobrać ingrediance, name i preparation na podstawie wylosowanego id
          #np. self.name = name_db

    def losowyPrzepis(self):
        id=self.losowy_ID()
        try:
            przepis = "SELECT * FROM DINNER WHERE ID = '%s'" % (id)
            self.cursor=self.connection.cursor()
            self.cursor.execute(przepis)
            result = self.cursor.fetchone()
            name=result[1]
            ingredients=result[2]
            preparation=result[3]
            #image = Image.open(io.BytesIO(result[5]))
            danie=[name,ingredients,preparation]
            return danie

        except:
             self.connection.rollback()



