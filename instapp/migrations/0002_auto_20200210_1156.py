# Generated by Django 2.2.9 on 2020-02-10 11:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('instapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='comment',
            field=models.CharField(max_length=140, null=True),
        ),
    ]