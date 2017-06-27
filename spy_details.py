from datetime import datetime


class Spy:

    def __init__(self, name, salutation, age, rating):
        self.name = name
        self.salutation = salutation
        self.age = age
        self.rating = rating
        self.online = True
        self.chats = []
        self.current_status_message = None


class ChatMessage:

    def __init__(self, message, sent_by_me):
        self.message = message
        self.time = datetime.now()
        self.sent_by_me = sent_by_me


spy = Spy('James Bond', 'Mr.', 20, 5)

friend1 = Spy('Tom', 'Mr.', 21, 4.3)
friend2 = Spy('Sherlock', 'Mr.', 25, 5)
friend3 = Spy('Harry', 'Mr.', 30, 4)

friends = [friend1, friend2, friend3]
