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
        ('1', _('فرد إعلامي')),
        ('2', _('ناشط حقوقي')),
        ('3', _('مؤسسة إعلامية')),
    )

    city_CHOICES = (
        ('0', _(' الحسكة')),
        ('1', _(' حلب')),
        ('2', _('الرقة')),
        ('3', _('السويداء ')),
        ('4', _('ريف دمشق ')),
        ('5', _('درعا ')),
        ('6', _('دير الزور')),
        ('7', _('حماه')),
        ('8', _(' حمص ')),
        ('9', _(' إدلب ')),
        ('10', _(' اللاذقية ')),
        ('11', _('القنيطرة')),
        ('12', _('دمشق')),
        ('13', _('طرطوس')),
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

    current_area = models.CharField(
        max_length=255, null=True, blank=True, verbose_name=_('في اي منطقة ؟'))

    who_are_you = models.CharField(
        max_length=100, choices=user_CHOICES, verbose_name=_("هل أنت ؟"))
    image = models.ImageField(
        default='profile_pics/default.jpg', upload_to='profile_pics', verbose_name=_("صورة شخصية"))

    def __str__(self):
        # return f'{self.user.username, self.user.first_name} Profile'
        return '%s %s' % (self.user.first_name, self.user.last_name) + ' من ' + '%s' % (self.region)


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

    class Meta:
        verbose_name_plural = _('الجهات المحولة ')


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
        ('0', _('لا')),
        ('1', _('نعم')),
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
    )
    know_support_CHOICES = (
        ('1', _('عبر موقع الانترنت')),
        ('2', _('صفحة الفيسبوك')),
        ('3', _('تويتر')),
        ('4', _('أحد الزملاء العاملين في المركز')),
        ('5', _('منظمة داعمة')),
        ('6', _('صديق')),
        ('7', _('زميل عمل')),
        ('8', _('غير ذلك')),
    )

    # connect with user and profiele models
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    profile = models.ForeignKey(
        Profile, default=None, on_delete=models.CASCADE)
 
    # :::::::::::: FAMILY STATE :::::::::::
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
                                        verbose_name=_("هل لديك منشور باسمك الصريح أو المستعار ؟"))
    articls_link_1 = models.TextField(
        max_length=200, blank=True, null=True, verbose_name=_("يرجى وضع الروابط اﻹعلامية المنشورة"))

    if_stop_work = models.CharField(max_length=100,
                                    choices=bool_CHOICES, verbose_name=_("هل انت منقطع/ة  عن العمل الاعلامي ؟"))
    date_stop_work = models.DateField(
        blank=True, null=True, verbose_name=_("منذ متى منقطع/ة  عن العمل الاعلامي"))

    summary_of_your_state = models.TextField(
        blank=True, null=True, verbose_name=_("اكتب ملخص عن حالتك"))

    # ::::::::::::: ROSOURCE PROF WORKS ::::::::::::::
    # resource_prof = models.CharField(max_length=100,
    #                                  choices=bool_CHOICES, verbose_name="هل لديك مصادر تثبت عملك ؟")
    recmond_1 = models.CharField(
        max_length=255, blank=True, null=True, verbose_name=_("مصدر1 للتثبت من عملك"))
    phon_1 = models.CharField(
        max_length=255, blank=True, null=True, verbose_name=_("رقم هاتف للمصدر الاول "))
    email_1 = models.EmailField(
        max_length=255,  blank=True, null=True, verbose_name=_("بريد الكتروني للمصدر الاول"))
    recmond_2 = models.CharField(
        max_length=255, blank=True, null=True, verbose_name=_("مصدر 2 للتثبت من عملك"))
    phon_2 = models.CharField(
        max_length=255, blank=True, null=True, verbose_name=_("رقم هاتف للمصدر الثاني "))
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
    # last_job_salary = models.CharField(
    #     max_length=255, blank=True, null=True, verbose_name=_("يرجى ذكر آخر عمل تقاضيت منه أجر وقيمة الأجر"))
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
    know_support_programme = models.CharField(
        max_length=150, choices=know_support_CHOICES, verbose_name=_("كيف علمت ببرنامجنا للدعم ؟"))

    # ::::::::::::::::: TRAINING ::::::::::::::::::
    training_media = models.CharField(max_length=30, choices=bool_CHOICES,
                                      verbose_name=_("هل سبق أن شاركت بأي ورشات أو دورات لتطوير الخبرات اﻹعلامية أو الحقوقية؟"))
    details_traning_media = models.TextField(
        max_length=1500, blank=True, null=True, verbose_name=_("يرجى ذكر التفاصيل"))

    state_step = models.CharField(
        _("المعالجة"), max_length=30, blank=True, default=1, choices=procesc_CHOICES, null=True)
    support_org_state_1 = models.ForeignKey(
        Support_descrption, null=True, blank=True, on_delete=models.CASCADE, verbose_name=_("الجهة المحولة"))

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name_plural = _('طلبات الافراد الإعلامين')

