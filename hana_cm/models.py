from logging import PlaceHolder
from tabnanny import verbose
from tkinter import CASCADE
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django import forms



# Create your models here.
#利用者クラス
class Riyousha(models.Model):
    

    class Meta:
        verbose_name_plural = '利用者' 
        


    #基本情報
    hihoken_no = models.CharField(max_length=10,verbose_name='被保険者番号',null=True)
    name = models.CharField(max_length=50, verbose_name='氏名',null=True)
    name_kana = models.CharField(max_length=100,verbose_name='氏名カナ',null=True)
    nyuuryoku_date = models.DateField(auto_now_add=False, verbose_name='入力日',null=True)
    gender = models.ForeignKey('Gender', verbose_name='性別',  related_name = 'hana_cm.Riyousha.gender+', on_delete = models.PROTECT,null=True)
    birth_day = models.DateField(auto_now_add=False, null=True, verbose_name='生年月日')

    
    pub_date = models.DateTimeField(auto_now_add=True)
    
    

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('hana_cm:detail', kwargs={'pk': self.pk})  
 
class Gender(models.Model):
    class Meta:
        verbose_name_plural = '性別'

    gender = models.CharField(max_length=10, verbose_name ='性別')

    def __str__(self):
        return self.gender

class RiyoushaAttributes(models.Model):

    class Meta:
        verbose_name_plural = '利用者フェイスシート'

    nyuuryoku_date = models.DateField(verbose_name ='フェイスシート入力日', auto_now_add=False,null=True, blank=True)

    name = models.ForeignKey('Riyousha', related_name='riyousha_attributes', verbose_name='氏名',null=True, on_delete=models.CASCADE)    

    #住所
    post_no = models.CharField(max_length=8,verbose_name='郵便番号',null=True, blank=True)
    adress = models.CharField(max_length=100,verbose_name='住所',null=True, blank=True)

    #認定情報
    youkaigodo_nyuuryokuDate = models.DateField(auto_now_add=False,verbose_name='認定情報入力日',null=True, blank=True)
    kaigodo = models.ForeignKey('Kaigodo', on_delete=models.CASCADE,verbose_name='要介護度',related_name='Riyousha_kaigodo', db_column='kaigodo',null=True, blank=True)
    nintei_date = models.DateField(auto_now_add=False,verbose_name='認定日',null=True, blank=True)
    start_date = models.DateField(auto_now_add=False,verbose_name='認定開始日',null=True, blank=True)
    end_date = models.DateField(auto_now_add=False,verbose_name='認定終了日',null=True, blank=True) 

    #担当ケアマネ
    cm_name = models.ForeignKey('CareManager', verbose_name='担当ケアマネ', on_delete=models.CASCADE,
    related_name ='hana_cm.Riyousha.cm_name +',null=True, blank=True)

    #主訴
    shuso_honninn = models.TextField(verbose_name='主訴（本人）',null=True, blank=True)
    shuso_family = models.TextField(verbose_name='主訴（家族）',null=True, blank=True)
    family_situation = models.TextField(verbose_name='家族の状況',null=True, blank=True)

    #家族など連絡先
    family_name = models.CharField(max_length=20,verbose_name='家族氏名',blank=True,null=True)
    family_relationship = models.CharField(max_length=10,verbose_name='続柄',blank=True,null=True)
    family_phone = models.CharField(max_length=14,verbose_name='電話番号',blank=True,null=True)
    family_name2 = models.CharField(max_length=20,verbose_name='家族氏名',blank=True,null=True)
    family_relationship2 = models.CharField(max_length=10,verbose_name='続柄',blank=True,null=True)
    family_phone2 = models.CharField(max_length=14,verbose_name='電話番号',blank=True,null=True)
    family_name3 = models.CharField(max_length=20,verbose_name='家族氏名',blank=True,null=True)
    family_relationship3 = models.CharField(max_length=10,verbose_name='続柄',blank=True,null=True)
    family_phone3 = models.CharField(max_length=14,verbose_name='電話番号',blank=True,null=True)

    #日常生活自立度
    shougai_koureisha = models.ForeignKey('Shogai_Jiritudo', verbose_name='障害高齢者自立度', related_name = 'hana_cm.RiyoushaAttributes.shougai_koureisha+',on_delete=models.CASCADE,null=True, blank=True)
    ninchisho_koureisha = models.ForeignKey('Ninchisho_Jiritudo', verbose_name='認知症高齢者自立度', related_name = 'hana_cm.RiyoushaAttributes.ninchisho_jkoureisha+', on_delete=models.CASCADE,null=True, blank=True)
    #生活歴
    life_history = models.TextField(verbose_name = '生活歴',null=True, blank=True)
    disease_history = models.TextField(verbose_name = '病歴',null=True, blank=True)
    #かかりつけ病状
    desease_name = models.CharField(max_length=20,verbose_name='病名',blank=True,null=True)
    primary_care_doctor = models.CharField(max_length=10,verbose_name='主治医',blank=True,null=True)
    frequency = models.ForeignKey('FrequencyOfHospitalVisits',verbose_name='通院頻度', related_name = 'hana_cm.FrequencyOfHospitalVisits+', on_delete=models.CASCADE,null=True, blank=True)
    othe_frequency = models.CharField(max_length=20,verbose_name='その他通院頻度',blank=True,null=True)
    examination_status = models.ForeignKey('ExaminationStatus',verbose_name='診察状況', related_name = 'hana_cm.ExaminationStatus+', on_delete=models.CASCADE,null=True, blank=True)
    desease_name2 = models.CharField(max_length=20,verbose_name='病名2',blank=True,null=True)
    primary_care_doctor2 = models.CharField(max_length=10,verbose_name='主治医2',blank=True,null=True)
    frequency2 = models.ForeignKey('FrequencyOfHospitalVisits',verbose_name='通院頻度2', related_name = 'hana_cm.FrequencyOfHospitalVisits2+', on_delete=models.CASCADE,null=True, blank=True)
    othe_frequency2 = models.CharField(max_length=20,verbose_name='その他通院頻度2',blank=True,null=True)
    examination_status2 = models.ForeignKey('ExaminationStatus',verbose_name='診察状況2', related_name = 'hana_cm.ExaminationStatus2+', on_delete=models.CASCADE,null=True, blank=True)
    #診察状況
    
    
    desease_name3 = models.CharField(max_length=20,verbose_name='病名2',blank=True,null=True)
    primary_care_doctor3 = models.CharField(max_length=10,verbose_name='主治医2',blank=True,null=True)
    frequency3 = models.ForeignKey('FrequencyOfHospitalVisits',verbose_name='通院頻度3', related_name = 'hana_cm.FrequencyOfHospitalVisits3+', on_delete=models.CASCADE,null=True, blank=True)
    othe_frequency3 = models.CharField(max_length=20,verbose_name='その他通院頻度3',blank=True,null=True)
    examination_status3 = models.ForeignKey('ExaminationStatus',verbose_name='診察状況3', related_name = 'hana_cm.ExaminationStatus3+', on_delete=models.CASCADE,null=True, blank=True)

    #社会保険状況
    medical_insurance = models.ForeignKey('Medical_Insurance', verbose_name='医療保険', related_name='insurance',null=True, blank=True,on_delete=models.CASCADE )

    #年金
    pension_insurance = models.ForeignKey('Pension_Insurance', verbose_name='年金', related_name='pension_insurance',null=True, blank=True,on_delete=models.CASCADE )

    #障害手帳
    disability_notebook = models.ForeignKey('DisabilityNotebook', verbose_name='障害者手帳', related_name='insurance',null=True, blank=True,on_delete=models.CASCADE )

    #現在利用しているサービス
    current_service = models.TextField(verbose_name = '生活歴',null=True, blank=True)

    pub_datetime = models.DateTimeField(auto_now_add=True, null=True)
    pub_date = models.DateField(auto_now_add=True, null=True)
    
    def get_absolute_url(self):
        return reverse('hana_cm:attributesdetail', kwargs={'pk' : self.pk})
    
