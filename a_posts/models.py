from django.db import models
import uuid

class Post(models.Model):
    title = models.CharField(max_length=500)
  #  artist = models.CharField(max_length=500, null=True)
  #  url = models.URLField(max_length=500, null=True) 
    image = models.URLField(max_length=500)
   # author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='posts')
    body = models.TextField()
   # likes = models.ManyToManyField(User, related_name="likedposts", through="LikedPost")
 #   tags = models.ManyToManyField('Tag')
    created = models.DateTimeField(auto_now_add=True)
    id = models.CharField(max_length=100, default=uuid.uuid4, unique=True, primary_key=True, editable=False)


    def __str__(self):
        return str(self.title)