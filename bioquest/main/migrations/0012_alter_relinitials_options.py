# Generated by Django 3.2.6 on 2021-08-06 00:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0011_auto_20210806_0328'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='relinitials',
            options={'ordering': ['parent_question'], 'verbose_name': 'RelInitial', 'verbose_name_plural': 'RelInitials'},
        ),
    ]
