# Generated by Django 4.2.7 on 2023-11-30 06:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sitioApp', '0002_alter_descarga_descripcion_alter_descarga_tamaño'),
    ]

    operations = [
        migrations.AlterField(
            model_name='descarga',
            name='descarga',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
    ]