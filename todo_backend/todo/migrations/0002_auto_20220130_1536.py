# Generated by Django 3.2.11 on 2022-01-30 14:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='todo',
            table='todo',
        ),
        migrations.AlterModelTable(
            name='todolist',
            table='todo_list',
        ),
    ]