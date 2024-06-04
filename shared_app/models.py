from django.db import models
import uuid


# Create your models here.

class SharedClass(models.Model):
    uu_id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4(),
        editable=False
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'shared_class'

    def __str__(self):
        return self.created_at
