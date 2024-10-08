# Generated by Django 4.1 on 2024-08-26 19:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='APTEST',
            fields=[
                ('num', models.AutoField(primary_key=True, serialize=False)),
                ('libelle', models.CharField(max_length=255)),
                ('ap', models.FloatField()),
                ('annee', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='etat_project',
            fields=[
                ('id_etat', models.IntegerField(primary_key=True, serialize=False)),
                ('nom_etat', models.CharField(max_length=100)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='project',
            fields=[
                ('id_project', models.AutoField(primary_key=True, serialize=False)),
                ('Libelle', models.CharField(max_length=150)),
                ('num_indiv', models.CharField(max_length=150)),
                ('AP_Act', models.FloatField()),
                ('dp_cum', models.FloatField()),
                ('PEC', models.FloatField()),
                ('dp_prev', models.FloatField()),
                ('date_chng', models.DateField()),
                ('etat_project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.etat_project')),
            ],
        ),
        migrations.CreateModel(
            name='sector',
            fields=[
                ('id_sect', models.IntegerField(primary_key=True, serialize=False)),
                ('nom_sect', models.CharField(max_length=100)),
                ('id_project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.project')),
            ],
        ),
        migrations.CreateModel(
            name='operation',
            fields=[
                ('id_libelle_op', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('num_op', models.CharField(max_length=100)),
                ('object_vise_po', models.TextField()),
                ('notifcation_an_MF_op', models.TextField()),
                ('indiv_an_op', models.TextField()),
                ('AP_init_op', models.FloatField()),
                ('AP_real_op', models.FloatField(default=0.0)),
                ('cum_AP_eng_an_op', models.FloatField(default=0.0)),
                ('cum_AP_pai_an_op', models.FloatField(default=0.0)),
                ('taux_real_ph_an_op', models.FloatField(default=0.0)),
                ('date_cre_op', models.DateField()),
                ('id_project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.project')),
            ],
        ),
    ]
