import json
import os


class DbJson:
    def __init__(self):
        self.__db_name = "data.json"
        self.start_connection()

    def start_connection(self):
        if not os.path.exists(self.__db_name):
            with open(self.__db_name, "w") as file:
                json.dump([], file, indent=4)
                print(
                    f"Creando la base base de datos")

    def get(self):
        with open(self.__db_name, "r") as file:
            return json.load(file)

    def save(self, items):
        with open(self.__db_name, "w") as file:
            json.dump(items, file, indent=4)
        print(f"Guardando... datos")
