# Generated by Django 2.1.3 on 2018-12-19 08:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('JioKisan', '0005_auto_20181219_0841'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categary',
            name='cid',
            field=models.IntegerField(default=5),
        ),
        migrations.AlterField(
            model_name='phoneuser',
            name='chat_state',
            field=models.CharField(max_length=10),
        ),
    ]
