# Generated by Django 2.2.4 on 2019-08-12 00:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("games", "0006_auto_20190812_0254")]

    operations = [
        migrations.AlterField(
            model_name="card",
            name="drawn_datetime",
            field=models.DateTimeField(blank=True, null=True),
        )
    ]
