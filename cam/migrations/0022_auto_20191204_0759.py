# Generated by Django 2.2.6 on 2019-12-04 07:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cam', '0021_auto_20191129_1513'),
    ]

    operations = [
        migrations.CreateModel(
            name='Site',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='Reparation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_reparation', models.DateTimeField(blank=True, null=True)),
                ('frais', models.DecimalField(decimal_places=2, max_digits=10)),
                ('descriptif', models.TextField()),
                ('camera', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Camera', to='cam.Camera')),
            ],
        ),
        migrations.AddField(
            model_name='camera',
            name='site',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Site', to='cam.Site'),
        ),
    ]
