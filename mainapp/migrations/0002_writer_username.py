# Generated by Django 3.1.1 on 2020-10-26 17:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='writer',
            name='username',
            field=models.CharField(max_length=10, null=True),
        ),
    ]