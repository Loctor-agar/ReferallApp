from datetime import datetime, date

from django.db import models


# Create your models here.


class Subscriber(models.Model):
    phone = models.CharField(max_length=15)
    active = models.BooleanField(default=True)
    add_date = models.DateTimeField(default=date.today())
    edit_date = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Subscriber'
        verbose_name_plural = 'Subscribers'

    def __str__(self):
        return self.phone


class Invite(models.Model):
    sender_subs_id = models.ForeignKey(Subscriber,
                                       on_delete=models.CASCADE,
                                       related_name='sender',
                                       verbose_name='Sender')
    receiver_subs_id = models.ForeignKey(Subscriber,
                                         on_delete=models.CASCADE,
                                         related_name='receiver',
                                         verbose_name='Receiver')
    status = models.BooleanField(default="Active")
    start_date = models.DateTimeField(auto_now_add=True)
    end_date = models.DateTimeField(default=datetime(year=2999, month=12, day=31))

    def __str__(self):
        return f'From {self.sender_subs_id} to {self.receiver_subs_id}'
