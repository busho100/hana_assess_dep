from sqlite3 import Date
from django import forms
from .models import Riyousha,RiyoushaAttributes,DisabilityNotebook,RiyoushaAssessment,CareManager
 
class FindForm(forms.Form):
    find = forms.CharField(max_length=255, label='利用者名',required=False,\
        widget=forms.TextInput(attrs = {'class':'form-controle'})) 

class CreateForm(forms.ModelForm):
    
    class Meta:
        model = Riyousha


        def __init__(self, hana_cm = None, *args, **kwargs): 
            self.hana_cm = hana_cm
            super().__init__(*args, **kwargs) 

        fields = ('hihoken_no','name','name_kana','nyuuryoku_date','gender','birth_day')
        labels = {
            'hihoken_no':'被保険者番号',
            'name':'氏名',
            'name_kana':'氏名カナ',
            'nyuuryoku_date':'入力日',
            'gender':'性別',
            'birth_day':'生年月日',
        }    
        
        
    hihoken_no = forms.CharField(label='被保険者番号', max_length=10,
                widget=forms.TextInput(attrs={'placeholder':'半角で入力してください','class':'class_name'}))
    name = forms.CharField(label = '氏名', max_length=50,
                widget=forms.TextInput(attrs={'placeholder':'花みずき　太郎','class':'class_name'}))
    name_kana = forms.CharField(label = '氏名カナ', max_length=50,
                widget=forms.TextInput(attrs={'placeholder':'ハナミズキ　タロウ','class':'class_name'}))

    nyuuryoku_date = forms.DateField(label = '入力日',
                widget=forms.DateInput(attrs={'placeholder':'YYYY-MM-DD','class':'class_name'}))
    
    birth_day = forms.DateField(label = '生年月日',
                widget=forms.DateInput(attrs={'placeholder':'YYYY-MM-DD','class':'class_name'}))

  
class UpdateForm(forms.ModelForm):
    
    class Meta:
        model = Riyousha
        
        fields = ('hihoken_no','name','name_kana','nyuuryoku_date','gender','birth_day')
        labels = {
            'hihoken_no':'被保険者番号',
            'name':'氏名',
            'name_kana':'氏名カナ',
            'nyuuryoku_date':'入力日',
            'gender':'性別',
            'birth_day':'生年月日',
        }     

