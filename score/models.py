from django.db import models
from django.conf import settings

class Loan(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='loans')
    amount = models.DecimalField(max_digits=6, decimal_places=2)
    due_date = models.DateField(auto_now=False, auto_now_add=False)
    payment_complete = models.BooleanField(default=False)
    payment_complete_date = models.DateField(blank=True, null=True)

    def __str__(self):
        return f'Amount:{self.amount}, by:{self.user.username}, Due date:{self.due_date} fulfiled:{self.payment_complete}'
    
