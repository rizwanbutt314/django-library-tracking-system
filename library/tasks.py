from datetime import date

from celery import shared_task
from .models import Loan
from django.core.mail import send_mail
from django.conf import settings

@shared_task
def send_loan_notification(loan_id):
    try:
        loan = Loan.objects.get(id=loan_id)
        member_email = loan.member.user.email
        book_title = loan.book.title
        send_mail(
            subject='Book Loaned Successfully',
            message=f'Hello {loan.member.user.username},\n\nYou have successfully loaned "{book_title}".\nPlease return it by the due date.',
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=[member_email],
            fail_silently=False,
        )
    except Loan.DoesNotExist:
        pass

@shared_task
def check_overdue_loans():
    """
    Query all loans where is_returned is False and due_date is past.
    Send an email reminder to each member with overdue books.

    """

    past_due_loan_ids = list(Loan.objects.filter(is_returned=False, due_date__lt=date.today()).values_list("id"))

    for loan_id in past_due_loan_ids:
        send_loan_notification(loan_id)