class RiyoushaAttributesCreateForm(forms.ModelForm): 
    class Meta:
        model = RiyoushaAttributes 
        def __init__(self, hana_cm = None,*args, **kwargs):
            self.hana_cm = hana_cm
            super().__init__(*args, **kwargs)

            for field in self.Meta.required:
                self.fields[field].required = False

        fields = '__all__'
        required = ('kaigodo','cm_name','shougai_koureisha','ninchisho_koureisha','medical_insurance',
            'pension_insurance','frequency','frequency2','frequency3','disability_notebook',
            'nyuuryoku_date','post_no','adress','youkaigodo_nyuuryokuDate','nintei_date',
            'start_date','end_date','examination_status','examination_status2','examination_status3',)  
        labels = {
          'name':'氏名',
          'kaigodo':'介護度',
          'cm_name':'ケアマネジャー',
          'ninchisho_koureisha':'認知症高齢者自立度',
          'shougai_koureisha':'障害高齢者自立度',
          'medical_insurance' : '医療保険',
          'pension_insurance':'年金',
          'frequency':'通院頻度',
          'frequency2':'通院頻度２',
          'frequency3':'通院頻度３',
          'disability_notebook':'障害者手帳',
          'nyuuryoku_date':'入力日',
          'examination_status':'診察状況',
          'examination_status2':'診察状況２',
          'examination_status3':'診察状況３',
        } 

    nyuuryoku_date = forms.DateField(label = '入力日',required=False,
                widget=forms.DateInput(attrs={'placeholder':'YYYY-MM-DD','class':'class_name'}))

    post_no = forms.CharField(label = '郵便番号', max_length=8,required=False,
                widget=forms.TextInput(attrs={'placeholder':'〇〇〇ー△△△△','class':'class_name'}))

    adress = forms.CharField(label = '住所', max_length=100,required=False,
                widget=forms.Textarea(attrs={'rows':3, 'cols':50, 'placeholder':'被保険者証記載の住所','class':'class_name'})) 

    youkaigodo_nyuuryokuDate = forms.DateField(label = '認定情報入力日',required=False,
                widget=forms.DateInput(attrs={'placeholder':'YYYY-MM-DD','class':'class_name'}))

    nintei_date = forms.DateField(label = '認定日',required=False,
                widget=forms.DateInput(attrs={'placeholder':'YYYY-MM-DD','class':'class_name'}))

    start_date = forms.DateField(label = '認定開始日',required=False,
                widget=forms.DateInput(attrs={'placeholder':'YYYY-MM-DD','class':'class_name'}))

    end_date = forms.DateField(label = '認定終了日',required=False,
                widget=forms.DateInput(attrs={'placeholder':'YYYY-MM-DD','class':'class_name'}))

    
    huso_honninn = forms.CharField(label = '主訴（本人)',required=False, max_length=255,widget=forms.Textarea(attrs={'rows':5, 'cols':80, 'placeholder':'ご本人の主訴','class':'class_name'}))

    shuso_family = forms.CharField(label = '主訴（家族)',required=False, max_length=255,widget=forms.Textarea(attrs={'rows':5, 'cols':80, 'placeholder':'ご家族の主訴','class':'class_name'}))
    
    family_situation = forms.CharField(label = '家族状況',required=False, max_length=255,widget=forms.Textarea(attrs={'rows':5, 'cols':80, 'placeholder':'ご家族の状況','class':'class_name'}))
    
    family_name = forms.CharField(label = '家族氏名', max_length=20,required=False,widget=forms.Textarea(attrs={'rows':1, 'cols':20,'placeholder':'本庄　花子','class':'class_name',}))
    family_relationship = forms.CharField(label = '続柄', max_length=10,required=False,widget=forms.Textarea(attrs={'rows':1, 'cols':10,'placeholder':'長男の妻','class':'class_name'}))
    family_phone = forms.CharField(label = '電話番号', max_length=14,required=False,widget=forms.Textarea(attrs={'rows':1, 'cols':14,'placeholder':'例）〇〇〇-◎◎◎◎-△△△△','class':'class_name'}))
    family_name2 = forms.CharField(label = '家族氏名2', max_length=20,required=False,widget=forms.Textarea(attrs={'rows':1, 'cols':20,'placeholder':'本庄　花子','class':'class_name',}))
    family_relationship2 = forms.CharField(label = '続柄2', max_length=10,required=False,widget=forms.Textarea(attrs={'rows':1, 'cols':10,'placeholder':'長男の妻','class':'class_name'}))
    family_phone2 = forms.CharField(label = '電話番号2', max_length=14,required=False,widget=forms.Textarea(attrs={'rows':1, 'cols':14,'placeholder':'例）〇〇〇-◎◎◎◎-△△△△','class':'class_name'}))  
    family_name3 = forms.CharField(label = '家族氏名3', max_length=20,required=False,widget=forms.Textarea(attrs={'rows':1, 'cols':20,'placeholder':'本庄　花子','class':'class_name',}))
    family_relationship3 = forms.CharField(label = '続柄3', max_length=10,required=False,widget=forms.Textarea(attrs={'rows':1, 'cols':10,'placeholder':'長男の妻','class':'class_name'}))
    family_phone3 = forms.CharField(label = '電話番号3', max_length=14,required=False,widget=forms.Textarea(attrs={'rows':1, 'cols':14,'placeholder':'例）〇〇〇-◎◎◎◎-△△△△','class':'class_name'}))  
    
    life_history = forms.CharField(label='生活歴', max_length=510,required=False,widget=forms.Textarea(attrs={'rows':5, 'cols':80, 'placeholder':'主な生活歴','class':'class_name'})) 
    disease_history= forms.CharField(label='病歴', max_length=510,required=False,widget=forms.Textarea(attrs={'rows':5, 'cols':80, 'placeholder':'主な病歴','class':'class_name'}))
    
    desease_name = forms.CharField(label = '病名', max_length=20,required=False,widget=forms.Textarea(attrs={'rows':1, 'cols':20,'placeholder':'高血圧症','class':'class_name',}))
    primary_care_doctor = forms.CharField(label = '主治医', max_length=20,required=False,widget=forms.Textarea(attrs={'rows':1, 'cols':10,'placeholder':'本庄医院','class':'class_name'}))
    othe_frequency = forms.CharField(label = 'その他通院頻度', max_length=20,required=False,widget=forms.Textarea(attrs={'rows':1, 'cols':20,'placeholder':'半年に1回等','class':'class_name',}))
    desease_name2 = forms.CharField(label = '病名２', max_length=20,required=False,widget=forms.Textarea(attrs={'rows':1, 'cols':20,'placeholder':'糖尿病','class':'class_name',}))
    primary_care_doctor2 = forms.CharField(label = '主治医２', max_length=20,required=False,widget=forms.Textarea(attrs={'rows':1, 'cols':10,'placeholder':'巨勢病院','class':'class_name'})) 
    othe_frequency2 = forms.CharField(label = 'その他通院頻度２', max_length=20,required=False,widget=forms.Textarea(attrs={'rows':1, 'cols':20,'placeholder':'半年に1回等','class':'class_name',}))
    desease_name3 = forms.CharField(label = '病名３', max_length=20,required=False,widget=forms.Textarea(attrs={'rows':1, 'cols':20,'placeholder':'アルツハイマー型認知症','class':'class_name',}))
    primary_care_doctor3 = forms.CharField(label = '主治医３', max_length=20,required=False,widget=forms.Textarea(attrs={'rows':1, 'cols':10,'placeholder':'佐賀総合病院','class':'class_name'}))   
    othe_frequency3 = forms.CharField(label = 'その他通院頻度３', max_length=20,required=False,widget=forms.Textarea(attrs={'rows':1, 'cols':20,'placeholder':'半年に1回等','class':'class_name',}))
    
    current_service = forms.CharField(label='現在利用しているサービス', max_length=510,required=False,widget=forms.Textarea(attrs={'rows':5, 'cols':80, 'placeholder':'デイサービス：週3回','class':'class_name'})) 