# ::::::::::::::::::: EXPERIENCE ::::::::::::::::::::::::


class WorkDetail(models.Model):
    bool_CHOICES = (
        ('0', _('لا')),
        ('1', _('نعم')),
    )

    registration_media_act = models.ForeignKey(
        RegisterMediaAct, null=True, blank=True, related_name="registration_media_act", on_delete=models.CASCADE)
    # worker = models.ForeignKey(
    #     User, null=True, blank=True, on_delete=models.CASCADE)
    org_name = models.CharField(
        max_length=255, null=False, blank=True, verbose_name=_("اسم الجهة المشغلة"))
    job_title = models.CharField(
        max_length=255, null=False, blank=True, verbose_name=_("المسمى الوظيفي"))
    job_location = models.CharField(
        max_length=255, null=True, blank=True, verbose_name=_("مكان العمل"))
    start_date = models.DateField(
        verbose_name=_('تاريخ بدء العمل'), null=True, blank=True)
    until_now = models.CharField(
        choices=bool_CHOICES, verbose_name=_("هل تعمل حتى اﻵن ؟"), null=True, blank=True, max_length=100)
    end_date = models.DateField(
        verbose_name=_("تاريخ انتهاء العمل"), null=True, blank=True)
    if_salary = models.CharField(
        choices=bool_CHOICES, verbose_name=_("هل كنت تعمل بأجر ؟"), null=True, blank=True, max_length=100)
    salary = models.CharField(
        max_length=255, null=True, blank=True, verbose_name=_("اذكر آخر راتب تقاضيته من هذا العمل"))
    created_at = models.DateTimeField(auto_now_add=True)

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
        ('9', _('التهجير القسري')),
        ('10', _('غير ذلك')),
    )

    responsibility_CHOICES = (
        ('1', _('القوات الحكومية')),
        ('2', _('فصائل المعارضة المسلحة')),
        ('3', _('الادارة الذاتية')),
        ('4', _('داعش')),
        ('5', _('غير ذلك'))
    )

    violation = models.ForeignKey(RegisterMediaAct, on_delete=models.CASCADE)
    # victim = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    violation_type = models.CharField(
        max_length=200, choices=violation_CHOICES, null=True, blank=True, verbose_name=_('نوع الانتهاك'))
    date_of_violation = models.DateField(
        verbose_name=_("تاريخ الانتهاك "), blank=True, null=True)
    responsibility = models.TextField(max_length=500, choices=responsibility_CHOICES,
                                      null=True, blank=True, verbose_name=_("من هي الجهة المسؤولة عن الانتهاك؟"))
    date_end_violation = models.DateField(
        verbose_name=_("تاريخ انتهاء الانتهاك"), blank=True, null=True)
    vio_description = models.TextField(
        max_length=2000, null=True, blank=True, verbose_name=_('تفاصيل الانتهاك'))
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = _('الانتهاكات')
    def __str__(self):
        return self.violation_type
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
        verbose_name_plural = _('ارفاق  ملفات')


