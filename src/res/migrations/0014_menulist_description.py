# Generated by Django 4.0.6 on 2022-07-07 11:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('res', '0013_menulist_ven'),
    ]

    operations = [
        migrations.AddField(
            model_name='menulist',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
    ]
