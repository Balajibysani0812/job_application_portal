# Generated by Django 3.1 on 2020-09-21 20:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('apply', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='application',
            old_name='email',
            new_name='mail',
        ),
        migrations.RenameField(
            model_name='application',
            old_name='upload_resume',
            new_name='resume_file',
        ),
    ]