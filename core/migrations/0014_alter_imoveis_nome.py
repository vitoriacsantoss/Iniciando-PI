# Generated by Django 5.0.6 on 2024-12-13 15:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0013_imoveis_nome"),
    ]

    operations = [
        migrations.AlterField(
            model_name="imoveis",
            name="nome",
            field=models.CharField(max_length=255),
        ),
    ]