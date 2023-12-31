# Generated by Django 4.2.6 on 2023-10-13 12:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0006_add_about_edu_model'),
    ]

    operations = [
        migrations.CreateModel(
            name='AboutExperience',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.RemoveField(
            model_name='abouteducation',
            name='description',
        ),
        migrations.AddField(
            model_name='abouteducation',
            name='field',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='abouteducation',
            name='notes',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='abouteducation',
            name='relevant_courses',
            field=models.TextField(blank=True, null=True),
        ),
    ]
