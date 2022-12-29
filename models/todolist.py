from mongoengine import *


class TodoList(Document):
    task = StringField(required=True, min_length=3)
    complete = BooleanField(default=False)
