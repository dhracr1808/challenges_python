import uuid
import time
from db.dbjsonlocale.db_task import DbJson as Db


class Task:
    def __init__(self, description):
        self.id = f"{uuid.uuid4()}"
        self.description = description
        self.status = "todo"
        self.createAt = time.strftime("%Y-%m-%d %H:%M:%S")
        self.updateAt = time.strftime("%Y-%m-%d %H:%M:%S")

    @property
    def get_task(self):
        return self.__dict__


class TaskRepository:
    def __init__(self, db):
        self.__db = db
        self.task = self.__db.get()
        self.__list_by = {"": "", "todo": "🔴", "in-progress": "🟡", "done": "🟢"}

    def create(self, new_task):
        self.task.append(Task(new_task).get_task)
        self.__db.save(self.task)

    def update(self,  id, description):
        id_task = int(id)
        if 0 < id_task <= len(self.task):
            pos = id_task - 1
            self.task[pos]["description"] = description
            self.task[pos]["updateAt"] = time.strftime("%Y-%m-%d %H:%M:%S")
            self.__db.save(self.task)
            print("Tarea actualizada con exito")
        else:
            print("Error Posicion no valida")

    def delete(self, id_task):
        # for task in self.task:
        #     if task["id"] == id_task.strip():
        #         self.task.remove(task)
        #         print("Tarea eliminada con exito")
        #         self.__db.save(self.task)
        #         return
        # print("No se encontro la tarea")

        if 0 < int(id_task) <= len(self.task):
            del self.task[int(id_task) - 1]
            self.__db.save(self.task)
            print("Tarea eliminada con exito")
        else:
            print("Posicion no valida")

    def list(self, type_list=""):
        if not type_list in self.__list_by:
            return

        def f_by(task):
            return task["status"] if not type_list else task["status"] == type_list

        task = list(filter(f_by, self.task))

        for (i, task) in enumerate(task, 1):
            self.print_list(i, task)

    def print_list(self, i, task):
        emoticon = self.__list_by[task["status"]]
        print(f"""[{i}] {emoticon} {task["description"]} - {task["updateAt"]}""")

    def mark_in_progress(self, index):
        index = int(index) - 1
        self.task[index]["status"] = 'in-progress'
        self.task[index]["updateAt"] = time.strftime("%Y-%m-%d %H:%M:%S")
        self.__db.save(self.task)
        print("Tarea actualizada con exito")

    def mark_done(self, index):
        index = int(index) - 1
        self.task[index]["status"] = 'done'
        self.task[index]["updateAt"] = time.strftime("%Y-%m-%d %H:%M:%S")
        self.__db.save(self.task)
        print("Tarea actualizada con exito")


startTasks = TaskRepository(Db())
