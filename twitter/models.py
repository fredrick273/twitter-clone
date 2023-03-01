from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    pic = models.ImageField(upload_to='media/',default='default.jpg')
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    birth_date = models.DateField(null=True,blank=True)
    totalfollowers = models.IntegerField(null=True,blank=True)
    totalfollowing = models.IntegerField(null=True,blank=True)
    bio = models.TextField(max_length=200,blank=True)
    creation_date = models.DateTimeField(auto_now_add=True,blank= True)


    def __str__(self):
        return self.user.username
    
class Followers(models.Model):
    followersprofile = models.ManyToManyField(Profile,related_name="profile_followers",blank=True)
    followingprofile = models.ManyToManyField(Profile,related_name="profile_following",blank=True)
    profileuser = models.ForeignKey(Profile,on_delete=models.CASCADE)

    def totalfollowers(self):
        return self.followersprofile.count()
    
    def totalfollowing(self):
        return self.followingprofile.count()

class Tweet(models.Model):
    user = models.ForeignKey(Profile,on_delete=models.CASCADE)
    content = models.TextField(max_length=300)
    created_time = models.DateTimeField(auto_now_add=True)
    replycount = models.IntegerField(default=0)
    likes = models.ManyToManyField(Profile,related_name='tweet_likes')
    image = models.ImageField(upload_to='tweetimg/',blank=True,null=True)

    def totallike(self):
        return self.likes.count()



class Comment(models.Model):
    tweet = models.ForeignKey(Tweet,on_delete=models.CASCADE,null=True,blank=True)
    commenter = models.ForeignKey(Profile,on_delete=models.CASCADE,null=True,blank=True)
    content = models.TextField(max_length=200,null=True,blank=True)
    like = models.IntegerField(default=0,null=True,blank=True)
    created_time = models.DateTimeField(auto_now_add=True,blank=True)
