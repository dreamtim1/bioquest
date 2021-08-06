# Generated by Django 3.2.6 on 2021-08-05 22:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20210805_2342'),
    ]

    operations = [
        migrations.CreateModel(
            name='VarList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('var', models.CharField(max_length=100, verbose_name='Вариант ответа')),
                ('is_right', models.BooleanField(verbose_name='Правильность')),
            ],
        ),
        migrations.AddField(
            model_name='question',
            name='vars',
            field=models.ManyToManyField(related_name='vs', to='main.VarList'),
        ),
    ]
