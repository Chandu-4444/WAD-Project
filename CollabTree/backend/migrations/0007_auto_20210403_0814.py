# Generated by Django 3.1.7 on 2021-04-03 08:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0006_userattribs_user_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userattribs',
            name='user_image',
            field=models.ImageField(blank=True, upload_to='images'),
        ),
    ]
