# Generated by Django 5.1.4 on 2024-12-28 11:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Food', '0003_alter_fooditem_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='orderitem',
            old_name='FoodItem',
            new_name='food_tem',
        ),
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('Pending', 'Pending'), ('Processing', 'Processing'), ('Completed', 'Completed'), ('Cancelled', 'Cancelled')], default='Pending', max_length=20),
        ),
    ]