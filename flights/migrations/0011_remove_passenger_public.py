# Generated by Django 4.1.4 on 2022-12-25 22:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("flights", "0010_delete_userspasswordf_passenger_temp"),
    ]

    operations = [
        migrations.RemoveField(model_name="passenger", name="public",),
    ]
