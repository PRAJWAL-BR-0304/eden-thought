# Generated by Django 5.0.7 on 2024-08-06 16:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('journal', '0002_profile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='profile_pic',
            field=models.ImageField(blank=True, default='Default.png', null=True, upload_to='media/'),
        ),
    ]
