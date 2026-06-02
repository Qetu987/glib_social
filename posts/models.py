from django.db import models
from users.models import User

class Post(models.Model):
    title = models.CharField(verbose_name='Title', max_length=150)
    description = models.TextField(verbose_name='Dedcription', max_length=500, blank=True, null=True)
    owner = models.ForeignKey(User, verbose_name='Owner', on_delete=models.CASCADE)
    is_active = models.BooleanField('Is active', default=True) # бачить тільки адмін (імітація видалення поста)
    is_visible = models.BooleanField('Is visible', default=True) # бачить тільки власник
    date = models.DateTimeField(auto_now_add=True, verbose_name='Date create')

    def __str__(self):
        return f'{self.id}_{self.title}_({self.owner})'