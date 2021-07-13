# Generated by Django 3.2.4 on 2021-06-29 16:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('adminPiezas', '0006_rename_fnln_paramedico_nombre'),
    ]

    operations = [
        migrations.RenameField(
            model_name='paramedico',
            old_name='nombre',
            new_name='nombreP',
        ),
        migrations.AlterField(
            model_name='pieza',
            name='paramedico',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='adminPiezas.paramedico'),
        ),
    ]