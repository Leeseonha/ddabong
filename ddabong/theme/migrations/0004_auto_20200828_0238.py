# Generated by Django 2.2.1 on 2020-08-27 17:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('theme', '0003_works'),
    ]

    operations = [
        migrations.AddField(
            model_name='works',
            name='v_finish',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='works',
            name='v_member',
            field=models.IntegerField(default=True),
        ),
        migrations.AddField(
            model_name='works',
            name='v_point',
            field=models.IntegerField(default=True),
        ),
        migrations.AlterField(
            model_name='works',
            name='v_organ',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]