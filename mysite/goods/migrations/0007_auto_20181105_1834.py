# Generated by Django 2.1.2 on 2018-11-05 15:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('goods', '0006_auto_20181103_1631'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Recomend',
        ),
        migrations.AddField(
            model_name='goods',
            name='recomendation_list',
            field=models.TextField(null=True),
        ),
    ]
