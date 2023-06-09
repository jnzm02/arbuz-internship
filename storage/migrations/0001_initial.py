# Generated by Django 4.2 on 2023-05-21 11:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import storage.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.CharField(max_length=255)),
                ('time', models.TimeField(max_length=255)),
                ('period', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='CartCard',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.DecimalField(decimal_places=2, max_digits=5)),
                ('cart', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cart', to='storage.cart')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=255)),
                ('name', models.CharField(max_length=255)),
                ('price', models.DecimalField(decimal_places=2, max_digits=5)),
                ('count', models.IntegerField()),
                ('unit', models.CharField(max_length=255)),
                ('image', models.ImageField(null=True, upload_to=storage.models.product_image_file_path)),
            ],
        ),
        migrations.CreateModel(
            name='Storage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('storageCards', models.ManyToManyField(to='storage.cartcard')),
            ],
        ),
        migrations.CreateModel(
            name='StorageCard',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.DecimalField(decimal_places=2, max_digits=5)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='storage.product')),
                ('storage', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='storage.storage')),
            ],
        ),
        migrations.AddField(
            model_name='cartcard',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='storage.product'),
        ),
        migrations.AddField(
            model_name='cart',
            name='cartCards',
            field=models.ManyToManyField(related_name='cartCards', to='storage.cartcard'),
        ),
        migrations.AddField(
            model_name='cart',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
