# Generated by Django 4.2 on 2023-05-25 12:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_stockextra_cost_stockhop_cost_stockmalt_cost_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='alcool',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='cost',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='ebc',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='ibu',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='stockextra',
            name='quantity',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
        migrations.AlterField(
            model_name='stockhop',
            name='quantity',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
        migrations.AlterField(
            model_name='stockmalt',
            name='quantity',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
    ]
