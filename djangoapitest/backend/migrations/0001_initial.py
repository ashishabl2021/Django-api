# Generated by Django 4.2.2 on 2023-06-27 06:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Box',
            fields=[
                ('Box_ID', models.IntegerField(primary_key=True, serialize=False)),
                ('Box_material', models.CharField(max_length=50)),
                ('QTY_material', models.CharField(max_length=50)),
            ],
        ),
    ]
