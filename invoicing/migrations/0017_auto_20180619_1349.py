# Generated by Django 2.0.6 on 2018-06-19 11:49

from django.db import migrations, models
import django_countries.fields
import invoicing.fields


class Migration(migrations.Migration):

    dependencies = [
        ('invoicing', '0016_update_credit_notes'),
    ]

    operations = [
        migrations.AddField(
            model_name='invoice',
            name='customer_email',
            field=models.EmailField(blank=True, max_length=254),
        ),
        migrations.AddField(
            model_name='invoice',
            name='customer_phone',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='invoice',
            name='bank_city',
            field=models.CharField(blank=True, default='', max_length=255),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='invoice',
            name='bank_country',
            field=django_countries.fields.CountryField(blank=True, default='', max_length=2),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='invoice',
            name='bank_name',
            field=models.CharField(blank=True, default='', max_length=255),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='invoice',
            name='bank_street',
            field=models.CharField(blank=True, default='', max_length=255),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='invoice',
            name='bank_zip',
            field=models.CharField(blank=True, default='', max_length=255),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='invoice',
            name='constant_symbol',
            field=models.CharField(blank=True, default='', max_length=64),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='invoice',
            name='customer_city',
            field=models.CharField(blank=True, default='', max_length=255),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='invoice',
            name='customer_registration_id',
            field=models.CharField(blank=True, default='', max_length=255),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='invoice',
            name='customer_street',
            field=models.CharField(blank=True, default='', max_length=255),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='invoice',
            name='customer_tax_id',
            field=models.CharField(blank=True, default='', max_length=255),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='invoice',
            name='customer_vat_id',
            field=invoicing.fields.VATField(blank=True, default='', max_length=13),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='invoice',
            name='customer_zip',
            field=models.CharField(blank=True, default='', max_length=255),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='invoice',
            name='delivery_method',
            field=models.CharField(default='PERSONAL_PICKUP', max_length=64),
        ),
        migrations.AlterField(
            model_name='invoice',
            name='issuer_email',
            field=models.EmailField(blank=True, default='', max_length=254),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='invoice',
            name='issuer_name',
            field=models.CharField(blank=True, default='', max_length=255),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='invoice',
            name='issuer_phone',
            field=models.CharField(blank=True, default='', max_length=255),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='invoice',
            name='note',
            field=models.CharField(blank=True, default='Thank you for using our services.', max_length=255),
        ),
        migrations.AlterField(
            model_name='invoice',
            name='reference',
            field=models.CharField(blank=True, default='', max_length=140),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='invoice',
            name='shipping_city',
            field=models.CharField(blank=True, default='', max_length=255),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='invoice',
            name='shipping_country',
            field=django_countries.fields.CountryField(blank=True, default='', max_length=2),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='invoice',
            name='shipping_name',
            field=models.CharField(blank=True, default='', max_length=255),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='invoice',
            name='shipping_street',
            field=models.CharField(blank=True, default='', max_length=255),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='invoice',
            name='shipping_zip',
            field=models.CharField(blank=True, default='', max_length=255),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='invoice',
            name='status',
            field=models.CharField(default='NEW', max_length=64),
        ),
        migrations.AlterField(
            model_name='invoice',
            name='subtitle',
            field=models.CharField(blank=True, default='', max_length=255),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='invoice',
            name='supplier_city',
            field=models.CharField(blank=True, default='', max_length=255),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='invoice',
            name='supplier_registration_id',
            field=models.CharField(blank=True, default='', max_length=255),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='invoice',
            name='supplier_street',
            field=models.CharField(blank=True, default='', max_length=255),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='invoice',
            name='supplier_tax_id',
            field=models.CharField(blank=True, default='', max_length=255),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='invoice',
            name='supplier_vat_id',
            field=invoicing.fields.VATField(blank=True, default='', max_length=13),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='invoice',
            name='supplier_zip',
            field=models.CharField(blank=True, default='', max_length=255),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='invoice',
            name='type',
            field=models.CharField(default='INVOICE', max_length=64),
        ),
        migrations.AlterField(
            model_name='item',
            name='unit',
            field=models.CharField(default='PIECES', max_length=64),
        ),
    ]