# evalutions model procesing steps
class Checking(models.Model):
    app_CHOICES = (
        ('0', _('نعم')),
        ('1', _('لا')),

    )

    recmond_CHOICES = (
        ('0', _('التنيجة ايجابية')),
        ('1', _('النتيجة سلبية')),

    )

    experinc_CHOICES = (
        ('0', _('أقل من عامين')),
        ('1', _('عامين إلى خمسة')),
        ('2', _('أكثر من خمسة ')),

    )
    result_CHOICES = (
        ('0', _('مقبولة')),
        ('1', _('مرفوضة')),
        ('2', _('بحث عن مانحين')),
        ('3', _('عدم استجابة طالب الدعم لأسئلة التحقق الإضافية ')),


    )
    close_or_open = (
        ('0', _('مفتوح ')),
        ('1', _('مغلق')),
        
    )

    registration = models.OneToOneField(
        RegisterMediaAct,related_name="registration", on_delete=models.CASCADE)
    date_of_updat = models.DateField(
        editable=False, null=True, blank=True, auto_now=True, verbose_name=_("تاريخ اخر تحديث"))
    tiitle_of_state = models.CharField(
        max_length=255, blank=True, null=True, verbose_name=_("عنوان الحالة"))
    colse_or_open=models.CharField(
        max_length=255, blank=True,choices=close_or_open, null=True,default='مفتوح ', verbose_name=_("متابعة الحالة"))
    urg_mark = models.CharField(
        max_length=255, blank=True, null=True, verbose_name=_("درجة الطوارئ"))
    confirm_stat = models.CharField(
        max_length=255, blank=True, null=True, verbose_name=_("نوع الحالة"))
    verfication_method = models.CharField(
        max_length=255, blank=True, null=True, verbose_name=_("آلية التحقق"))
    total_of_note = models.CharField(
        max_length=255, blank=True, default=0, null=True, verbose_name=_(" مجموع النقاط"))
    # first step
    family_state_1 = models.CharField(
        max_length=30, null=True, blank=True, verbose_name=_("الوضع العائلي"))
    medical_state = models.CharField(
        max_length=30, null=True, blank=True, verbose_name=_("-الوضع الطبي"))
    medical_state_note = models.CharField(
        max_length=30, null=True, blank=True, verbose_name=_("تقيم الوضع الصحي"))
    educatton_level_1 = models.CharField(
        max_length=255, blank=True, null=True, verbose_name=_("التحصيل العلمي"))
    cruntly_adre = models.CharField(
        max_length=30, null=True, blank=True, verbose_name=_("تقيم خطورة مكان الإقامة الحالي"))
    traning_partcipate = models.CharField(
        max_length=30, null=True, blank=True, verbose_name=_("المشاركة بورشات سابقة"))
    member_in_journal = models.CharField(
        max_length=30, null=True, blank=True, verbose_name=_("هل هو عضو في مجمع صحفي"))
    hase_violants = models.CharField(
        max_length=30, null=True, blank=True,  verbose_name=_("تعرّض مُقدّم الطلب لأيّ انتهاكات"))
    is_related_with_media = models.CharField(
        max_length=255, blank=True, choices=app_CHOICES, null=True, verbose_name=_("هل طلب الدعم مرتبط بالعمل الصحفي"))
    number_of_year_exprince = models.CharField(
        max_length=255, blank=True, null=True, choices=experinc_CHOICES, verbose_name=_("عدد سنوات الخبرة في العمل"))
    note_of_year_experince = models.CharField(
        max_length=255, default=0, blank=True, null=True, verbose_name=_("تقيم عدد سنوات الخبرة في العمل"))
    note_paid_job = models.CharField(
        max_length=255, blank=True, null=True, verbose_name=_("تقيم العمل بإجر"))
    manitry_realtion = models.CharField(
        max_length=255, blank=True, null=True, choices=app_CHOICES, verbose_name=_("هل لديه ارتباطات عسكرية"))
    note_manitry_realtion = models.CharField(
        max_length=255, blank=True, null=True, verbose_name=_("ملاحظة حول لارتباطات العسكرية"))
    is_thier_info_correct = models.CharField(
        max_length=255, choices=app_CHOICES, blank=True, null=True, verbose_name=_("هل قدم معلومات صحيحة ضمن طلب الدعم"))
    # second step
    is_thier_heate_speech = models.CharField(max_length=255, choices=app_CHOICES, blank=True,
                                             null=True, verbose_name=_("-	هل يُحرّض على العنف والكراهية؟ أو الإرهاب أو الطائفيّة؟"))
    is_thier_heate_speech_note = models.CharField(
        max_length=255, blank=True, null=True, verbose_name=_("شرح لتقيم التحريض "))
    type_heate_speech = models.CharField(max_length=255, choices=app_CHOICES, blank=True, null=True,
                                         verbose_name=_("هل هو خطاب تميّزي على أساس العرق أو الدين أو أو النوع الجندري أو الطائفة أو القوميّة؟"))
    note_type_heate_speech = models.CharField(
        max_length=255, blank=True, null=True, verbose_name=_("شرح الخطاب التمييزي"))
    rspect_legal_coppyright = models.CharField(
        max_length=255, choices=app_CHOICES, blank=True, null=True, verbose_name=_("-هل يُراعي الحق في الخصوصيّة والصور؟"))
    note_rspect_legal_coppyright = models.CharField(
        max_length=255, blank=True, null=True, verbose_name=_("شرح لمراعاة خصوصية الصور"))
    mark_rspect_legal_coppyright = models.CharField(
        max_length=255, blank=True, default=0, null=True, verbose_name=_("-تقيم الحق في الخصوصيّة والصور؟"))
    rspect_coppyright = models.CharField(
        max_length=255, choices=app_CHOICES, blank=True, null=True, verbose_name=_("هل يُراعي حقوق الملكية الفكرية؟"))
    note_rspect_coppyright = models.CharField(
        max_length=255, blank=True, null=True, verbose_name=_("شرح لاحترام حقوق النشر"))
    mark_rspect_coppyright = models.CharField(
        max_length=255, blank=True, null=True, default=0, verbose_name=_(" تقيم شرح لاحترام حقوق النشر"))
    rspect_right_human = models.CharField(
        max_length=255, choices=app_CHOICES, blank=True, null=True, verbose_name=_("هل يُراعي شرعة حقوق الإنسان؟"))
    note_rspect_right_human = models.CharField(
        max_length=255, blank=True, null=True, verbose_name=_("شرح لتقيم احترام حقوق الانسان"))
    mark_rspect_right_human = models.CharField(
        max_length=255, blank=True, null=True, default=0, verbose_name=_("تقيم احترام حقوق الانسان"))
    prof_media = models.CharField(max_length=255, choices=app_CHOICES,
                                  blank=True, null=True, verbose_name=_("المهنية في صياغة الاخبار"))
    # third step
    first_recmond_name = models.CharField(
        max_length=255, blank=True, null=True, verbose_name=_("اسم المعرف الاول"))
    here_speech_1 = models.CharField(
        max_length=255, choices=recmond_CHOICES, blank=True, null=True, verbose_name=_("شهادة المعرف"))
    recmond_1att = models.CharField(
        max_length=255, blank=True, null=True, verbose_name=_('اثبات شهادة المعرف الأول'))
    second_recmond_name = models.CharField(
        max_length=255, blank=True, null=True, verbose_name=_("اسم المعرف الثاني"))
    here_speech_2 = models.CharField(
        max_length=255, choices=recmond_CHOICES, blank=True, null=True, verbose_name=_("شهادة المعرف"))
    recmond_2_att = models.CharField(
        max_length=255, blank=True, null=True, verbose_name=_("اثبات شهادة المعرف الثاني"))
    # forth step
    check_responsabl_group_opnion = models.TextField(
        max_length=255, blank=True, null=True, verbose_name=_("تحقق مسؤول التواصل أو المتعاونين تسجيل المعلومات الواردة حول طالب الدعم"))
    date_of_verficaton = models.DateField(
        blank=True, null=True, verbose_name=_("تاريخ الانتهاء من التحقق"))
    result_of_verfication = models.CharField(
        max_length=255, choices=result_CHOICES, blank=True, null=True, verbose_name=_("نتيجة التحقق"))
    sumary_of_study = models.TextField(
        max_length=255, blank=True, null=True, verbose_name=_("ملاحظات إضافية تتضمن أية ملاحظات حول الحالة"))

    def __str__(self):
        return self.registration.user.username

    def save(self, *args, **kwargs):
        ''' On save, update timestamps '''
        if not self.registration:
            self.date_of_updat = timezone.now()

        return super(Checking, self).save(*args, **kwargs)
