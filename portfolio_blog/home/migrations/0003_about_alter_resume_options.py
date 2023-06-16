# Generated by Django 4.2.2 on 2023-06-16 14:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_resume'),
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('greet', models.TextField()),
                ('desc', models.TextField()),
                ('photo', models.ImageField(upload_to='about/', verbose_name='photo (better pick square-sized like 768x768):')),
            ],
            options={
                'verbose_name': 'About',
            },
        ),
        migrations.AlterModelOptions(
            name='resume',
            options={'verbose_name': 'Resume'},
        ),
    ]
