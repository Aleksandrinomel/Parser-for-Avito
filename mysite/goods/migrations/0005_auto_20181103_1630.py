# Generated by Django 2.1.2 on 2018-11-03 13:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('goods', '0004_recomend'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='recomend',
            name='five_nearest',
        ),
        migrations.AddField(
            model_name='recomend',
            name='id_recommend',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='recomend',
            name='weight',
            field=models.TextField(null=True),
        ),
    ]