class CareManager(models.Model):

    class Meta:
        verbose_name_plural = 'ケアマネジャー'

    
    cm_name=models.CharField(max_length=50)
    pub_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.cm_name

class Kaigodo(models.Model):

    class Meta:
        verbose_name_plural = '介護度'

    kaigodo = models.CharField(max_length=4)
    pub_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.kaigodo

class Shogai_Jiritudo(models.Model):

    class Meta:
        verbose_name_plural = '障害自立度'
    shougai_koureisha = models.CharField( max_length=10, verbose_name="障害自立度")

    def __str__(self):
        return self.shougai_koureisha

class Ninchisho_Jiritudo(models.Model):

    class Meta:
        verbose_name_plural = '認知症自立度'
    ninchisho_koureisha = models.CharField( max_length=10, verbose_name="認知症自立度")

    def __str__(self):
        return self.ninchisho_koureisha

class Medical_Insurance(models.Model):
    class Meta:
        verbose_name_plural = '医療保険'
    medical_insurance = models.CharField(max_length=255, verbose_name='医療保険種別')

    def __str__(self):
        return self.medical_insurance

class Pension_Insurance(models.Model):
    class Meta:
        verbose_name_plural = '年金'
    medical_insurance = models.CharField(max_length=255, verbose_name='年金種別')

    def __str__(self):
        return self.medical_insurance

