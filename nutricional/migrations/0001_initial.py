# Generated by Django 4.0.4 on 2022-05-04 21:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Nutricional',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('valorEnergetico', models.DecimalField(decimal_places=1, max_digits=4)),
                ('carboidratos', models.DecimalField(decimal_places=1, max_digits=4)),
                ('gordurasTotais', models.DecimalField(decimal_places=1, max_digits=4)),
                ('gordurasSaturadas', models.DecimalField(decimal_places=1, max_digits=4)),
                ('gordurasTrans', models.DecimalField(decimal_places=1, max_digits=4)),
                ('fibraAlimentar', models.DecimalField(decimal_places=1, max_digits=4)),
                ('sodio', models.DecimalField(decimal_places=1, max_digits=4)),
            ],
        ),
    ]
