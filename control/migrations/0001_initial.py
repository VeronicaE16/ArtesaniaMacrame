# Generated by Django 4.0.6 on 2022-09-14 20:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Material',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50, verbose_name='Nombre')),
                ('precio', models.FloatField(verbose_name='Precio')),
                ('categoria', models.CharField(choices=[('Hilo', 'Hilo'), ('Pepitas', 'Pepitas')], max_length=50, verbose_name='Categoria')),
                ('cantidad', models.IntegerField(verbose_name='Cantidad de material')),
                ('metodo', models.CharField(choices=[('Efectivo', 'Efectivo')], default='Efectivo', max_length=50, verbose_name='Metodo de pago')),
                ('estado', models.CharField(choices=[('Existente', 'Existente'), ('Agotado', 'Agotado')], default='Existente', max_length=50, verbose_name='Estado')),
            ],
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.TextField(max_length=100, verbose_name='Descripción')),
                ('precio', models.FloatField(verbose_name='Precio')),
                ('categoria', models.CharField(choices=[('Llaveros', 'Llaveros'), ('Atrapasueños', 'Atrapasueños'), ('Masetas', 'Masetas'), ('Manillas', 'Manillas')], max_length=50, verbose_name='Categoria')),
                ('ganancia', models.CharField(choices=[('0.65', '65%'), ('0.7', '70%'), ('0.75', '75%')], max_length=50, verbose_name='Ganancia')),
                ('estado', models.CharField(choices=[('Existente', 'Existente'), ('Agotado', 'Agotado')], default='Existente', max_length=50, verbose_name='Estado')),
            ],
        ),
        migrations.CreateModel(
            name='Produccion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fechai', models.DateField(verbose_name='Fecha de inicio')),
                ('fechaf', models.DateField(verbose_name='Fecha final')),
                ('cantidad_material', models.IntegerField(verbose_name='Cantidad de material')),
                ('gastos', models.IntegerField(default=0)),
                ('estado', models.CharField(choices=[('Activo', 'Activo'), ('Inactivo', 'Inactivo')], default='Activo', max_length=50, verbose_name='Estado')),
                ('material', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='control.material', verbose_name='Material')),
                ('producto', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='control.producto', verbose_name='Producto')),
            ],
        ),
    ]
