# Generated by Django 2.1.7 on 2020-06-29 17:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ProTransApp', '0002_auto_20200626_0923'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuario',
            name='tipo_transporte',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='ProTransApp.Tipo_transporte'),
        ),
    ]
