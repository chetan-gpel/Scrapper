# Generated by Django 3.2.5 on 2021-09-22 13:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scraper', '0011_remove_new_scraper'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Course',
        ),
        migrations.AddField(
            model_name='new',
            name='email',
            field=models.EmailField(default=1, max_length=254),
            preserve_default=False,
        ),
    ]
