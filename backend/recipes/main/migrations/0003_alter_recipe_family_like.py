# Generated by Django 4.2 on 2023-05-10 12:12

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_recipe_family'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='family',
            field=models.CharField(choices=[('Lager', 'Lager'), ('Pilsner', 'Pilsner'), ('Wheat Beer', 'Wheat Beer'), ('Pale Ale', 'Pale Ale'), ('IPA', 'IPA'), ('Stout', 'Stout'), ('Porter', 'Porter'), ('Belgian Ale', 'Belgian Ale'), ('Amber Ale', 'Amber Ale'), ('Brown Ale', 'Brown Ale'), ('Bock', 'Bock'), ('Kolsch', 'Kolsch'), ('Saison', 'Saison'), ('Gose', 'Gose'), ('Lambic', 'Lambic'), ('Sour Ale', 'Sour Ale'), ('Other', 'Other')], default='Lager', max_length=20),
        ),
        migrations.CreateModel(
            name='Like',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('recipe', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.recipe')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
