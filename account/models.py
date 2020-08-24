from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils.translation import ugettext_lazy as _

from django_countries.fields import CountryField
from django.utils import timezone


# ::::::::::::::: USER PROFILE ::::::::::::::::::
class Profile(models.Model):

    gender_CHOICES = (
        ('1', _('أنثى')),
        ('2', _('ذكر')),
        ('3', _('أفضل أن لا أحدد')),
    )

    user_CHOICES = (
        ('1', 'فرد إعلامي'),
        ('2', 'ناشط حقوقي'),
        ('3', 'مؤسسة إعلامية')
    )

    city_CHOICES = (
        ('aleppo', _('حلب')),
        ('damascus', _('دمشق')),
        ('suburb of damascus', _('ريف دمشق')),
        ('daraa', _('درعا')),
        ('deir ez-Zor', _('دير الزور')),
        ('hama', _('حماه')),
        ('al-Hasakah', _('الحسكة')),
        ('homs', _('حمص')),
        ('idlib', _('إدلب')),
        ('latakia', _('اللاذقية')),
        ('quneitra', _('القنيطرة')),
        ('raqqa', _('الرقة')),
        ('as-Suwayda', _('السويداء')),
        ('tartus', _('طرطوس')),
    )

    user = models.OneToOneField(
        User, on_delete=models.CASCADE)
    gender = models.CharField(max_length=30, choices=gender_CHOICES, null=True)
    nickname = models.CharField(
        max_length=150, null=True, blank=True, verbose_name=_('الاسم المستعار'))
    birth_date = models.DateField(verbose_name=_("تاريخ الميلاد"), null=True)
    birth_place = models.CharField(
        max_length=255, verbose_name=_("مكان الولادة"), null=True)
    phone = models.CharField(
        max_length=100, verbose_name=_('رقم الهاتف مع الرمز الدولي'))
    facebook = models.CharField(max_length=255,
                                blank=True, null=True, verbose_name=_("صفحة الفيسبوك"))
    country = CountryField(
        max_length=255, verbose_name=_('من أي دولة ؟'), null=True)
    region = models.CharField(
        max_length=100, choices=city_CHOICES, null=True, blank=True, verbose_name=_('من أي محافظة ؟'))

    current_country = CountryField(
        max_length=255, verbose_name=_('في أي دولة ؟'), null=True)
    current_region = models.CharField(
        max_length=100, choices=city_CHOICES, null=True, blank=True, verbose_name=_('في أي محافظة ؟'))

    who_are_you = models.CharField(
        max_length=100, choices=user_CHOICES, verbose_name=_("هل أنت ؟"))
    image = models.ImageField(
        default='default.jpg', upload_to='profile_pics', verbose_name=_("صورة شخصية"))

    def __str__(self):
        return f'{self.user.username} Profile'


# ::::::::::::::::::::: CREATE USER PROFILE AUTO :::::::::::::::::::::::
@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()


@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    instance.profile.save()

# //////////////////////// START FORMULA /////////////////////////


class Support_descrption(models.Model):
    suppo = models.CharField(max_length=255, null=True,
                             blank=True, verbose_name=_("اسم الجهة الداعمة"))
    suppo_description = models.CharField(
        max_length=255, null=True, blank=True, verbose_name=_("وصف حول الجهة"))

    def __str__(self):
        return self.suppo


# ::::::::::::::::::: REGISTERATION MEDIA ACTIVIST :::::::::::::::::::::::

