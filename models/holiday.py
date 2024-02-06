from datetime import datetime

from bson import ObjectId
from mongoengine import DateField, DateTimeField, IntField, ObjectIdField, StringField

from models.base_model import BaseModel


class Holiday(BaseModel):
    _id = ObjectIdField(required=False, default=lambda: ObjectId())
    title = StringField()
    code = StringField()
    description = StringField(required=False)
    year = IntField(required=False)
    date = DateField()
    created_at = DateTimeField(default=datetime.now)
    updated_at = DateTimeField(default=datetime.now)
    deleted_at = DateTimeField(default=None)

    meta = {"collection": "holidays"}
