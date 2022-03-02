# Generated by Django 3.1 on 2020-09-21 20:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Application',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=256)),
                ('last_name', models.CharField(max_length=256)),
                ('email', models.EmailField(max_length=256)),
                ('mobile', models.CharField(max_length=256)),
                ('information', models.CharField(max_length=5000)),
                ('upload_resume', models.FileField(upload_to='images')),
            ],
        ),
    ]