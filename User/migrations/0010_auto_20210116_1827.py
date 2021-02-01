# Generated by Django 3.1.5 on 2021-01-16 18:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0009_auto_20210114_1454'),
    ]

    operations = [
        migrations.CreateModel(
            name='SubscriptionPeriods',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('subPeriod', models.IntegerField()),
                ('createDate', models.DateTimeField(auto_now_add=True)),
                ('updateDate', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='subscriptiondetail',
            name='exprirationPeriod',
        ),
        migrations.AddField(
            model_name='subscriptiontypes',
            name='subprice',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='subscriptiondetail',
            name='subPeriod',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.PROTECT, to='User.subscriptionperiods'),
            preserve_default=False,
        ),
    ]
