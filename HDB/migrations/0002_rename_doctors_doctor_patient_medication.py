# Generated by Django 4.2.3 on 2023-07-04 14:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('HDB', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Doctors',
            new_name='Doctor',
        ),
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('card_No', models.IntegerField(verbose_name=9)),
                ('ward', models.CharField(max_length=6)),
                ('doctor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='HDB.doctor')),
            ],
        ),
        migrations.CreateModel(
            name='Medication',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('dosage', models.CharField(max_length=100)),
                ('doctor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='HDB.doctor')),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='HDB.patient')),
            ],
        ),
    ]
