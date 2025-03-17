# Generated by Django 4.2 on 2025-03-17 18:12
import datetime

from django.db import migrations


def set_due_date_of_loan(apps, schema_editor):
    """
        Function to set due_date for every not returned loan by 14 days.
    """

    # Get the model from apps registry (using the historical version)
    LoanModel = apps.get_model('library', 'Loan')

    all_non_returned_loans  = LoanModel.objects.filter(is_returned=False)

    for loan in all_non_returned_loans:
        next_14_days_date = loan.loan_date + datetime.timedelta(days=14)
        loan.due_date = next_14_days_date
        loan.save()


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0002_loan_due_date'),
    ]

    operations = [
        migrations.RunPython(set_due_date_of_loan),
    ]
