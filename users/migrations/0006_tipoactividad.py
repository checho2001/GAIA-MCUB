# Generated by Django 4.1.3 on 2022-11-21 17:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_rename_especimen_ejemplar'),
    ]

    operations = [
        migrations.CreateModel(
            name='TipoActividad',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombreactividad', models.CharField(max_length=50)),
            ],
        ),
    ]