from django.db import models
from django.contrib.auth.models import User
class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    phone = models.CharField(null=True,max_length=20)
    def __str__(self):
        return self.user.username

class News(models.Model):
    theme = models.CharField(max_length=300,null=True)
    text = models.CharField(max_length=1000,null=True)
    tag = models.CharField(max_length=50,null=True)
    image = models.ImageField(null=True)
    added_date = models.DateTimeField(auto_now_add=True)
    like = models.IntegerField(default=0)
    dis_like = models.IntegerField(default=0)
    views = models.IntegerField(default=0)
    @property
    def imageURL(self):
        try:
            return self.image.url
        except Exception as e:
            return ''
    def __str__(self):
        return self.theme
    @property
    def add_like(self):
        self.like += 1
    @property
    def add_dis_like(self):
        self.dis_like += 1
    @property
    def sub_like(self):
        self.like -= 1
    @property
    def sub_dis_like(self):
        self.dis_like -= 1
    @property
    def add_view(self):
        self.views += 1

class Comment(models.Model):
    new = models.ForeignKey(News,on_delete=models.CASCADE)
    user = models.ForeignKey(Profile,on_delete=models.SET_NULL,null=True)
    text = models.CharField(max_length=2000,null=True)
class Like_Dislike(models.Model):
    new = models.ForeignKey(News,on_delete=models.CASCADE)
    user = models.ForeignKey(Profile,on_delete=models.CASCADE)
    like_dislike = models.BooleanField(null=True)