class DisabilityNotebook(models.Model):
    class Meta:
        verbose_name_plural = '障害者手帳'
    disability_notebook = models.CharField( max_length=10, verbose_name="障害障害者手帳",null=True)

    def __str__(self):
        return self.disability_notebook

class ExaminationStatus(models.Model):

    class Meta:
        verbose_name_plural = '診察状況'
    examination_status = models.CharField( max_length=10, verbose_name="診察状況",null=True)

    def __str__(self):
        return self.examination_status

class FrequencyOfHospitalVisits(models.Model):
    class Meta:
        verbose_name_plural = '通院頻度'
    frequency_of_hospital_visits = models.CharField( max_length=10, verbose_name="通院頻度",null=True)

    def __str__(self):
        return self.frequency_of_hospital_visits
    

class Adl_1(models.Model):

    class Meta:
        verbose_name_plural = 'アセスメント'
    


    IS_USED_CHOICES = (
        (False, 'なし'),
        (True, 'あり'),
    )
    riyousha = models.ForeignKey('Riyousha', verbose_name='利用者',on_delete=models.CASCADE)
    nyuuryoku_date = models.DateField(auto_now_add=False, verbose_name='入力基準日')
    non = models.BooleanField( help_text="「なし」なら、チェックしてください", verbose_name='麻痺なし')
    left_upper_limbs = models.BooleanField( choices=IS_USED_CHOICES, verbose_name='左上肢',help_text="「左上肢に麻痺」があれば、チェックしてください",null=True)
    left_lower_limbs = models.BooleanField( choices=IS_USED_CHOICES, verbose_name='左下肢',help_text="「左下肢に麻痺」があれば、チェックしてください",null=True)
    right_upper_limbs = models.BooleanField( choices=IS_USED_CHOICES, verbose_name='右上肢',help_text="「右上肢に麻痺」があれば、チェックしてください",null=True)
    right_lower_limbs = models.BooleanField( choices=IS_USED_CHOICES, verbose_name='右下肢',help_text="「右下肢に麻痺」があれば、チェックしてください",null=True)
    others = models.BooleanField( help_text="「その他」があれば、チェックしてください。詳細を「麻痺その他」に記入してください", verbose_name='その他',null=True)
    paralysis_others = models.CharField(max_length=50, verbose_name='その他詳細',null=True)
    pub_date = models.DateTimeField('date published',auto_now_add=True)

    def __str__(self):
        return self.riyousha


