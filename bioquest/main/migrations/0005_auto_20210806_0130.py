# Generated by Django 3.2.6 on 2021-08-05 22:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_auto_20210806_0124'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='varlist',
            options={'ordering': ['parent_question'], 'verbose_name': 'Вариант ответа', 'verbose_name_plural': 'Варианты ответа'},
        ),
        migrations.AlterField(
            model_name='varlist',
            name='var',
            field=models.CharField(max_length=100, verbose_name='Текст варианта'),
        ),
    ]
