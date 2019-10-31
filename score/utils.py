from django.utils import timezone
from django.db.models import F


def credit_score(user):
    '''Function that checks credit risk level for users
    this assumes that previous records of loan are stored in our database.
    this function can be modified to retrieve credit record with an API if it is available in an external resource'''

    risks = {
        'N/A': 'No credit record',
        1: 'Very High',
        2: 'High',
        3: 'Medium',
        4: 'Low',
        5: 'Very Low'
    }
    user_loans = user.loans.all()
    paid_in_due_date = user_loans.filter(
        due_date__lt=F('payment_complete_date')).count()
    out_of_due_date = user_loans.filter(
        due_date__gte=F('payment_complete_date')).count()
    overdue_loans = user_loans.filter(
        due_date__lt=timezone.now(), payment_complete=False).count()

    score = 'N/A'
    if user_loans.exists():  # if there's a record of loan ever taken

        # If he repaid all his loans on time, then his credit score should be 4
        if out_of_due_date + overdue_loans == 0:
            score = 5
        # if he has a maximum of 5 overdue loans i.e. still owing even after the agreed Repayment date, his credit score should be 1.
        elif overdue_loans >= 5:
            score = 1

        # if he has at most 2 overdue loans, his credit score should be 2
        elif overdue_loans >= 2:
            score = 2
        # If he repaid all his loans on time, then his credit score should be 4

    risk_level = risks[score]
    return score, risk_level


def creditScore(user):
    '''this is a modified function i suggested
    1. unpaid overdue loans carries the highest risk = 5
    2. loans paid outside due date = 4
    3. loans paid in due date = 3
    4. unpaid loans but not due date = 2
    5. loans paid before due date = 0 #no risk
    '''
    risks = {
        0: 'No credit record',
        5: 'Very High',
        4: 'High',
        3: 'Medium',
        2: 'Low',
        1: 'Very Low'
    }

    user_loans = user.loans.all()

    unpaid_overdue = user_loans.filter(
        due_date__lt=timezone.now(), payment_complete=False).count()
    paid_outside_due_date = user_loans.filter(due_date__lt=F(
        'payment_complete_date'), payment_complete=True).count()
    paid_in_due_date = user_loans.filter(due_date=F(
        'payment_complete_date'), payment_complete=True).count()
    paid_before_due_date = user_loans.filter(due_date__gt=F(
        'payment_complete_date'), payment_complete=True).count()
    unpaid_loans = user_loans.filter(
        due_date__lt=timezone.now(), payment_complete=False).count()

    # Multiplying the risks with the risk factors and computing the average

    try:

        risk = (unpaid_overdue * 5) + (paid_outside_due_date * 4) + (paid_in_due_date * 3) + (paid_before_due_date * 0) + \
            (unpaid_loans * 1) // (unpaid_overdue + paid_outside_due_date +
                                paid_in_due_date + paid_before_due_date + unpaid_loans)

        risk = risk//5
    except ZeroDivisionError:
        risk = 0


    return risk, risks[risk]
