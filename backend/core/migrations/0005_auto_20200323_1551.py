# Generated by Django 3.0.4 on 2020-03-23 15:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_default_interest_rate'),
    ]

    operations = [
        migrations.AddField(
            model_name='statementofaccount',
            name='trade_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.Trade'),
        ),
        migrations.DeleteModel(
            name='StatementTrade',
        ),
    ]
