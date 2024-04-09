# Generated by Django 5.0.2 on 2024-04-09 02:38

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullName', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=255)),
                ('condition_type', models.CharField(max_length=255)),
                ('severity', models.CharField(max_length=255)),
                ('admission_date', models.DateField()),
                ('status', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Time',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestart', models.DateTimeField()),
                ('timeend', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Cleaner',
            fields=[
                ('employee_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='core.employee')),
            ],
            bases=('core.employee',),
        ),
        migrations.CreateModel(
            name='Surgeon',
            fields=[
                ('employee_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='core.employee')),
                ('qualifications', models.CharField(max_length=100)),
                ('exp', models.CharField(max_length=2)),
            ],
            bases=('core.employee',),
        ),
        migrations.CreateModel(
            name='Surgery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.patient')),
                ('time_period', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.time')),
                ('cleaners', models.ManyToManyField(to='core.cleaner')),
                ('surgeons', models.ManyToManyField(to='core.surgeon')),
            ],
        ),
        migrations.CreateModel(
            name='Schedule',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.DateTimeField()),
                ('surgeries', models.ManyToManyField(to='core.surgery')),
            ],
        ),
        migrations.AddField(
            model_name='employee',
            name='assignments',
            field=models.ManyToManyField(to='core.surgery'),
        ),
        migrations.AddField(
            model_name='employee',
            name='availability',
            field=models.ManyToManyField(related_name='available_employees', to='core.time'),
        ),
        migrations.AddField(
            model_name='employee',
            name='sched',
            field=models.ManyToManyField(related_name='scheduled_employees', to='core.time'),
        ),
    ]
