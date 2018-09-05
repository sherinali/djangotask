# Generated by Django 2.0.7 on 2018-09-04 20:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Evnts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=300)),
                ('details', models.CharField(max_length=850)),
                ('address', models.CharField(max_length=300)),
                ('source', models.CharField(max_length=500)),
                ('dates', models.DateField()),
                ('username', models.CharField(max_length=250)),
                ('disabled', models.BooleanField(default=False)),
            ],
        ),
    ]