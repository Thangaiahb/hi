# Generated by Django 5.0.4 on 2024-04-25 11:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='feedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('User_Name', models.CharField(max_length=50)),
                ('Mobile', models.BigIntegerField()),
                ('FeedBack', models.CharField(max_length=100)),
            ],
        ),
    ]
