# Generated by Django 2.2.16 on 2022-01-16 20:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("reviews", "0008_auto_20220117_0117"),
    ]

    operations = [
        migrations.AddField(
            model_name="title",
            name="year",
            field=models.IntegerField(
                db_index=True, null=True, verbose_name="Год издания"
            ),
        ),
    ]
