# Generated by Django 2.2.7 on 2019-11-13 13:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rubric', '0003_commetn'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Commetn',
            new_name='Comment',
        ),
    ]