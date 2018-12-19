# Generated by Django 2.1.3 on 2018-12-19 06:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categary',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('MSP', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='PhoneUser',
            fields=[
                ('phone_number', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=40)),
                ('session_time', models.DateTimeField()),
                ('chat_state', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Sellable',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cost', models.IntegerField()),
                ('categary', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='JioKisan.Categary')),
                ('seller', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='JioKisan.PhoneUser')),
            ],
        ),
    ]
