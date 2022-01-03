
from django.contrib import admin
from django.urls import path, include
from allauth.account.views import confirm_email
from django.conf.urls import url

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('apis.urls')),
    path('rest-auth/', include('rest_auth.urls')),
    url(r'^rest-auth/registration/', include('rest_auth.registration.urls')),
    url(r'^account/', include('allauth.urls')),
    path('reset-password/', include('django_rest_passwordreset.urls', namespace='password_reset')),
    url(r'^accounts-rest/registration/account-confirm-email/(?P<key>.+)/$', confirm_email, name='account_confirm_email'),   
]


# urlpatterns = [
#     path("validate_token/", reset_password_validate_token, name="reset-password-validate"),
#     path("confirm/", reset_password_confirm, name="reset-password-confirm"),
#     path("", reset_password_request_token, name="reset-password-request"),
# ]