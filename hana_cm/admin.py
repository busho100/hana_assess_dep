from django.contrib import admin
from .models import RiyoushaAttributes,CareManager,RiyoushaAssessment
from .models import Ninchisho_Jiritudo,Shogai_Jiritudo,Medical_Insurance
from .models import Riyousha,Pension_Insurance,Gender,Kaigodo,FrequencyOfHospitalVisits
from .models import DisabilityNotebook,ExaminationStatus

# Register your models here.

# admin.site.register(Riyousha_kihon)

admin.site.register(CareManager)

admin.site.register(Kaigodo)
admin.site.register(Riyousha)
admin.site.register(RiyoushaAttributes)
admin.site.register(RiyoushaAssessment)
admin.site.register(Shogai_Jiritudo)
admin.site.register(Ninchisho_Jiritudo)
admin.site.register(Medical_Insurance)
admin.site.register(Pension_Insurance)
admin.site.register(Gender)
admin.site.register(FrequencyOfHospitalVisits)
admin.site.register(DisabilityNotebook)
admin.site.register(ExaminationStatus)

