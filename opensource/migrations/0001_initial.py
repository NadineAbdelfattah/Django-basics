# Generated by Django 3.2.3 on 2021-05-15 20:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Track',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname', models.CharField(default='Ahmed', max_length=50, null=True)),
                ('lname', models.CharField(default='Ahmed', max_length=50, null=True)),
                ('age', models.IntegerField()),
                ('student_track', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='opensource.track')),
            ],
        ),
    ]