class RegisterMediaAct(models.Model):

    education_CHOICES = (
        ('1', _('مادون الثانوي')),
        ('2', _('الثانوي')),
        ('3', _('الجامعي')),
        ('4', _('دراسات عليا')),
    )

    family_CHOICES = (
        ('single', _('أعزب / عزباء')),
        ('married', _('متزوج / متزوجة')),
        ('divorced', _('مطلق / مطلقة')),
        ('widow', _('أرمل / أرملة')),
    )

    demand_CHOICES = (
        ('1', _('مناصرة')),
        ('2', _('إيجاد فرصة عمل')),
        ('3', _('دعم قانوني')),
        ('4', _('دعم طبي')),
        ('5', _('دعم ملف اللجوء - تأشيرات خروج')),
        ('6', _('دعم الانتقال اﻵمن')),
        ('7', _('الدعم المعيشي')),
        ('8', _('الدعم التقني')),
        ('9', _('دعم بطاقات صحفية')),
        ('10', _('رسائل توصية')),
        ('11', _('خروج آمن')),
        ('12', _('غير ذلك')),
    )

    bool_CHOICES = (
        ('0', 'لا'),
        ('1', 'نعم'),
    )

    support_CHOICES = (
        ('1', _('مراسلون بلا حدود | RSF')),
        ('2', _('فري بريس أنليميتيد | FPU')),
        ('3', _('مؤسسة الإعلام النسوي الدولية | IWMF')),
        ('4', _('مؤسسة كاليتي | Kality Foundation')),
        ('5', _('لايف لاين | Lifeline')),
    )

    jobـCHOICES = (
        ('1', _('مراسل / مراسلة ')),
        ('2', _('محرر / محررة ')),
        ('3', _('مصور / مصورة ')),
        ('4', _('مراسل حربي / مراسلة حربية')),
        ('5', _('مراسل عسكري / مراسلة عسكرية')),
        ('6', _('كاتب/ة- مدير/ة مكتب إعلامي ')),
        ('7', _('رئيس تحرير / رئيسة تحرير')),
        ('8', _(' معد تقارير / معدة تقارير')),
        ('9', _(' سيناريست ')),
        ('10', _(' مدير / مديرة قسم إنتاج')),
        ('11', _('منسق إعلامي / منسقه إعلاميه')),
        ('12', _('مونيتير')),
        ('13', _('مخرج / مخرجة')),
        ('14', _('منتج / منتجة')),
        ('15', _('متحدث إعلامي /متحدثة إعلامية')),
        ('16', _('عامل / عاملة في المجال اﻹعلامي')),
        ('17', _('ناشط إعلامي / ناشطة إعلامية')),
        ('18', _('مقدم / مقدمة برامج')),
        ('19', _('مذيع / مذيعة')),
        ('20', _('فنان تشكيلي / فنانة تشكيلية')),
        ('21', _('ممثل / ممثلة')),
        ('22', _('غير ذلك')),
    )

    procesc_CHOICES = (
        ('1', _('لم يتم البدء بالمعالجة')),
        ('2', _('الخطوة الاولى')),
        ('3', _('الخطوة الثانية')),
        ('4', _('الخطوة الثالثة')),
        ('5', _('تمت المعالجة')),
        ('6', _('تحميل ملفات مرفقة')),

    )

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    profile = models.ForeignKey(Profile, default=None, on_delete=models.CASCADE)

    # :::::::::::: FALILY STATE :::::::::::
    family_state = models.CharField(
        max_length=30, choices=family_CHOICES, verbose_name=_('الوضع العائلي'))
    have_kids = models.CharField(
        max_length=50, null=True, blank=True, choices=bool_CHOICES, verbose_name=_('هل لديك أولاد ؟'))
    number_kids = models.CharField(
        max_length=50, null=True, blank=True, verbose_name=_('عدد اﻷولاد'))
    summary_family = models.TextField(
        max_length=2000, null=True, blank=True, verbose_name=_('ملخص وضعك العائلي'))

    # :::::::::::::::: MEDICAL STATE ::::::::::::::::::::
    medical_state_q = models.CharField(
        max_length=50, choices=bool_CHOICES, verbose_name=_('هل لديك وضع صحي خاص ؟'))
    medical_state_des = models.TextField(
        max_length=3000, null=True, blank=True, verbose_name=_('اشرح وضعك الصحي'))

    # ::::::::::::::::::: EDUCATIONS AND JOB STATE ::::::::::::::::::::
    education_level = models.CharField(
        max_length=100, choices=education_CHOICES, verbose_name=_('المستوى التعليمي'))
    job = models.CharField(
        max_length=150, choices=jobـCHOICES, verbose_name=_('المهنة'))

    # :::::::::::::: EXPERIENCE ::::::::::::::::
    experience = models.CharField(max_length=100, choices=bool_CHOICES, verbose_name=_(
        'هل سبق عملت بأجر أو لديك خبرات سابقة ؟'))

    # ::::::::::::::::: ARTICLES LINKES :::::::::::::::
    if_article_linke = models.CharField(max_length=100, choices=bool_CHOICES,
                                        verbose_name="هل لديك منشورة باسمك الصريح أو المستعار ؟")
    articls_link_1 = models.TextField(
        max_length=200, blank=True, null=True, verbose_name="يرجى وضع الروابط اﻹعلامية المنشورة")

    if_stop_work = models.CharField(max_length=100,
                                    choices=bool_CHOICES, verbose_name="هل انت منقطع/ة  عن العمل الاعلامي ؟")
    date_stop_work = models.DateField(
        blank=True, null=True, verbose_name="منذ متى منقطع/ة  عن العمل الاعلامي")

    summary_of_your_state = models.TextField(
        blank=True, null=True, verbose_name="اكتب ملخص عن حالتك")

    # ::::::::::::: ROSOURCE PROF WORKS ::::::::::::::
    resource_prof = models.CharField(max_length=100,
                                     choices=bool_CHOICES, verbose_name="هل لديك مصادر تثبت عملك ؟")
    recmond_1 = models.CharField(
        max_length=255, blank=True, null=True, verbose_name="مصدر1 للتثبت من عملك")
    phon_1 = models.CharField(
        max_length=255, blank=True, null=True, verbose_name="رقم هاتف للمصدر الاول ")
    email_1 = models.EmailField(
        max_length=255,  blank=True, null=True, verbose_name="بريد الكتروني للمصدر الاول")
    recmond_2 = models.CharField(
        max_length=255, blank=True, null=True, verbose_name="مصدر 2 للتثبت من عملك")
    phon_2 = models.CharField(
        max_length=255, blank=True, null=True, verbose_name="رقم هاتف للمصدر الثاني ")
    email_2 = models.EmailField(
        max_length=255, blank=True, null=True, verbose_name=_("بريد الكتروني للمصدر الثاني"))

    org_memeber = models.CharField(max_length=255, choices=bool_CHOICES,
                                   verbose_name=_("هل أنت عضو في أي تجمع إعلامي، أو من الموقعين على مواثيق شرف إعلامية أو سواه من المبادرات المشتركة"))
    details = models.TextField(
        max_length=4000, blank=True, null=True, verbose_name=_("يرجى ذكر التفاصيل"))

    # :::::::::::::: VIOLATIONS :::::::::::::
    violations = models.CharField(max_length=255,
                                  choices=bool_CHOICES, verbose_name=_("هل سبق أن تعرضت ﻷي نوع من أنواع الانتهاكات؟"))

    # ::::::::::::::: QUASTIONS :::::::::::::::::
    relation_with_org = models.CharField(max_length=100, choices=bool_CHOICES,
                                         verbose_name=_("هل لديك أي ارتباطات تنظيمية مع أي فصيل عسكري أو ديني أو تجمع سياسي أو ديني؟"))
    summary_of_relations = models.TextField(
        blank=True, null=True, verbose_name=_("الرجاء اﻹجابة مع ذكر التفاصيل"))

    # :::::::::::::::::: ASK FOR HELP ::::::::::::::::::::
    type_of_dmande = models.CharField(
        max_length=50, choices=demand_CHOICES, verbose_name=_("طبيعة المساعدة المطلوبة"))
    resaon_for_help = models.TextField(
        blank=True, null=True, verbose_name=_("رجاء اكتب ملخص لسبب طلب المساعدة"))

    list_of_tools = models.TextField(max_length=255, blank=True, null=True,
                                     verbose_name=_("إن كان الدعم المطلوب متعلق بمستلزمات خاصة بالعمل، نرجو تزويدنا بقائمة الأسعار"))
    last_job_salary = models.CharField(
        max_length=255, blank=True, null=True, verbose_name=_("يرجى ذكر آخر عمل تقاضيت منه أجر وقيمة الأجر"))
    reason_stopping_job = models.TextField(
        max_length=1500, verbose_name=_("لماذا لا تستطيع أن تعمل بأجر في الوقت الحالي؟"))
    summary_of_help = models.TextField(
        max_length=2000, verbose_name=_("يرجى شرح الوضع الحالي"))

    # :::::::::::::::::::: OTHER ORGS HELP ::::::::::::::::::::::
    other_org_demand = models.CharField(max_length=255, choices=bool_CHOICES,
                                        verbose_name=_("هل تقدمت بطلب مساعدة ﻷي منظمة سابقاً؟"))
    name_org = models.TextField(
        max_length=1500, blank=True, null=True, verbose_name=_("يرجى ذكر اسم المنظمة / المنظمات"))
    date_of_demand_org = models.DateField(
        blank=True, null=True, verbose_name=_("نرجو معرفة تاريخ تقديم الطلب ؟"))
    type_of_demand_other_org = models.TextField(
        max_length=1500, blank=True, null=True, verbose_name=_("ما هي طبيعة الطلب؟"))
    result_of_demand_other_org = models.TextField(
        max_length=1500, blank=True, null=True, verbose_name=_("ما هي نتيجة الطلب؟"))
    know_support_programme = models.TextField(
        max_length=1500, verbose_name=_("كيف علمت ببرنامج الدعم ؟"))

    # ::::::::::::::::: TRAINING ::::::::::::::::::
    training_media = models.CharField(max_length=30, choices=bool_CHOICES,
                                      verbose_name=_("هل سبق أن شاركت بأي ورشات أو دورات لتطوير الخبرات اﻹعلامية أو الحقوقية؟"))
    details_traning_media = models.TextField(
        max_length=1500, blank=True, null=True, verbose_name=_("يرجى ذكر التفاصيل"))

    state_step = models.CharField(
        _("المعالجة"), max_length=30, blank=True, default=1, choices=procesc_CHOICES, null=True)
    support_org_state_1 = models.ForeignKey(
        Support_descrption, null=True, default=1, blank=True, on_delete=models.CASCADE, verbose_name=_("الجهة المحولة"))

    created_at = models.DateTimeField(auto_now_add=True)


