# Generated by Django 4.2.6 on 2023-10-31 06:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='autor',
            options={'ordering': ['nombre'], 'verbose_name_plural': 'Autores'},
        ),
        migrations.AlterModelOptions(
            name='editor',
            options={'ordering': ['nombre'], 'verbose_name_plural': 'Editores'},
        ),
        migrations.AlterModelOptions(
            name='libro',
            options={'ordering': ['titulo'], 'verbose_name_plural': 'Libros'},
        ),
    ]
