# Generated by Django 4.0.2 on 2022-05-23 01:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('property2App', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('skillName', models.CharField(max_length=45)),
                ('addedSkill', models.DateTimeField(auto_now_add=True)),
                ('updatedSkill', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]