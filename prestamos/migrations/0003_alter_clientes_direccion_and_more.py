# Generated by Django 4.2.5 on 2024-12-18 01:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('prestamos', '0002_alter_prestamos_fecha_solicitud'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clientes',
            name='direccion',
            field=models.CharField(default='direccion 12345', max_length=255),
        ),
        migrations.AlterField(
            model_name='clientes',
            name='identificacion',
            field=models.CharField(default='123456789', max_length=45),
        ),
        migrations.AlterField(
            model_name='clientes',
            name='telefono',
            field=models.CharField(default='+54 11 1234-5678', max_length=25),
        ),
    ]