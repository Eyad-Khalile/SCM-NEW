from django.core.management.base import BaseCommand
from account.models import RegisterMediaAct
from datetime import date,datetime, timedelta
from django.db.models import Q
from django.core.mail import EmailMessage

def update_blog():
    #l=RegisterMediaAct.objects.all()
    remainder_list=RegisterMediaAct.objects.filter(Q(created_at__date=datetime.now().date()-timedelta(days=2))& Q(medical_state_q= 0))
    l=[]
    for elm in remainder_list:
        l.append(elm.user.first_name +' '+ elm.user.last_name + '  has this mail  ' + elm.user.email)
    print(l)
    mail_subject = 'warning'
    message ='''                                                                        مرحبا عزيزي 
                    نرفق لك في هذا التننيه قائمة بالطلبات التي مضى عليها خمسةعشر يوم ولم تعالج        
                %s, ''' % (l)
    to_email = 'jh.programmer@scm.bz'
    email = EmailMessage( mail_subject, message, to=[to_email] )
    email.send()
class Command(BaseCommand):
    def handle(self, **options):
        update_blog()