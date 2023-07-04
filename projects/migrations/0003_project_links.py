# Generated by Django 4.1.7 on 2023-07-03 23:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_links'),
        ('projects', '0002_project_domains'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='links',
            field=models.ManyToManyField(related_name='links', to='home.links'),
        ),
    ]
