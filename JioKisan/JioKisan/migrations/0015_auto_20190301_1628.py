# Generated by Django 2.1.3 on 2019-03-01 16:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('JioKisan', '0014_auto_20190226_1950'),
    ]

    operations = [
        migrations.AddField(
            model_name='user_reg',
            name='available_capacity',
            field=models.IntegerField(blank=True, default=None, null=True),
        ),
        migrations.AddField(
            model_name='user_reg',
            name='current_address',
            field=models.CharField(blank=True, default=None, max_length=40, null=True),
        ),
        migrations.AddField(
            model_name='user_reg',
            name='current_position_latitude',
            field=models.FloatField(blank=True, default=None, null=True),
        ),
        migrations.AddField(
            model_name='user_reg',
            name='current_position_longitude',
            field=models.FloatField(blank=True, default=None, null=True),
        ),
        migrations.AddField(
            model_name='user_reg',
            name='isHired',
            field=models.BooleanField(blank=True, default=None, null=True),
        ),
        migrations.AddField(
            model_name='user_reg',
            name='path',
            field=models.CharField(blank=True, default=None, max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='consignment',
            name='truck',
            field=models.ForeignKey(blank=True, db_column='PAN', default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='JioKisan.User_reg'),
        ),
    ]