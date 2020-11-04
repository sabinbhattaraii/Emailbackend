# Generated by Django 3.1.3 on 2020-11-03 16:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=200)),
                ('Age', models.IntegerField()),
                ('Email', models.EmailField(max_length=254)),
                ('Message', models.TextField()),
                ('Video', models.FileField(upload_to='')),
            ],
        ),
    ]