class RiyoushaAttributesUpdateForm(forms.ModelForm):
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field in self.Meta.required:
            self.fields[field].required = False

    class Meta:
        model = RiyoushaAttributes 

        fields = '__all__'
        required = ('kaigodo','cm_name','shougai_koureisha','ninchisho_koureisha','medical_insurance',
            'pension_insurance','frequency','frequency2','frequency3','disability_notebook',
            'examination_status','examination_status2','examination_status3',)    
        labels = {
          'name':'氏名',
          'kaigodo':'介護度',
          'cm_name':'ケアマネジャー',
          'ninchisho_koureisha':'認知症高齢者自立度',
          'shougai_koureisha':'障害高齢者自立度',
          'medical_insurance' : '医療保険',
          'pension_insurance':'年金',
          'frequency':'通院頻度',
          'frequency2':'通院頻度２',
          'frequency3':'通院頻度３',
          'disability_notebook':'障害者手帳',
          'examination_status':'診察状況',
          'examination_status2':'診察状況２',
          'examination_status3':'診察状況３',
        } 


    nyuuryoku_date = forms.DateField(label = '入力日',required=False,
                widget=forms.DateInput(attrs={'placeholder':'YYYY-MM-DD','class':'class_name'}))

    post_no = forms.CharField(label = '郵便番号', max_length=8,required=False,
                widget=forms.TextInput(attrs={'placeholder':'〇〇〇ー△△△△','class':'class_name'}))

    adress = forms.CharField(label = '住所', max_length=100,required=False,
                widget=forms.Textarea(attrs={'rows':3, 'cols':50, 'placeholder':'被保険者証記載の住所','class':'class_name'})) 

    youkaigodo_nyuuryokuDate = forms.DateField(label = '認定情報入力日',required=False,
                widget=forms.DateInput(attrs={'placeholder':'YYYY-MM-DD','class':'class_name'}))

    nintei_date = forms.DateField(label = '認定日',required=False,
                widget=forms.DateInput(attrs={'placeholder':'YYYY-MM-DD','class':'class_name'}))

    start_date = forms.DateField(label = '認定開始日',required=False,
                widget=forms.DateInput(attrs={'placeholder':'YYYY-MM-DD','class':'class_name'}))

    end_date = forms.DateField(label = '認定終了日',required=False,
                widget=forms.DateInput(attrs={'placeholder':'YYYY-MM-DD','class':'class_name'}))

    
    huso_honninn = forms.CharField(label = '主訴（本人)',required=False, max_length=255,widget=forms.Textarea(attrs={'rows':5, 'cols':80, 'placeholder':'ご本人の主訴','class':'class_name'}))

    shuso_family = forms.CharField(label = '主訴（家族)',required=False, max_length=255,widget=forms.Textarea(attrs={'rows':5, 'cols':80, 'placeholder':'ご家族の主訴','class':'class_name'}))
    
    family_situation = forms.CharField(label = '家族状況',required=False, max_length=255,widget=forms.Textarea(attrs={'rows':5, 'cols':80, 'placeholder':'ご家族の状況','class':'class_name'}))
    
    family_name = forms.CharField(label = '家族氏名', max_length=20,required=False,widget=forms.Textarea(attrs={'rows':1, 'cols':20,'placeholder':'本庄　太郎','class':'class_name',}))
    family_relationship = forms.CharField(label = '続柄', max_length=10,required=False,widget=forms.Textarea(attrs={'rows':1, 'cols':10,'placeholder':'長男','class':'class_name'}))
    family_phone = forms.CharField(label = '電話番号', max_length=14,required=False,widget=forms.Textarea(attrs={'rows':1, 'cols':14,'placeholder':'例）〇〇〇-◎◎◎◎-△△△△','class':'class_name'}))
    family_name2 = forms.CharField(label = '家族氏名2', max_length=20,required=False,widget=forms.Textarea(attrs={'rows':1, 'cols':20,'placeholder':'本庄　花子','class':'class_name',}))
    family_relationship2 = forms.CharField(label = '続柄2', max_length=10,required=False,widget=forms.Textarea(attrs={'rows':1, 'cols':10,'placeholder':'長男の妻','class':'class_name'}))
    family_phone2 = forms.CharField(label = '電話番号2', max_length=14,required=False,widget=forms.Textarea(attrs={'rows':1, 'cols':14,'placeholder':'例）〇〇〇-◎◎◎◎-△△△△','class':'class_name'}))  
    family_name3 = forms.CharField(label = '家族氏名3', max_length=20,required=False,widget=forms.Textarea(attrs={'rows':1, 'cols':20,'placeholder':'本庄　梅子','class':'class_name',}))
    family_relationship3 = forms.CharField(label = '続柄3', max_length=10,required=False,widget=forms.Textarea(attrs={'rows':1, 'cols':10,'placeholder':'長女','class':'class_name'}))
    family_phone3 = forms.CharField(label = '電話番号3', max_length=14,required=False,widget=forms.Textarea(attrs={'rows':1, 'cols':14,'placeholder':'例）〇〇〇-◎◎◎◎-△△△△','class':'class_name'}))  
    
    desease_name = forms.CharField(label = '病名', max_length=20,required=False,widget=forms.Textarea(attrs={'rows':1, 'cols':20,'placeholder':'高血圧症','class':'class_name',}))
    primary_care_doctor = forms.CharField(label = '主治医', max_length=20,required=False,widget=forms.Textarea(attrs={'rows':1, 'cols':10,'placeholder':'本庄医院','class':'class_name'}))
    othe_frequency = forms.CharField(label = 'その他通院頻度', max_length=20,required=False,widget=forms.Textarea(attrs={'rows':1, 'cols':20,'placeholder':'半年に1回等','class':'class_name',}))
    desease_name2 = forms.CharField(label = '病名２', max_length=20,required=False,widget=forms.Textarea(attrs={'rows':1, 'cols':20,'placeholder':'糖尿病','class':'class_name',}))
    primary_care_doctor2 = forms.CharField(label = '主治医２', max_length=20,required=False,widget=forms.Textarea(attrs={'rows':1, 'cols':10,'placeholder':'巨勢病院','class':'class_name'})) 
    othe_frequency2 = forms.CharField(label = 'その他通院頻度２', max_length=20,required=False,widget=forms.Textarea(attrs={'rows':1, 'cols':20,'placeholder':'半年に1回等','class':'class_name',}))
    desease_name3 = forms.CharField(label = '病名３', max_length=20,required=False,widget=forms.Textarea(attrs={'rows':1, 'cols':20,'placeholder':'アルツハイマー型認知症','class':'class_name',}))
    primary_care_doctor3 = forms.CharField(label = '主治医３', max_length=20,required=False,widget=forms.Textarea(attrs={'rows':1, 'cols':10,'placeholder':'佐賀総合病院','class':'class_name'}))   
    othe_frequency3 = forms.CharField(label = 'その他通院頻度３', max_length=20,required=False,widget=forms.Textarea(attrs={'rows':1, 'cols':20,'placeholder':'半年に1回等','class':'class_name',}))
    
    life_history = forms.CharField(label='生活歴', max_length=510,required=False,widget=forms.Textarea(attrs={'rows':5, 'cols':80, 'placeholder':'主な生活歴','class':'class_name'})) 
    disease_history= forms.CharField(label='病歴', max_length=510,required=False,widget=forms.Textarea(attrs={'rows':5, 'cols':80, 'placeholder':'主な病歴','class':'class_name'}))  

    current_service = forms.CharField(label='現在利用しているサービス', max_length=510,required=False,widget=forms.Textarea(attrs={'rows':5, 'cols':80, 'placeholder':'デイサービス：週3回','class':'class_name'})) 

    # id = forms.IntegerField(label = 'ID')     


class RiyoushaAttributesOverwriteForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field in self.Meta.required:
            self.fields[field].required = False

    class Meta:
        model = RiyoushaAttributes 

        fields = '__all__'
        required = ('kaigodo','cm_name','shougai_koureisha','ninchisho_koureisha','medical_insurance',
            'pension_insurance','frequency','frequency2','frequency3','disability_notebook',
            'examination_status','examination_status2','examination_status3',)    
        labels = {
          'name':'氏名',
          'kaigodo':'介護度',
          'cm_name':'ケアマネジャー',
          'ninchisho_koureisha':'認知症高齢者自立度',
          'shougai_koureisha':'障害高齢者自立度',
          'medical_insurance' : '医療保険',
          'pension_insurance':'年金',
          'frequency':'通院頻度',
          'frequency2':'通院頻度２',
          'frequency3':'通院頻度３',
          'disability_notebook':'障害者手帳',
          'examination_status':'診察状況',
          'examination_status2':'診察状況２',
          'examination_status3':'診察状況３',
        } 


    nyuuryoku_date = forms.DateField(label = '入力日',required=False,
                widget=forms.DateInput(attrs={'placeholder':'YYYY-MM-DD','class':'class_name'}))

    post_no = forms.CharField(label = '郵便番号', max_length=8,required=False,
                widget=forms.TextInput(attrs={'placeholder':'〇〇〇ー△△△△','class':'class_name'}))

    adress = forms.CharField(label = '住所', max_length=100,required=False,
                widget=forms.Textarea(attrs={'rows':3, 'cols':50, 'placeholder':'被保険者証記載の住所','class':'class_name'})) 

    youkaigodo_nyuuryokuDate = forms.DateField(label = '認定情報入力日',required=False,
                widget=forms.DateInput(attrs={'placeholder':'YYYY-MM-DD','class':'class_name'}))

    nintei_date = forms.DateField(label = '認定日',required=False,
                widget=forms.DateInput(attrs={'placeholder':'YYYY-MM-DD','class':'class_name'}))

    start_date = forms.DateField(label = '認定開始日',required=False,
                widget=forms.DateInput(attrs={'placeholder':'YYYY-MM-DD','class':'class_name'}))

    end_date = forms.DateField(label = '認定終了日',required=False,
                widget=forms.DateInput(attrs={'placeholder':'YYYY-MM-DD','class':'class_name'}))

    
    huso_honninn = forms.CharField(label = '主訴（本人)',required=False, max_length=255,widget=forms.Textarea(attrs={'rows':5, 'cols':80, 'placeholder':'ご本人の主訴','class':'class_name'}))

    shuso_family = forms.CharField(label = '主訴（家族)',required=False, max_length=255,widget=forms.Textarea(attrs={'rows':5, 'cols':80, 'placeholder':'ご家族の主訴','class':'class_name'}))
    
    family_situation = forms.CharField(label = '家族状況',required=False, max_length=255,widget=forms.Textarea(attrs={'rows':5, 'cols':80, 'placeholder':'ご家族の状況','class':'class_name'}))
    
    family_name = forms.CharField(label = '家族氏名', max_length=20,required=False,widget=forms.Textarea(attrs={'rows':1, 'cols':20,'placeholder':'本庄　太郎','class':'class_name',}))
    family_relationship = forms.CharField(label = '続柄', max_length=10,required=False,widget=forms.Textarea(attrs={'rows':1, 'cols':10,'placeholder':'長男','class':'class_name'}))
    family_phone = forms.CharField(label = '電話番号', max_length=14,required=False,widget=forms.Textarea(attrs={'rows':1, 'cols':14,'placeholder':'例）〇〇〇-◎◎◎◎-△△△△','class':'class_name'}))
    family_name2 = forms.CharField(label = '家族氏名2', max_length=20,required=False,widget=forms.Textarea(attrs={'rows':1, 'cols':20,'placeholder':'本庄　花子','class':'class_name',}))
    family_relationship2 = forms.CharField(label = '続柄2', max_length=10,required=False,widget=forms.Textarea(attrs={'rows':1, 'cols':10,'placeholder':'長男の妻','class':'class_name'}))
    family_phone2 = forms.CharField(label = '電話番号2', max_length=14,required=False,widget=forms.Textarea(attrs={'rows':1, 'cols':14,'placeholder':'例）〇〇〇-◎◎◎◎-△△△△','class':'class_name'}))  
    family_name3 = forms.CharField(label = '家族氏名3', max_length=20,required=False,widget=forms.Textarea(attrs={'rows':1, 'cols':20,'placeholder':'本庄　梅子','class':'class_name',}))
    family_relationship3 = forms.CharField(label = '続柄3', max_length=10,required=False,widget=forms.Textarea(attrs={'rows':1, 'cols':10,'placeholder':'長女','class':'class_name'}))
    family_phone3 = forms.CharField(label = '電話番号3', max_length=14,required=False,widget=forms.Textarea(attrs={'rows':1, 'cols':14,'placeholder':'例）〇〇〇-◎◎◎◎-△△△△','class':'class_name'}))  
    
    desease_name = forms.CharField(label = '病名', max_length=20,required=False,widget=forms.Textarea(attrs={'rows':1, 'cols':20,'placeholder':'高血圧症','class':'class_name',}))
    primary_care_doctor = forms.CharField(label = '主治医', max_length=20,required=False,widget=forms.Textarea(attrs={'rows':1, 'cols':10,'placeholder':'本庄医院','class':'class_name'}))
    othe_frequency = forms.CharField(label = 'その他通院頻度', max_length=20,required=False,widget=forms.Textarea(attrs={'rows':1, 'cols':20,'placeholder':'半年に1回等','class':'class_name',}))
    desease_name2 = forms.CharField(label = '病名２', max_length=20,required=False,widget=forms.Textarea(attrs={'rows':1, 'cols':20,'placeholder':'糖尿病','class':'class_name',}))
    primary_care_doctor2 = forms.CharField(label = '主治医２', max_length=20,required=False,widget=forms.Textarea(attrs={'rows':1, 'cols':10,'placeholder':'巨勢病院','class':'class_name'})) 
    othe_frequency2 = forms.CharField(label = 'その他通院頻度２', max_length=20,required=False,widget=forms.Textarea(attrs={'rows':1, 'cols':20,'placeholder':'半年に1回等','class':'class_name',}))
    desease_name3 = forms.CharField(label = '病名３', max_length=20,required=False,widget=forms.Textarea(attrs={'rows':1, 'cols':20,'placeholder':'アルツハイマー型認知症','class':'class_name',}))
    primary_care_doctor3 = forms.CharField(label = '主治医３', max_length=20,required=False,widget=forms.Textarea(attrs={'rows':1, 'cols':10,'placeholder':'佐賀総合病院','class':'class_name'}))   
    othe_frequency3 = forms.CharField(label = 'その他通院頻度３', max_length=20,required=False,widget=forms.Textarea(attrs={'rows':1, 'cols':20,'placeholder':'半年に1回等','class':'class_name',}))
    
    life_history = forms.CharField(label='生活歴', max_length=510,required=False,widget=forms.Textarea(attrs={'rows':5, 'cols':80, 'placeholder':'主な生活歴','class':'class_name'})) 
    disease_history= forms.CharField(label='病歴', max_length=510,required=False,widget=forms.Textarea(attrs={'rows':5, 'cols':80, 'placeholder':'主な病歴','class':'class_name'}))  

    current_service = forms.CharField(label='現在利用しているサービス', max_length=510,required=False,widget=forms.Textarea(attrs={'rows':5, 'cols':80, 'placeholder':'デイサービス：週3回','class':'class_name'})) 

    # id = forms.IntegerField(label = 'ID')     

      

