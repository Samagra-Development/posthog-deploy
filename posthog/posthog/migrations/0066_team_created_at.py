# Generated by Django 3.0.7 on 2020-06-23 17:13

from django.db import migrations, models
from django.utils.timezone import now


class Migration(migrations.Migration):

    dependencies = [
        ("posthog", "0065_auto_20200624_1842"),
    ]

    operations = [
        migrations.AddField(
            model_name="team",
            name="created_at",
            field=models.DateTimeField(auto_now_add=True, default=now),
            preserve_default=False,
        ),
    ]
