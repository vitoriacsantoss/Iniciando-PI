# Generated by Django 5.0.6 on 2024-10-04 17:56

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0011_delete_tipousuario"),
        ("uploader", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="imoveis",
            name="foto",
        ),
        migrations.AddField(
            model_name="imoveis",
            name="foto",
            field=models.ForeignKey(
                blank=True,
                default=None,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="+",
                to="uploader.image",
            ),
        ),
    ]
