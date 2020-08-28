# Generated by Django 2.2.1 on 2020-08-27 17:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('theme', '0002_delete_works'),
    ]

    operations = [
        migrations.CreateModel(
            name='works',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('v_name', models.CharField(max_length=200)),
                ('pub_date', models.DateTimeField(verbose_name='date published')),
                ('v_organ', models.CharField(max_length=200)),
                ('body', models.TextField()),
            ],
        ),
    ]
