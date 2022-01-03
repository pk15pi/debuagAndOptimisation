from django.contrib import admin

from .models import Course, Candidate, Competencies, Education, Photos
from .models import Certification, Award, Skill, Experience
from .models import JobDescription, User


# Register your models here.

admin.site.register(Course)
admin.site.register(Candidate)
admin.site.register(Competencies)
admin.site.register(Education)
admin.site.register(Certification)
admin.site.register(Award)
admin.site.register(Skill)
admin.site.register(Experience)
admin.site.register(JobDescription)
admin.site.register(Photos)
# admin.site.register(User)