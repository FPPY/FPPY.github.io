# Generated by Django 3.2.7 on 2021-11-17 14:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doctors', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='appointment',
            name='status',
            field=models.CharField(choices=[('NOT COMFIRM', 'NOT COMFIRM'), ('CONFIRM', 'COMFIRM')], default='NOT COMFIRM', max_length=200, null=True),
        ),
    ]