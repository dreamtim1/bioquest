# Generated by Django 3.2.6 on 2021-08-05 20:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('slug', models.SlugField(max_length=100)),
            ],
            options={
                'verbose_name': 'Раздел',
                'verbose_name_plural': 'Разделы',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.IntegerField(verbose_name='Год')),
                ('stage', models.CharField(max_length=100, verbose_name='Олимпиада')),
                ('grade', models.IntegerField(verbose_name='Класс')),
                ('part', models.IntegerField(verbose_name='Часть')),
                ('number', models.IntegerField(verbose_name='Номер')),
                ('text', models.TextField(verbose_name='Текст вопроса')),
                ('image1', models.ImageField(blank=True, upload_to='')),
                ('image2', models.ImageField(blank=True, upload_to='')),
                ('image3', models.ImageField(blank=True, upload_to='')),
                ('imageA1', models.ImageField(blank=True, upload_to='')),
                ('imageA2', models.ImageField(blank=True, upload_to='')),
                ('imageA3', models.ImageField(blank=True, upload_to='')),
                ('tags', models.ManyToManyField(blank=True, related_name='qs', to='main.Tag')),
            ],
            options={
                'verbose_name': 'Вопрос',
                'verbose_name_plural': 'Вопросы',
                'ordering': ['-id'],
            },
        ),
    ]