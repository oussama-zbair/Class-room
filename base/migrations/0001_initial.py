# Generated by Django 3.0.3 on 2020-11-13 06:41

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
            name='Assignments',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('assignment_name', models.CharField(max_length=50)),
                ('due_date', models.DateField()),
                ('posted_date', models.DateField(auto_now_add=True)),
                ('instructions', models.TextField()),
                ('total_marks', models.IntegerField(default=100)),
            ],
        ),
        migrations.CreateModel(
            name='Classrooms',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('classroom_name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Students',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('classroom_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.Classrooms')),
                ('student_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Teachers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('classroom_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.Classrooms')),
                ('teacher_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Submissions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('submitted_date', models.DateField(auto_now_add=True)),
                ('submitted_on_time', models.BooleanField()),
                ('marks_alloted', models.IntegerField(default=0)),
                ('assignment_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.Assignments')),
                ('student_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.Students')),
            ],
        ),
        migrations.AddField(
            model_name='assignments',
            name='classroom_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.Classrooms'),
        ),
    ]
