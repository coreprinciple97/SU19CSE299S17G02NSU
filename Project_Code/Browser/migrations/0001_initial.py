# Generated by Django 2.2.3 on 2019-07-26 15:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Books',
            fields=[
                ('Book_ID', models.IntegerField(primary_key=True, serialize=False)),
                ('Title', models.CharField(max_length=150)),
                ('Author', models.CharField(max_length=150)),
                ('Genre1', models.CharField(max_length=150)),
                ('Genre2', models.CharField(max_length=150)),
                ('Plot', models.TextField()),
            ],
        ),
    ]
