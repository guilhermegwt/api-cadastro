# Generated by Django 4.1.2 on 2022-10-12 17:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('login', models.CharField(max_length=255)),
                ('senha', models.CharField(max_length=20)),
                ('dt_nascimento', models.DateField()),
            ],
        ),
    ]