# model to add attach documents
# here is the test commite to gethub for sure

    class Meta:
        verbose_name_plural = _('التحقق')


class CaseFile(models.Model):
    # When a Case is deleted, upload models are also deleted
    case = models.ForeignKey(RegisterMediaAct, on_delete=models.CASCADE)
    file = models.FileField(upload_to='documents/', null=True, blank=True)
    descrpiton = models.CharField(
        max_length=255, null=True, verbose_name=_("وصف الملف المرفق"))

    def __str__(self):
        return self.case.user.username
    class Meta:
        verbose_name_plural = _('صندوق الوثائق')

class app_from_org(models.Model):
       first_name = models.CharField(
        max_length=150, null=True, blank=True, verbose_name=_('الاسم '))
       email = models.EmailField(
        max_length=255,  blank=True, null=True, verbose_name=_("الايميل" ))
       date_of_response = models.DateField( _("تاريخ اﻹحالة"), null=True, blank=True)
       support1 = models.ForeignKey(Support_descrption, null=True, blank=True,
                                 on_delete=models.CASCADE, verbose_name=_("الجهة المحولة")) 
       state_summary = models.TextField(
        max_length=1500, blank=True, null=True, verbose_name=_("شرح معلومات وفق الجهة المحولة"))
       scm_summary = models.TextField(
        max_length=1500, blank=True, null=True, verbose_name=_("شرح معلومات وفق الجهة المحولة"))
       def __str__(self):
            return self.first_name
       class Meta:
            verbose_name_plural = _('طلبات التحقق من الجهات الخارجية')
