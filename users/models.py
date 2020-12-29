from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    email = models.EmailField(verbose_name='email',max_length=255,unique=True)
    name = models.CharField(max_length=255)  
    following = models.ManyToManyField('self',through='UserContact',related_name='followers',symmetrical=False)
    REQUIRED_FIELDS = ['name','username']
    USERNAME_FIELD = 'email'

    def get_username(self):
        return self.username


class UserContact(models.Model):
    user_from = models.ForeignKey(User,related_name='rel_from_set',on_delete=models.CASCADE)
    user_to = models.ForeignKey(User,related_name='rel_to_set',on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True,db_index=True)

    class Meta:
        ordering = ('-created'),    

    def __str__(self):
        return f'@{self.user_from.username} follows {self.user_to.username}'


