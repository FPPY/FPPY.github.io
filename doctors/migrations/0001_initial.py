# Generated by Django 3.2.6 on 2021-11-14 16:23

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('First_name', models.CharField(blank=True, max_length=100, null=True)),
                ('Last_name', models.CharField(max_length=100, null=True)),
                ('phone', models.CharField(max_length=100, null=True)),
                ('email', models.CharField(max_length=200, null=True)),
                ('spec', models.CharField(max_length=100, null=True)),
                ('date_created', models.DateTimeField(default=django.utils.timezone.now)),
                ('profile_pic', models.ImageField(default='person.jpg', null=True, upload_to='')),
                ('user', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Package',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, null=True)),
                ('price', models.IntegerField(null=True)),
                ('desc', models.CharField(max_length=200, null=True)),
                ('cond', models.CharField(max_length=200, null=True)),
                ('img', models.ImageField(default='pic.jpg', null=True, upload_to='')),
                ('date_created', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('First_name', models.CharField(blank=True, max_length=100, null=True)),
                ('Last_name', models.CharField(max_length=100, null=True)),
                ('phone', models.CharField(max_length=100, null=True)),
                ('email', models.CharField(max_length=200, null=True)),
                ('date_created', models.DateTimeField(default=django.utils.timezone.now)),
                ('profile_pic', models.ImageField(default='defaultpic.jpeg', null=True, upload_to='')),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='New',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('header', models.CharField(max_length=150, null=True)),
                ('context', models.TextField()),
                ('img', models.ImageField(default='pic.jpg', null=True, upload_to='')),
                ('date_created', models.DateTimeField(default=django.utils.timezone.now)),
                ('doctor', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='doctors.doctor')),
            ],
        ),
        migrations.CreateModel(
            name='Buy',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateTimeField(default=django.utils.timezone.now)),
                ('img', models.ImageField(default='nopic.png', null=True, upload_to='')),
                ('status', models.CharField(choices=[('NOT PAID', 'NOT PAID'), ('PAID', 'PAID')], default='NOT PAID', max_length=200, null=True)),
                ('package', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='doctors.package')),
                ('patient', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='doctors.patient')),
            ],
        ),
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('header', models.CharField(max_length=150, null=True)),
                ('context', models.TextField()),
                ('img', models.ImageField(default='pic.jpg', null=True, upload_to='')),
                ('date_created', models.DateTimeField(default=django.utils.timezone.now)),
                ('doctor', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='doctors.doctor')),
            ],
        ),
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('symptom', models.CharField(max_length=100, null=True)),
                ('dateapp', models.DateField(null=True)),
                ('Doctor_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='doctors.doctor')),
                ('Patient_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='doctors.patient')),
            ],
        ),
    ]
