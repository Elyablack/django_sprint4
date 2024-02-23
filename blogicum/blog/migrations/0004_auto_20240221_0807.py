# Generated by Django 3.2.16 on 2024-02-21 05:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20240220_1854'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ('-pub_date',), 'verbose_name': 'публикация', 'verbose_name_plural': 'Публикации'},
        ),
        migrations.AlterField(
            model_name='category',
            name='description',
            field=models.TextField(verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='post',
            name='text',
            field=models.TextField(verbose_name='Текст'),
        ),
    ]
