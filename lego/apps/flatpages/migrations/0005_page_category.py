# Generated by Django 2.1.2 on 2019-01-17 19:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("flatpages", "0004_auto_20180406_1730")]

    operations = [
        migrations.AddField(
            model_name="page",
            name="category",
            field=models.CharField(
                choices=[
                    ("generelt", "generelt"),
                    ("bedrifter", "bedrifter"),
                    ("arrangementer", "arrangementer"),
                    ("undergrupper", "undergrupper"),
                    ("interessegrupper", "interessegrupper"),
                ],
                default="generelt",
                max_length=50,
            ),
        )
    ]