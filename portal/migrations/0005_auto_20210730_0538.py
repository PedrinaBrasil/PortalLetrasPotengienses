# Generated by Django 3.2.5 on 2021-07-30 08:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0004_author_photo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='author',
            name='books',
        ),
        migrations.AddField(
            model_name='book',
            name='authors',
            field=models.ManyToManyField(to='portal.Author'),
        ),
        migrations.AlterField(
            model_name='author',
            name='photo',
            field=models.ImageField(default='media/authors/no_image.png', upload_to='media/authors/'),
        ),
        migrations.AlterField(
            model_name='book',
            name='cover',
            field=models.ImageField(default='media/covers/no_image.png', upload_to='media/covers/'),
        ),
        migrations.AlterField(
            model_name='book',
            name='summary',
            field=models.TextField(null=True),
        ),
    ]
