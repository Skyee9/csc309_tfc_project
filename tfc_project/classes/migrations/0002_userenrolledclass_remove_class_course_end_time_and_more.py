# Generated by Django 4.1.3 on 2022-11-17 00:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('classes', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserEnrolledClass',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.PositiveIntegerField()),
                ('class_id', models.PositiveIntegerField()),
            ],
        ),
        migrations.RemoveField(
            model_name='class',
            name='course_end_time',
        ),
        migrations.RemoveField(
            model_name='class',
            name='is_cancelled',
        ),
        migrations.RemoveField(
            model_name='class',
            name='space_availability',
        ),
        migrations.AlterField(
            model_name='class',
            name='end_time',
            field=models.DateTimeField(),
        ),
        migrations.CreateModel(
            name='ClassInstance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('space_availability', models.PositiveIntegerField()),
                ('start_time', models.DateTimeField()),
                ('end_time', models.DateTimeField()),
                ('is_cancelled', models.BooleanField(default=False)),
                ('the_class', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='classes.class')),
            ],
        ),
    ]