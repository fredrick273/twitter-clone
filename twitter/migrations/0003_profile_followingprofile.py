# Generated by Django 4.1.6 on 2023-03-01 18:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('twitter', '0002_tweet_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='followingprofile',
            field=models.ManyToManyField(blank=True, related_name='Profile_followers', to='twitter.profile'),
        ),
    ]