# ::::::::::::::::::: EXPERIENCE ::::::::::::::::::::::::
class WorkDetail(models.Model):
    bool_CHOICES = (
        ('0', 'لا'),
        ('1', 'نعم'),
    )

    registration_media_act = models.ForeignKey(
        RegisterMediaAct, null=False, related_name="registration_media_act", on_delete=models.CASCADE)
    org_name = models.CharField(
        max_length=255, null=False, verbose_name="اسم الجهة المشغلة")
    job_title = models.CharField(
        max_length=255, null=False, verbose_name="المسمى الوظيفي")
    job_location = models.CharField(
        max_length=255, null=False, verbose_name="مكان العمل")
    start_date = models.DateField(
        verbose_name='تاريخ بدء العمل', null=False)
    until_now = models.CharField(
        choices=bool_CHOICES, verbose_name="هل تعمل حتى اﻵن ؟", null=False, max_length=100)
    end_date = models.DateField(
        verbose_name="تاريخ انتهاء العمل", null=True)
    if_salary = models.CharField(
        choices=bool_CHOICES, verbose_name="هل كنت تعمل بأجر ؟", null=False, max_length=100)
    salary = models.CharField(
        max_length=255, null=True, verbose_name="اذكر آخر راتب تقاضيته من هذا العمل")

    def __str__(self):
        return self.job_title


