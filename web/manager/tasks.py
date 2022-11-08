from datetime import datetime, timedelta

from django.contrib.auth.models import User
from django.core.mail import send_mail
from cost_manager.celery import app
from manager.models import Transaction


@app.task
def mass_send_mail():
    for user in User.objects.all():
        recipient=[]
        recipient.append(user.email)
        query = Transaction.objects.filter(user=user.id).values()
        for data in query:
            amount=data['amount']
            time=data['time'].time()
            today = datetime.today()
            yesterday = today - timedelta(days=1)
        message = 'Платежи за {0} \n Время - {1}    Сумма - {2}'.format(datetime.strftime(yesterday,'%d-%m-%Y'),time,amount)
        subject = "Рассылка статистики"
        from_email = "DjangoMarket@yandex.by"
        send_mail(subject,
                  message,
                  from_email,
                  recipient,
                  fail_silently=False)
    return f"sending emails"



