# Generated by Django 3.2.7 on 2021-09-28 21:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hero', '0003_hero_blurb'),
    ]

    operations = [
        migrations.RenameField(
            model_name='hero',
            old_name='blurb',
            new_name='identity',
        ),
    ]
