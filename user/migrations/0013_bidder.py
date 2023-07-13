# Generated by Django 4.1.7 on 2023-04-14 19:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0012_seller_simg'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bidder',
            fields=[
                ('b_id', models.AutoField(primary_key=True, serialize=False)),
                ('bfn', models.CharField(max_length=50, null=True)),
                ('bem', models.CharField(max_length=50, null=True)),
                ('bph', models.CharField(max_length=50, null=True)),
                ('bbd', models.CharField(max_length=50, null=True)),
                ('bgen', models.CharField(max_length=50, null=True)),
                ('bstreet', models.CharField(max_length=250, null=True)),
                ('blnk', models.CharField(max_length=100, null=True)),
                ('bcty', models.CharField(max_length=100, null=True)),
                ('bstat', models.CharField(max_length=50, null=True)),
                ('bpin', models.CharField(max_length=20, null=True)),
                ('baadh', models.CharField(max_length=30, null=True)),
                ('bpan', models.CharField(max_length=10, null=True)),
                ('bUPI', models.CharField(max_length=35, null=True)),
                ('bbank', models.CharField(max_length=30, null=True)),
            ],
            options={
                'db_table': 'bidder',
            },
        ),
    ]