# Generated by Django 3.2.5 on 2022-01-25 17:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_alter_user_nickname'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='hashed_password',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
