from abc import ABC, abstractmethod


class Events:
    def __init__(self, type_e, repo):
        self.type = type_e
        self.repo = repo


class UserEvents(ABC):
    @abstractmethod
    def get_events(self):
        pass


class PrinterEvents:
    def __init__(self, print_type):
        self.type = print_type


class UserGithubEvents(UserEvents):
    def __init__(self):
        self._events = []

    def get_events(self, events: Events):
        self._events = events

    def group_events(self):
        events_dic = dict()

        for event in self._events:
            type_event = event["type"]
            if events_dic.get(type_event):
                events_dic[type_event].append(event)
            else:
                events_dic[type_event] = [event]
        return events_dic

    def list_events(self):
        events = self.group_events()
        for e in events.keys():
            self.print_event(e, events)

    def print_event(self, type, events):
        list_printer = events.keys()
        str_format = type[:-5]
        end = "d" if str_format.endswith("e") else "ed"
        name = events[type][0]["repo"]["name"]
        if type == 'PushEvent':
            print(f'{str_format}{end} {len(events[type])} commits to {name} ')
        elif type == "PullRequestEvent":
            print(
                f'{str_format}{end} {len(events[type])} new issue in {name} ')
