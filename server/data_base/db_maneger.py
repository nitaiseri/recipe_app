import pymysql

HOST = "localhost"
USER = "root"
DB = "recipes_app"
PWD = ""
dairy_ingredients = ["Cream","Cheese","Milk","Butter","Creme","Ricotta","Mozzarella","Custard","Cream Cheese"]
gluten_ingredients = ["Flour","Bread","spaghetti","Biscuits","Beer"]

class DB_Manager:
    def __init__(self):
        self.connection = pymysql.connect(
            host=HOST,
            user=USER,
            password=PWD,
            db=DB,
            charset="utf8",
            cursorclass=pymysql.cursors.DictCursor
        )
    
    def insert_dairy_ingredients(self):
        with self.connection.cursor() as cursor:
            for ingredient in dairy_ingredients:
                cursor.execute(f"INSERT INTO dairy_ingredient VALUES(null, '{ingredient}');")
        self.connection.commit()
        
    def insert_gluten_ingredients(self):
        with self.connection.cursor() as cursor:
            for ingredient in gluten_ingredients:
                cursor.execute(f"INSERT INTO gluten_ingredient VALUES(null, '{ingredient}');")
        self.connection.commit()


    def get_dairy_ingredients(self):
        with self.connection.cursor() as cursor:
            cursor.execute(f"SELECT name FROM dairy_ingredient;")
            return cursor.fetchall()

        
    def get_gluten_ingredients(self):
        with self.connection.cursor() as cursor:
            cursor.execute(f"SELECT name FROM gluten_ingredient;")
            return cursor.fetchall()
    
    # def get_longest_book(self):
    #     with self.connection.cursor() as cursor:
    #         cursor.execute(GET_LONGEST_BOOK)
    #         result = cursor.fetchone()["name"]
    #         return result

db_manager = DB_Manager()
