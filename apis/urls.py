from django.urls import include, path
# from django.conf.urls import url
from rest_framework import routers
# from allauth.account.views import confirm_email
from .views import CourseViewSet, CandidateViewset, CompetenciesViewset, EducationViewset
from .views import CertificationViewset, AwardViewset, SkillViewset, ExperienceViewset
from .views import JobDescriptionViewset, CommonViewset
#, UserViewSet

router = routers.DefaultRouter()

router.register(r'course', CourseViewSet)
router.register(r'candidate', CandidateViewset, basename='candidateview')
router.register(r'competencies', CompetenciesViewset)
router.register(r'education', EducationViewset)
router.register(r'certification', CertificationViewset)
router.register(r'award', AwardViewset)
router.register(r'skill', SkillViewset)
router.register(r'experience', ExperienceViewset)
router.register(r'jd', JobDescriptionViewset)
router.register(r'commonview', CommonViewset, basename='commonview')
# router.register(r'users', UserViewSet)

urlpatterns = [
    path('', include(router.urls)),
    # path('rest-auth/', include('rest_auth.urls')),
    # path('rest-auth/registration', include('rest_auth.registration.urls')),
    # path('account/', include('allauth.urls')),
    # url(r'^accounts-rest/registration/account-confirm-email/(?P<key>.+)/$', confirm_email, name='account_confirm_email'),
]