# Generated by Django 3.2.12 on 2022-07-16 08:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('urunler', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Kategori',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.AddField(
            model_name='urun',
            name='kategori',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='urunler.kategori'),
        ),
    ]
