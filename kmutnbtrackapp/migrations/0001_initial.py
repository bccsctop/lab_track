# Generated by Django 3.0.3 on 2020-06-01 08:29

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Lab',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300, null=True)),
                ('amount', models.IntegerField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_id', models.CharField(blank=True, max_length=13)),
                ('check_in_status', models.BooleanField(blank=True, default=False)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='History',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('checkin', models.DateTimeField(null=True)),
                ('checkout', models.DateTimeField(null=True)),
                ('lab', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='kmutnbtrackapp.Lab')),
                ('person', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='kmutnbtrackapp.Person')),
            ],
        ),
    ]
