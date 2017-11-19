from Przepis import *
import io
from PIL import Image


connection = pymysql.connect("mysql6001.site4now.net", "a2dc82_recipes", "conaobiad1", "db_a2dc82_recipes")
cursor = connection.cursor()

try:
    dish=Przepis()
    dish.losowy_ID()




except:
    connection.rollback()

