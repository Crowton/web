# Generated by Django 3.2 on 2021-04-20 20:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0005_alter_failedgameupload_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='failedgameupload',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
