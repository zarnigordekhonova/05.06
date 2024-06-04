from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import FileExtensionValidator
from django.core.exceptions import ValidationError
from random import randint
from shared_app.models import SharedClass
from django.conf import settings
# Create your models here.

ORDINARY_USER, ADMIN, MANAGER = ('ordinary_user', 'admin', 'manager')
VIA_EMAIL, VIA_PHONE = ('via_email', 'via_phone')
NEW, CONFIRM, DONE, DONE_PHOTO = ('new', 'confirm', 'done', 'done_photo')
MALE, FEMALE = ('male', 'female')

def FileSizeValidator(value):
    limit = 2 * 1024 * 1024
    if value.size > limit:
        raise ValidationError('File size should not be over 2 MB!')


class Followers(AbstractUser):
    USER_ROLES = (
        (ORDINARY_USER, ORDINARY_USER),
        (ADMIN, ADMIN),
        (MANAGER, MANAGER)
    )
    USER_TYPES = (
        (VIA_EMAIL, VIA_EMAIL),
        (VIA_PHONE, VIA_PHONE)
    )
    USER_STATUS = (
        (NEW, NEW),
        (CONFIRM, CONFIRM),
        (DONE, DONE),
        (DONE_PHOTO, DONE_PHOTO)
    )
    GENDER = (
        (MALE, MALE),
        (FEMALE, FEMALE)
    )

    user_id = models.ForeignKey(SharedClass, on_delete=models.CASCADE)
    user_role = models.CharField(max_length=64, choices=USER_ROLES, default=ORDINARY_USER)
    user_type = models.CharField(max_length=64, choices=USER_TYPES)
    user_status = models.CharField(max_length=64, choices=USER_STATUS)
    gender = models.CharField(max_length=32, choices=GENDER)
    email = models.EmailField(unique=True, blank=True, null=True)
    phone = models.IntegerField(unique=True, blank=True, null=True)
    image = models.ImageField(upload_to='images/',
            validators=[
                FileExtensionValidator(allowed_extensions=['.jpeg', 'png', 'jpg']),
                FileSizeValidator
            ]
        )


    class Meta:
        db_table = 'followers'
        verbose_name = 'follower'
        verbose_name_plural = 'followers'

    def __str__(self):
        return f'{self.username} - {self.user_role}'


class CodeVerify(models.Model):
    USER_STATUS = (
        (NEW, NEW),
        (CONFIRM, CONFIRM),
        (DONE, DONE),
        (DONE_PHOTO, DONE_PHOTO)
    )
    id_follower = models.ForeignKey(SharedClass, on_delete=models.CASCADE)
    code = models.CharField(max_length=4, blank=True, editable=False)

    def random_code(self):
        return ''.join(str(randint(1, 100) % 10) for _ in range(4))

    def save_code(self, *args, **kwargs):
        if not self.code:
            self.code = self.random_code()
        super(CodeVerify, self).save(*args, **kwargs)

    is_confirm = models.BooleanField(default=False)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='code_verifications')
    expire_time = models.TimeField()
    user_status = models.CharField(max_length=32, choices=USER_STATUS)

    class Meta:
        db_table = 'code_verify'

    def __str__(self):
        return f'{self.user} - {self.is_confirm}'