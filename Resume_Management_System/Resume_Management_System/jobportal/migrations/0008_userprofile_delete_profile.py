# Generated by Django 5.2.2 on 2025-07-20 07:23

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobportal', '0007_profile'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('job_type', models.CharField(blank=True, max_length=100)),
                ('availability', models.CharField(blank=True, max_length=100)),
                ('location', models.CharField(blank=True, max_length=100)),
                ('education', models.TextField(blank=True)),
                ('summary', models.TextField(blank=True)),
                ('skills', models.TextField(blank=True)),
                ('languages', models.TextField(blank=True)),
                ('internships', models.TextField(blank=True)),
                ('accomplishments', models.TextField(blank=True)),
                ('resume', models.FileField(blank=True, null=True, upload_to='resumes/')),
                ('image', models.ImageField(default='default.jpg', upload_to='profile_pics/')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.DeleteModel(
            name='Profile',
        ),
    ]
