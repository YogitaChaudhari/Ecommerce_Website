# Generated by Django 3.0.2 on 2020-02-24 04:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('itvedantapp1', '0003_auto_20200203_1304'),
    ]

    operations = [
        migrations.CreateModel(
            name='Carts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('count', models.IntegerField(default=1)),
                ('email', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='itvedantapp1.Users')),
                ('pro_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='itvedantapp1.Products')),
            ],
        ),
    ]
