# 1
class Bot:

    def __init__(self, name):
        self.name = name

    def say_name(self):
        print(self.name)

    def send_message(self, message):
        print(message)


# 2
class TelegramBot(Bot):

    def __init__(self, name, url=None, chat_id=None):
        self.url = url
        self.chat_id = chat_id
        super().__init__(name)

    def send_message(self, message):
        print(f'{self.name} bot says {message} to chat {self.chat_id} using {self.url}')

    def set_chat_id(self, chat_id1):
        self.chat_id = chat_id1

    def set_url(self, url1):
        self.url = url1


# 3
class MyStr(str):

    def __init__(self, text):
        self.text = text

    def __str__(self):
        return self.text.upper()


# 4
class User:

    def __init__(self, name):
        self.name = name

    def __eq__(self, other):
        return self.name.lower() == other.name.lower()


# 5a
def init_func(self, name):
    self.name = name


def say_name_func(self):
    print(self.name)


def send_message_func(self, message):
    print(message)


new_class_bot = type('Bot1',
                     (),
                     {'__init__': init_func, 'say_name': say_name_func, 'send_message': send_message_func})


# 5b
def init_func1(self, name, url=None, chat_id=None):
    self.url = url
    self.chat_id = chat_id
    new_class_bot.__init__(self, name)


def send_message_func(self, message):
    print(f'{self.name} bot says {message} to chat {self.chat_id} using {self.url}')


def set_chat_id_func(self, chat_id=None):
    self.chat_id = chat_id


def set_url_func(self, url=None):
    self.url = url


new_class_telegrambot = type('TelegramBot1',
                             (new_class_bot,),
                             {'__init__': init_func1, 'send_message': send_message_func,
                              'set_chat_id': set_chat_id_func,
                              'set_url': set_url_func, 'super().__init__(name)': init_func})
