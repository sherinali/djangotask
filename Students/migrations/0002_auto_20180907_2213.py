# Generated by Django 2.0.6 on 2018-09-07 19:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Students', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Authentication',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_type', models.CharField(choices=[('manger', 'manger'), ('student', 'student'), ('sponser', 'sponser')], max_length=200)),
            ],
        ),
        migrations.AddField(
            model_name='req_st',
            name='disable',
            field=models.BooleanField(default=False),
        ),
    ]