# :::::::::::::::::: VIOLATIONS :::::::::::::::::::
class Violation(models.Model):
    violation_CHOICES = (
        ('1', _(' اعتقال')),
        ('2', _('اختطاف')),
        ('3', _('منع من العمل')),
        ('4', _('مصادرة معدات')),
        ('5', _('اعتداء بالضرب')),
        ('6', _('اصابة')),
        ('7', _('تهديد')),
        ('8', _('ابتزاز')),
        ('9', _('غير ذلك')),
    )

    responsibility_CHOICES = (
        ('1', _('القوات الحكومية')),
        ('2', _('فصائل المعارضة المسلحة')),
        ('3', _('الادارة الذاتية')),
        ('4', _('داعش')),
        ('5', _('غير ذلك'))
    )
    violation = models.ForeignKey(RegisterMediaAct, on_delete=models.CASCADE)
    violation_type = models.CharField(
        max_length=200, choices=violation_CHOICES, null=True, verbose_name='نوع الانتهاك')
    date_of_violation = models.DateField(
        verbose_name="تاريخ الانتهاك ", blank=True)
    responsibility = models.TextField(max_length=500, choices=responsibility_CHOICES,
                                      null=True, verbose_name="من هي الجهة المسؤولة عن الانتهاك؟")

# :::::::::::::::::: DOCS :::::::::::::::::::::::


