# Generated by Django 3.1.6 on 2021-02-04 18:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0005_remove_book_language'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='author',
            options={'ordering': ['last_name']},
        ),
    ]
