# Generated by Django 4.1.2 on 2022-11-16 22:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='footballlingo',
            fields=[
                ('lingoid', models.IntegerField(primary_key=True, serialize=False)),
                ('term', models.CharField(max_length=30)),
                ('description', models.CharField(max_length=5000)),
            ],
        ),
    ]
