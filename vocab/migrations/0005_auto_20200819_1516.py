# Generated by Django 3.1 on 2020-08-19 15:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('vocab', '0004_example'),
    ]

    operations = [
        migrations.AlterField(
            model_name='example',
            name='text',
            field=models.CharField(max_length=2048),
        ),
        migrations.CreateModel(
            name='Definition',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=2048)),
                ('word', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vocab.word')),
            ],
        ),
    ]
