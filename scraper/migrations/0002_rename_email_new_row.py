# Generated by Django 3.2.5 on 2021-08-02 05:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('scraper', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='new',
            old_name='email',
            new_name='row',
        ),
    ]
