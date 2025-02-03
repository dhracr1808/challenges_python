import sys
from Task import startTasks
from comands.Comand import ComandTask as Comand


comands = {
    "add": {"comand": Comand(startTasks.create), "arg": {"min": 3, "max": 3}},
    "update": {"comand": Comand(startTasks.update), "arg": {"min": 4, "max": 4}},
    "delete": {"comand": Comand(startTasks.delete), "arg": {"min": 3, "max": 3}},
    "list": {"comand": Comand(startTasks.list), "arg": {"min": 2, "max": 3}},
    "mark-in-progress": {"comand": Comand(startTasks.mark_in_progress), "arg": {"min": 3, "max": 3}},
    "mark-done": {"comand": Comand(startTasks.mark_done), "arg": {"min": 2, "max": 3}},

}

print("Bienvenidos a tu lista de tareas")
if sys.argv[1] in comands:
    arg = comands[sys.argv[1]]["arg"]
    if arg["min"] <= len(sys.argv) <= arg["max"]:
        comands[sys.argv[1]]["comand"].execute(*sys.argv[2:])
    else:
        leng_arg = arg["min"]-len(sys.argv)
        if leng_arg > 0:
            print(
                f'\033[31m{sys.argv[1]}\033[0m necesita { leng_arg } argumentos más...')
        else:
            leng_arg = len(sys.argv) - arg["max"]
            print(
                f'\033[31m{sys.argv[1]}\033[0m argumentos excedidos por { leng_arg }')

else:
    print("Opcion no válida")
