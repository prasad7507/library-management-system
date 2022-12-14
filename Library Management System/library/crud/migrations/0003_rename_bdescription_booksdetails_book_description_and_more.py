# Generated by Django 4.1 on 2022-08-11 14:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crud', '0002_alter_booksdetails_bid'),
    ]

    operations = [
        migrations.RenameField(
            model_name='booksdetails',
            old_name='bdescription',
            new_name='book_description',
        ),
        migrations.RenameField(
            model_name='booksdetails',
            old_name='bname',
            new_name='book_name',
        ),
        migrations.RemoveField(
            model_name='booksdetails',
            name='bid',
        ),
        migrations.RemoveField(
            model_name='booksdetails',
            name='id',
        ),
        migrations.AddField(
            model_name='booksdetails',
            name='book_id',
            field=models.IntegerField(default=1, primary_key=True, serialize=False),
            preserve_default=False,
        ),
    ]
