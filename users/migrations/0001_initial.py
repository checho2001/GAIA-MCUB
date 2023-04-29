# Generated by Django 4.1.3 on 2023-04-29 18:38

from django.conf import settings
import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import users.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=60)),
                ('nombre', models.CharField(max_length=60)),
                ('apellido', models.CharField(max_length=60)),
                ('email', models.EmailField(db_index=True, max_length=255, unique=True)),
                ('password', models.CharField(max_length=50)),
                ('estado', models.BooleanField(default=True)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Area',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Clase',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombreClase', models.CharField(max_length=50)),
                ('estado', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='departamento',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='especimen',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('NumeroCatalogo', models.CharField(max_length=500, unique=True)),
                ('NombreDelConjuntoDatos', models.CharField(max_length=500)),
                ('ComentarioRegistroBiologico', models.CharField(max_length=500)),
                ('RegistradoPor', models.CharField(max_length=500)),
                ('NumeroIndividuo', models.CharField(max_length=500)),
                ('FechaEvento', models.DateField(blank=True, max_length=500, null=True)),
                ('Habitad', models.CharField(max_length=500)),
                ('Departamento', models.CharField(max_length=500)),
                ('Municipio', models.CharField(max_length=500)),
                ('IdentificadoPor', models.CharField(max_length=500)),
                ('FechaIdentificacion', models.DateField(blank=True, max_length=500, null=True)),
                ('IdentificacionReferencias', models.CharField(max_length=500)),
                ('ComentarioIdentificacion', models.CharField(max_length=500)),
                ('NombreCientificoComentarioRegistroBiologico', models.CharField(max_length=500)),
                ('ClaseE', models.CharField(max_length=500)),
                ('Orden', models.CharField(max_length=500)),
                ('Genero', models.CharField(max_length=500)),
                ('Familia', models.CharField(max_length=500)),
                ('NombreComun', models.CharField(max_length=500)),
                ('estado', models.BooleanField(default=True)),
                ('Image', models.ImageField(default='media/en_construccion.png', upload_to='media/')),
            ],
        ),
        migrations.CreateModel(
            name='familia',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombreFamilia', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Genero',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombreGenero', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Imagenes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='media/')),
            ],
        ),
        migrations.CreateModel(
            name='Orden',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombreOrden', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Rol',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombrerol', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Text',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('content', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='TipoActividad',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombreactividad', models.CharField(max_length=500)),
                ('estado', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='UserAction',
            fields=[
                ('id_user_action', users.fields.ActionField(primary_key=True, serialize=False)),
                ('tarea', models.CharField(max_length=100)),
                ('ejemplar', models.CharField(max_length=100)),
                ('tiempo', models.DateTimeField(auto_now_add=True)),
                ('estado', models.BooleanField(default=False)),
                ('Descripcion', models.CharField(max_length=500)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='municipio',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('municipio', models.CharField(max_length=50)),
                ('departamento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.departamento')),
            ],
        ),
        migrations.CreateModel(
            name='Class_User',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('id_clase', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.clase')),
                ('id_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Area_User',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('id_area', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.area')),
                ('id_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Actividades',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('NumeroCatalogo', models.CharField(max_length=50)),
                ('Hora', models.TimeField(max_length=50)),
                ('Fecha', models.DateField(max_length=50)),
                ('Descripcion', models.CharField(max_length=1000)),
                ('TareaRealizada', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.tipoactividad')),
            ],
        ),
        migrations.AddField(
            model_name='user',
            name='rol',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.rol'),
        ),
        migrations.AddField(
            model_name='user',
            name='user_permissions',
            field=models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions'),
        ),
    ]
