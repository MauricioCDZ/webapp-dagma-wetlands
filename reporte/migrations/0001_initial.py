# Generated by Django 3.1.3 on 2021-04-16 02:10

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import reporte.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Comuna',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero', models.IntegerField()),
                ('dateCreated', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='FamiliaFauna',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=200)),
                ('dateCreated', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='FamiliaFlora',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=200)),
                ('dateCreated', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='FaunaAcuatica',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=200)),
                ('foto', models.ImageField(upload_to='faunaAcuatica/', verbose_name='Image')),
                ('dateCreated', models.DateTimeField(auto_now_add=True)),
                ('familia', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reporte.familiafauna')),
            ],
        ),
        migrations.CreateModel(
            name='FaunaAcuaticaHumedal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dateCreated', models.DateTimeField(auto_now_add=True)),
                ('nombreFaunaAcuatica', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reporte.faunaacuatica')),
            ],
        ),
        migrations.CreateModel(
            name='FaunaTerrestre',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=200)),
                ('foto', models.ImageField(upload_to='faunaTerrestre/', verbose_name='Image')),
                ('dateCreated', models.DateTimeField(auto_now_add=True)),
                ('familia', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reporte.familiafauna')),
            ],
        ),
        migrations.CreateModel(
            name='FaunaTerrestreHumedal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dateCreated', models.DateTimeField(auto_now_add=True)),
                ('nombreFauna', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reporte.faunaterrestre')),
            ],
        ),
        migrations.CreateModel(
            name='Flora',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=200)),
                ('foto', models.ImageField(upload_to='flora/', verbose_name='Image')),
                ('dateCreated', models.DateTimeField(auto_now_add=True)),
                ('familia', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reporte.familiaflora')),
            ],
        ),
        migrations.CreateModel(
            name='FloraHumedal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dateCreated', models.DateTimeField(auto_now_add=True)),
                ('nombreFlora', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reporte.flora')),
            ],
        ),
        migrations.CreateModel(
            name='Humedal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=200)),
                ('areaEstacional', models.FloatField()),
                ('areaPermanente', models.FloatField()),
                ('latitud', models.FloatField()),
                ('altitud', models.FloatField()),
                ('dateCreated', models.DateTimeField(auto_now_add=True)),
                ('FaunaAcuatica', models.ManyToManyField(through='reporte.FaunaAcuaticaHumedal', to='reporte.FaunaAcuatica')),
                ('faunaTerrestre', models.ManyToManyField(through='reporte.FaunaTerrestreHumedal', to='reporte.FaunaTerrestre')),
                ('flora', models.ManyToManyField(through='reporte.FloraHumedal', to='reporte.Flora')),
                ('jurisdiccion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reporte.comuna')),
            ],
        ),
        migrations.CreateModel(
            name='InvolucrateMensaje',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=200)),
                ('correoElectronico', models.EmailField(max_length=200)),
                ('asunto', models.CharField(max_length=200)),
                ('descripcion', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='TipoHumedal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=200)),
                ('numAsignado', models.IntegerField()),
                ('dateCreated', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='TipoReporte',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=200)),
                ('dateCreated', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Reporte',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=100)),
                ('descripcion', models.TextField()),
                ('fecha_reporte', models.DateTimeField(default=django.utils.timezone.now)),
                ('image', models.ImageField(upload_to='reporte_pics', validators=[reporte.models.validate_image])),
                ('status', models.CharField(choices=[('Visible', 'Visible'), ('Invisible', 'Invisible')], max_length=200)),
                ('importancia', models.CharField(choices=[('Muy Importante', 'Muy Importante'), ('Regular', 'Regular')], max_length=200)),
                ('autor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('nombreHumedal', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reporte.humedal')),
                ('tipoReporte', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reporte.tiporeporte')),
            ],
        ),
        migrations.AddField(
            model_name='humedal',
            name='tipoHumedal',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reporte.tipohumedal'),
        ),
        migrations.AddField(
            model_name='florahumedal',
            name='nombreHumedal',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reporte.humedal'),
        ),
        migrations.AddField(
            model_name='faunaterrestrehumedal',
            name='nombreHumedal',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reporte.humedal'),
        ),
        migrations.AddField(
            model_name='faunaacuaticahumedal',
            name='nombreHumedal',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reporte.humedal'),
        ),
    ]