""" class AssessAdl1(forms.ModelForm): 
    '''
    :class Meta:'riyousha', 'nyuuryoku_date'のみ選択。ラベルも選択フィールドにのみ付与
    :htmlで<div>処理をするため、個々にフィールドを作成。グループごとに、htmlで<div>で区切ること。
    '''
    class Meta:
        model = RiyoushaAssessment
    
        fields = ('riyousha', 'nyuuryoku_date')
        labels = {
            'riyousha':'利用者名',
            'nyuuryoku_date':'入力基準日',
        }
    non = forms.BooleanField(label='麻痺なし') """

class Assess_Adl_Koushuku_Form(forms.ModelForm): 
    class Meta:
        model = RiyoushaAssessment 
        def __init__(self, hana_cm = None,*args, **kwargs):
            self.hana_cm = hana_cm
            super().__init__(*args, **kwargs)

            for field in self.Meta.required:
                self.fields[field].required = False

        fields = '__all__'
        required = ('non', 'left_upper_limbs', 'left_lower_limbs','right_upper_limbs',
                  'right_lower_limbs', 'others', 'paralysis_others',)  
        labels = {
            'name':'氏名',
            'nyuuryoku_date':'入力日',
            'non':'麻痺なし',
            'left_upper_limbs':'左上肢',
            'left_lower_limbs':'左下肢',
            'right_upper_limbs':'右上肢',
            'right_lower_limbs':'右下肢',
            'koushuku_hiza':'膝関節',
            'others':'その他の麻痺',
            'paralysis_others':'その他の麻痺の詳細',   
        } 

        non = forms.ChoiceField(label = '麻痺なし',required=False,
                widget=forms.DateInput(attrs={'id': 'one','class': 'form-check-input'}))
