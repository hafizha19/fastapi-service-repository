from datetime import datetime

from mongoengine import DateTimeField, Document


class BaseModel(Document):
    meta = {"allow_inheritance": True, "abstract": True}

    created_at = DateTimeField(required=True, default=datetime.now)
    updated_at = DateTimeField(required=True, default=datetime.now)
    deleted_at = DateTimeField(default=None)

    def save(self, *args, **kwargs):
        # Set created_at only if it's not already set
        if not self.created_at:
            self.created_at = datetime.now()
            
        # Always update updated_at
        self.updated_at = datetime.now()

        super(BaseModel, self).save(*args, **kwargs)
