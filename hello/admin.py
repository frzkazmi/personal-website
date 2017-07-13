from django.contrib import admin
from .models import Person
from .models import Company
from .models import PersonalProject
from .models import CompanyProject
from .models import Education
from .models import TechnicalSkill
from .models import Skills
from .models import Strength


admin.site.register(Person)
admin.site.register(PersonalProject)
admin.site.register(Company)
admin.site.register(CompanyProject)
admin.site.register(Education)
admin.site.register(TechnicalSkill)
admin.site.register(Skills)
admin.site.register(Strength)