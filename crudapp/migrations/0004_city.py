# Generated by Django 3.2.6 on 2021-08-06 07:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crudapp', '0003_gender'),
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('City', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'citytable',
            },
        ),
    ]