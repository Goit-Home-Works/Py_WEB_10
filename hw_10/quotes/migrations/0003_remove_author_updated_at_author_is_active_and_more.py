# Generated by Django 5.0.3 on 2024-03-16 09:40

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("quotes", "0002_alter_author_born_location_alter_author_fullname"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="author",
            name="updated_at",
        ),
        migrations.AddField(
            model_name="author",
            name="is_active",
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name="author",
            name="description",
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name="author",
            name="fullname",
            field=models.CharField(max_length=120, unique=True),
        ),
        migrations.AlterField(
            model_name="quote",
            name="author",
            field=models.ForeignKey(
                default=None,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="quotes.author",
            ),
        ),
        migrations.AlterField(
            model_name="tag",
            name="name",
            field=models.CharField(max_length=50, unique=True),
        ),
    ]
