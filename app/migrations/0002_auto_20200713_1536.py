# Generated by Django 3.0.8 on 2020-07-13 13:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='film',
            name='csfd_link',
            field=models.CharField(max_length=150, null=True),
        ),
    ]
