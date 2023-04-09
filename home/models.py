from django.db import models
from django.contrib.auth.models import User
from froala_editor.fields import FroalaField
from .helpers import *

class BlogModel(models.Model):
    title = models.CharField(max_length=200)
    content = FroalaField()
    slug = models.SlugField(max_length=1000,null=True,blank=True)
    user = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)
    image = models.ImageField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


    def save(self,*args,**kwargs):
        self.slug = generate_slug(self.title)
        super(BlogModel,self).save(*args,**kwargs)