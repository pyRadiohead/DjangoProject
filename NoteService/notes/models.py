import datetime
from django.db import models
from django.utils import timezone
from django.urls import reverse
from django.contrib.auth.models import User

class AllManager(models.Manager):
    def get_queryset(self):
        return super(AllManager,self).get_queryset()


class Note(models.Model):
    slug = models.SlugField(max_length=250, unique_for_date='pub_date')
    title_text = models.CharField(max_length=60)
    note_text = models.TextField(null=True, blank = True)
    created_by = models.ForeignKey(User,on_delete = models.PROTECT)
    pub_date = models.DateTimeField(auto_now_add= True)
    objects = models.Manager()
    all = AllManager()


    def __str__(self):
        return self.title_text

   # def get_absolute_url(self):
     #   return reverse('notes:note_detail_view',
         #              args=[self.pub_date.year, self.pub_date.strftime('%m'), self.pub_date.strftime('%d'), self.slug])


# Create your models here.