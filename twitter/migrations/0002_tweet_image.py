# Generated by Django 4.1.6 on 2023-03-01 16:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('twitter', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='tweet',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='tweetimg/'),
        ),
    ]
