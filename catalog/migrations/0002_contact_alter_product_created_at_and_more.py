# Generated by Django 5.0.6 on 2024-06-11 09:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("catalog", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Contact",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=100, verbose_name="Имя")),
                ("phone", models.CharField(max_length=20, verbose_name="Телефон")),
                ("message", models.TextField(verbose_name="Сообщение")),
                (
                    "created_at",
                    models.DateTimeField(
                        auto_now_add=True, verbose_name="Дата создания"
                    ),
                ),
            ],
            options={
                "verbose_name": "Сообщение",
                "verbose_name_plural": "Сообщения",
                "ordering": ["-created_at"],
            },
        ),
        migrations.AlterField(
            model_name="product",
            name="created_at",
            field=models.DateTimeField(auto_now_add=True, verbose_name="Дата создания"),
        ),
        migrations.AlterField(
            model_name="product",
            name="description",
            field=models.TextField(
                blank=True,
                help_text="Введите описание товара",
                null=True,
                verbose_name="Описание",
            ),
        ),
        migrations.AlterField(
            model_name="product",
            name="updated_at",
            field=models.DateTimeField(auto_now=True, verbose_name="Дата изменения"),
        ),
    ]