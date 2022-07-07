# Generated by Django 4.0.6 on 2022-07-07 18:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('res', '0014_menulist_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='rslist',
            name='mulcui',
            field=models.CharField(choices=[('multicuision', 'multicuision'), ('cuision', 'cuision')], default='1', max_length=20),
        ),
        migrations.AlterField(
            model_name='rslist',
            name='type',
            field=models.CharField(choices=[('veg', 'veg'), ('non-veg', 'non-veg')], default='1', max_length=10),
        ),
    ]