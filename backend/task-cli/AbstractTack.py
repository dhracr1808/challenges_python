from abc import ABC, abstractmethod


class Admin_Task(ABC):
    @abstractmethod
    def create_task(self):
        pass

    @abstractmethod
    def update_task(self):
        pass

    @abstractmethod
    def delete_task(self):
        pass

    def get_task(self):
        pass
