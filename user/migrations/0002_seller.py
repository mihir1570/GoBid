# Generated by Django 4.1.7 on 2023-04-14 12:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Seller',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sc', models.CharField(max_length=50, null=True)),
                ('ain', models.CharField(max_length=100, null=True)),
                ('aip', models.IntegerField(max_length=50, null=True)),
                ('aid', models.CharField(max_length=250, null=True)),
                ('st', models.CharField(max_length=250, null=True)),
                ('et', models.CharField(max_length=250, null=True)),
                ('fn', models.CharField(max_length=50, null=True)),
                ('em', models.CharField(max_length=50, null=True)),
                ('ph', models.IntegerField(max_length=10, null=True)),
                ('bd', models.CharField(max_length=50, null=True)),
                ('gen', models.CharField(max_length=50, null=True)),
                ('street', models.CharField(max_length=250, null=True)),
                ('lnk', models.CharField(max_length=100, null=True)),
                ('cty', models.CharField(max_length=100, null=True)),
                ('stat', models.CharField(max_length=50, null=True)),
                ('pin', models.IntegerField(max_length=6, null=True)),
                ('aadh', models.IntegerField(max_length=12, null=True)),
                ('pan', models.CharField(max_length=10, null=True)),
                ('UPI', models.CharField(max_length=35, null=True)),
                ('bank', models.IntegerField(max_length=20, null=True)),
                ('POA', models.IntegerField(max_length=25, null=True)),
            ],
            options={
                'db_table': 'seller',
            },
        ),
    ]
