# Generated by Django 4.2.4 on 2023-10-14 10:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('persons', '0005_alter_person_purpose'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='person',
            name='purpose',
        ),
    ]
