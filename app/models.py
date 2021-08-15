from django.db import models
from embed_video.fields import EmbedVideoField
class data(models.Model):
    id = models.AutoField(auto_created = True,primary_key = True)
    name = models.CharField(max_length = 150,unique = True)
    language = models.CharField(max_length = 50)
    actor = models.CharField(max_length = 50)
    actress = models.CharField(max_length = 50)
    released = models.IntegerField()
    link = EmbedVideoField()
    duration = models.CharField(max_length = 50)
    genre = models.CharField(max_length = 50)
    
    class Meta:
        def __str__(self):
            return str(self.name)