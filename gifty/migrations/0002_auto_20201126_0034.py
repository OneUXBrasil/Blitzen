# Generated by Django 2.2.10 on 2020-11-26 00:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gifty', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='ong',
            name='cnas',
            field=models.CharField(default=None, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='ong',
            name='federal_public_utility_certificate',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='gifty.FederalPublicUtilityCertificate'),
        ),
        migrations.AddField(
            model_name='ong',
            name='municipal_public_utility_certificate',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='gifty.MunicipalPublicUtilityCertificate'),
        ),
        migrations.AddField(
            model_name='ong',
            name='state_public_utility_certificate',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='gifty.StatePublicUtilityCertificate'),
        ),
    ]