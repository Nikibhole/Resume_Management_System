# Generated by Django 5.2.2 on 2025-07-07 10:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobportal', '0005_application_job'),
    ]

    operations = [
        migrations.AddField(
            model_name='application',
            name='status',
            field=models.CharField(choices=[('Pending', 'Pending'), ('Approved', 'Approved'), ('Rejected', 'Rejected')], default='Pending', max_length=10),
        ),
    ]