class docs(models.Model):
    docs = models.ForeignKey(
        RegisterMediaAct,
        verbose_name='docs', on_delete=models.CASCADE
    )
    doc = models.FileField(
        upload_to='documents/', verbose_name='ملف'
    )

    class Meta:
        verbose_name = ' ملفات'


# evalutions model procesing steps
class Checking(models.Model):
    app_CHOICES = (
        ('0', 'نعم'),
        ('1', 'لا'),

    )

    recmond_CHOICES = (
        ('0', 'التنيجة ايجابية'),
        ('1', 'النتيجة سلبية'),

    )
    zerone_CHOICES = (
        ('0', '0'),
        ('1', '1'),

    )
    experinc_CHOICES = (
        ('0', 'أقل من عامين'),
        ('1', 'عامين إلى خمسة'),
        ('2', 'أكثر من خمسة '),

    )
    result_CHOICES = (
        ('0', 'مقبولة'),
        ('1', 'مرفوضة'),
        ('2', 'بحث عن مانحين'),

    )
    registration = models.OneToOneField(
        RegisterMediaAct, on_delete=models.CASCADE)
    date_of_updat = models.DateField(
        editable=False, null=True, blank=True, auto_now=True, verbose_name="تاريخ اخر تحديث ")
    tiitle_of_state = models.CharField(
        max_length=255, blank=True, null=True, verbose_name="عنوان الحالة")
    urg_mark = models.CharField(
        max_length=255, blank=True, null=True, verbose_name="درجة الطوارئ ")
    confirm_stat = models.CharField(
        max_length=255, blank=True, null=True, verbose_name="نوع الحالة ")
    verfication_method = models.CharField(
        max_length=255, blank=True, null=True, verbose_name="آلية التحقق ")
    total_of_note = models.CharField(
        max_length=255, blank=True, default=0, null=True, verbose_name=" مجموع النقاط")
    # first step
    family_state_1 = models.CharField(
        max_length=30, null=True, blank=True, verbose_name="الوضع العائلي")
    medical_state = models.CharField(
        max_length=30, null=True, blank=True, verbose_name="-الوضع الطبي ")
    medical_state_note = models.CharField(
        max_length=30, null=True, blank=True, verbose_name="تقيم الوضع الصحي")
    educatton_level_1 = models.CharField(
        max_length=255, blank=True, null=True, verbose_name="التحصيل العلمي")
    cruntly_adre = models.CharField(
        max_length=30, null=True, blank=True, verbose_name="	تقيم خطورة مكان الإقامة الحالي  ")
    traning_partcipate = models.CharField(
        max_length=30, null=True, blank=True, verbose_name="	المشاركة بورشات سابقة")
    member_in_journal = models.CharField(
        max_length=30, null=True, blank=True, verbose_name="هل هو عضو في مجمع صحفي")
    hase_violants = models.CharField(
        max_length=30, null=True, blank=True, default=1, verbose_name="تعرّض مُقدّم الطلب لأيّ انتهاكات ")
    is_related_with_media = models.CharField(
        max_length=255, blank=True, choices=app_CHOICES, null=True, verbose_name="هل طلب الدعم مرتبط بالعمل الصحفي")
    number_of_year_exprince = models.CharField(
        max_length=255, blank=True, null=True, choices=experinc_CHOICES, verbose_name="عدد سنوات الخبرة في العمل")
    note_of_year_experince = models.CharField(
        max_length=255, default=0, blank=True, null=True, verbose_name="تقيم عدد سنوات الخبرة في العمل")
    note_paid_job = models.CharField(
        max_length=255, blank=True, null=True, verbose_name="تقيم العمل بإجر")
    manitry_realtion = models.CharField(
        max_length=255, blank=True, null=True, choices=app_CHOICES, verbose_name="هل لديه ارتباطات عسكرية")
    note_manitry_realtion = models.CharField(
        max_length=255, blank=True, null=True, verbose_name="ملاحظة حول لارتباطات العسكرية")
    is_thier_info_correct = models.CharField(
        max_length=255, choices=app_CHOICES, blank=True, null=True, verbose_name="هل قدم معلومات صحيحة ضمن طلب الدعم ")
    # second step
    is_thier_heate_speech = models.CharField(max_length=255, choices=app_CHOICES, blank=True,
                                             null=True, verbose_name="-	هل يُحرّض على العنف والكراهية؟ أو الإرهاب أو الطائفيّة؟ ")
    is_thier_heate_speech_note = models.CharField(
        max_length=255, blank=True, null=True, verbose_name="شرح لتقيم التحريض ")
    type_heate_speech = models.CharField(max_length=255, choices=app_CHOICES, blank=True, null=True,
                                         verbose_name="هل هو خطاب تميّزي على أساس العرق أو الدين أو أو النوع الجندري أو الطائفة أو القوميّة؟ ")
    note_type_heate_speech = models.CharField(
        max_length=255, blank=True, null=True, verbose_name="هل هو خطاب تميّزي على أساس العرق أو الدين أو أو النوع الجندري أو الطائفة أو القوميّة؟ ")
    rspect_legal_coppyright = models.CharField(
        max_length=255, choices=app_CHOICES, blank=True, null=True, verbose_name="-هل يُراعي الحق في الخصوصيّة والصور؟  ")
    note_rspect_legal_coppyright = models.CharField(
        max_length=255, blank=True, null=True, verbose_name="شرح لمراعاة خصوصية الصور ")
    mark_rspect_legal_coppyright = models.CharField(
        max_length=255, blank=True, default=0, null=True, verbose_name="-تقيم الحق في الخصوصيّة والصور؟")
    rspect_coppyright = models.CharField(
        max_length=255, choices=app_CHOICES, blank=True, null=True, verbose_name="هل يُراعي حقوق الملكية الفكرية؟ ")
    note_rspect_coppyright = models.CharField(
        max_length=255, blank=True, null=True, verbose_name="شرح لاحترام حقوق النشر ")
    mark_rspect_coppyright = models.CharField(
        max_length=255, blank=True, null=True, default=0, verbose_name=" تقيم شرح لاحترام حقوق النشر  ")
    rspect_right_human = models.CharField(
        max_length=255, choices=app_CHOICES, blank=True, null=True, verbose_name="هل يُراعي شرعة حقوق الإنسان؟  ")
    note_rspect_right_human = models.CharField(
        max_length=255, blank=True, null=True, verbose_name="شرح لتقيم احترام حقوق الانسان ")
    mark_rspect_right_human = models.CharField(
        max_length=255, blank=True, null=True, default=0, verbose_name="تقيم احترام حقوق الانسان ")
    prof_media = models.CharField(max_length=255, choices=zerone_CHOICES,
                                  blank=True, null=True, verbose_name="المهنية في صياغة الاخبار")
    # third step
    first_recmond_name = models.CharField(
        max_length=255, blank=True, null=True, verbose_name="اسم المعرف الاول")
    here_speech_1 = models.CharField(
        max_length=255, choices=recmond_CHOICES, blank=True, null=True, verbose_name="شهادة المعرف")
    recmond_1att = models.CharField(
        max_length=255, blank=True, null=True, verbose_name='اثبات شهادة المعرف الأول')
    second_recmond_name = models.CharField(
        max_length=255, blank=True, null=True, verbose_name="اسم المعرف الثاني")
    here_speech_2 = models.CharField(
        max_length=255, choices=recmond_CHOICES, blank=True, null=True, verbose_name="شهادة المعرف")
    recmond_2_att = models.CharField(
        max_length=255, blank=True, null=True, verbose_name="اثبات شهادة المعرف الثاني")
    # forth step
    check_responsabl_group_opnion = models.TextField(
        max_length=255, blank=True, null=True, verbose_name="تحقق مسؤول التواصل أو المتعاونين تسجيل المعلومات الواردة حول طالب الدعم ")
    date_of_verficaton = models.DateField(
        blank=True, null=True, verbose_name="تاريخ الانتهاء من التحقق ")
    result_of_verfication = models.CharField(
        max_length=255, choices=result_CHOICES, blank=True, null=True, verbose_name="نتيجة التحقق ")
    sumary_of_study = models.TextField(
        max_length=255, blank=True, null=True, verbose_name="ملاحظات إضافية تتضمن أية ملاحظات حول الحالة ")
    # def __str__(self):
    #     return self.registration

    def save(self, *args, **kwargs):
        ''' On save, update timestamps '''
        if not self.registration:
            self.date_of_updat = timezone.now()

        return super(Checking, self).save(*args, **kwargs)
