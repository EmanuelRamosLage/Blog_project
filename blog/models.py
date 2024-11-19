from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length= 100)                        # Use this one for simple sentences
    content = models.TextField()                                     # Use this one for multiple lines text
    date_posted = models.DateTimeField(default= timezone.now)        # Inside this class there's a boolean called 'auto_now=bool'. It updates the value of date every time the post is modified if True. It's great for 'last updated'
    author = models.ForeignKey(User, on_delete= models.CASCADE)      # 'on_delete' means 'what will happen to this post after the user is deleted?'. 'models.CASCADE' means that this post will also be deleted

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse("post-detail", kwargs={"pk": self.pk})
    