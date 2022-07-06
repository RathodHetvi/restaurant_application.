# Generated by Django 4.0.5 on 2022-07-05 04:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('res', '0002_rslist_delete_res'),
    ]

    operations = [
        migrations.CreateModel(
            name='Menulist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item', models.CharField(max_length=120)),
                ('price', models.IntegerField()),
                ('menu', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='res.rslist')),
            ],
        ),
    ]