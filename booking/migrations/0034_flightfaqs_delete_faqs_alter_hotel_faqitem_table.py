# Generated by Django 4.2.6 on 2024-06-07 07:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0033_navbar_photo'),
    ]

    operations = [
        migrations.CreateModel(
            name='flightfaqs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=250)),
                ('answer', models.TextField()),
            ],
        ),
        migrations.DeleteModel(
            name='faqs',
        ),
        migrations.AlterModelTable(
            name='hotel_faqitem',
            table='hotel_faqitem',
        ),
    ]