class CaseFile_org(models.Model):
    # When a Case is deleted, upload models are also deleted
    case_org = models.ForeignKey(app_from_org,related_name='case_org', on_delete=models.CASCADE)
    file = models.FileField(upload_to='documents/', null=True, blank=True)
    descrpiton = models.CharField(
        max_length=255, null=True, verbose_name=_("وصف الملف المرفق"))

    def __str__(self):
        return self.case_org.first_name
    class Meta:
        verbose_name_plural = _('صندوق الوثائق')

class SupportOrgchild(models.Model):
    result_of_org_CHOICES = (
        ('0', _('مقبول')),
        ('1', _('مرفوض')),
        ('2', _('قيد الدراسة ')),
    )
    supportOrgchild = models.ForeignKey(RegisterMediaAct, related_name="supportOrgchild", on_delete=models.CASCADE)
    date_of_response = models.DateField(
        _("تاريخ اﻹحالة"), null=True, blank=True)
    #supoo = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    support1 = models.ForeignKey(Support_descrption, null=True, blank=True,
                                 on_delete=models.CASCADE, verbose_name=_("الجهة الداعمة"))
    result_of_org = models.CharField(max_length=255, null=True, blank=True,
                                     choices=result_of_org_CHOICES, default=False, verbose_name=_("التنيجة من الجهة المانحة"))
    cost = models.DecimalField(max_digits=10, decimal_places=2,
                               null=True, blank=True, verbose_name=_("التكلفة مقدرة باليورو"))
    date_of_result = models.DateField(verbose_name=_(
        " تاريخ الاستجابة "), blank=True, null=True)
    note = models.CharField(max_length=300, null=True,
                            blank=True,  verbose_name=_("ملاحظات"))
    class Meta:
        verbose_name_plural = _('الاستجابة والجهات الداعمة')
   