# model to add attach documents
# here is the test commite to gethub

class CaseFile(models.Model):
    # When a Case is deleted, upload models are also deleted
    case = models.ForeignKey(RegisterMediaAct, on_delete=models.CASCADE)
    file = models.FileField(upload_to='documents/', null=True, blank=True)
    descrpiton = models.CharField(
        max_length=255, null=True, verbose_name="وصف الملف المرفق ")

    def __unicode__(self):
        return self.case


class SupportOrg(models.Model):
    support_CHOICES = (
        ('0', 'مراسلون بلا حدود | RSF'),
        ('1', 'فري بريس أنليميتيد | FPU'),
        ('2', 'مؤسسة الإعلام النسوي الدولية | IWMF'),
        ('3', 'مؤسسة كاليتي | Kality Foundation'),
        ('4', 'لايف لاين | Lifeline'),



    )
    result_of_org_CHOICES = (
        ('0', 'مقبول'),
        ('1', 'مرفوض'),


    )
    support = models.OneToOneField(RegisterMediaAct, on_delete=models.CASCADE)
    date_of_response = models.DateField(
        verbose_name="تاريخ الإحالة ", null=True, blank=True)
    result_of_org = models.CharField(
        max_length=255, null=True, blank=True, choices=result_of_org_CHOICES, default=False, verbose_name="النتيجة")
    date_of_result = models.DateField(
        verbose_name="تاريخ الإحالة ", blank=True, null=True)


class SupportOrgchild(models.Model):
    support = models.ForeignKey(RegisterMediaAct, on_delete=models.CASCADE)
    support1 = models.ForeignKey(Support_descrption, null=True, blank=True,
                                 on_delete=models.CASCADE, verbose_name="الجهة الداعمة ")
    cost = models.DecimalField(max_digits=10, decimal_places=2,
                               null=True, blank=True, verbose_name="التكلفة مقدرة باليورو")
# model to add violation to the registration form or application
