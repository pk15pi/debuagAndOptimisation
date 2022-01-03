from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.core.checks.messages import Error
from django.db import models
from django.db.models.expressions import F
from django.utils import timezone
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _


class UserManager(BaseUserManager):
    def create_user(self, email, password=None, **extrafields):
        """
        Creates and saves a User with the given email and password.
        """
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(email=self.normalize_email(email),)
        user = self.model(email=email, **extrafields)

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_staffuser(self, email, password, **extrafields):
        """
        Creates and saves a staff user with the given email and password.
        """
        user = self.create_user(email, password=password, **extrafields)
        user.staff = True
        user.verified=True
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password):
        """
        Creates and saves a superuser with the given email and password.
        """
        user = self.create_user(email,password=password,)
        user.staff = True
        user.admin = True
        user.verified=True
        user.save(using=self._db)
        return user



class User(AbstractBaseUser):    
    def minpassword(value):
        if len(value) < 8:
            raise Error('password must be minimum 8 Char')
    def clean(self):
        if (self.password != self.repeat_password):
            raise Error('Password doesnt match')
        if (self.email):
            try:
                User.objects.get(email = self.email)
                raise Error("Email already ")
            except Exception as e:
                return e
        if self.username:
            try:
                User.objects.get(username = self.username)
                raise Error("User name already taken")
            except Exception as e:
                return e

    @property
    def is_staff(self):
        return self.staff

    @property
    def is_admin(self):
        return self.admin
    
    email = models.EmailField(_('email address'), unique=True)
    first_name = models.TextField(max_length=50, blank=False, null=False)
    last_name = models.TextField(max_length=50, blank=False, null= False)
    gender = models.TextField(blank=False, null=False)
    mobile = models.IntegerField(blank=False, null=False)
    USERNAME_FIELD = 'email'

    objects = UserManager()
    
    def __str__(self):
          return self.email




class Course(models.Model):
    course_code = models.CharField(max_length=25, null=False)
    course_name = models.CharField(max_length=150, null=False)
    institute_name = models.CharField(max_length=100, null=False)
    institute_location = models.CharField(max_length=50, null=False)
    start_date = models.DateField(default=timezone.now)
    end_date = models.DateField(default=timezone.now)

    def __str__(self):
          return self.course_name



class Candidate(models.Model):
    id_email = models.CharField(max_length=100, null=True, blank=True) 
    course = models.PositiveIntegerField(null=False, default=0)
    name = models.CharField(max_length=50, null=False)
    rank = models.CharField(max_length=25, null=True, blank=True)
    service = models.CharField(max_length=20, null=True, blank=True)
    experience = models.CharField(max_length=20, null=True, blank=True)
    qualification = models.CharField(max_length=25, null=False)
    gender = models.CharField(max_length=10, null=False)
    phone_no = models.CharField(max_length=10, null=True, blank=True)
    email = models.CharField(max_length=100, null=True, blank=True)
    linkedIn = models.TextField(null=True, blank=True)
    image_url = models.TextField(null=True, blank=True)
    introduction = models.TextField(null=True, blank=True)

    # ROLE 
    hrm_role = models.BooleanField(default=False)
    scm_role = models.BooleanField(default=False)
    operation_role = models.BooleanField(default=False)
    project_role = models.BooleanField(default=False)
    security_role = models.BooleanField(default=False)
    admin_role = models.BooleanField(default=False)
    it_role = models.BooleanField(default=False)
    aviation_role = models.BooleanField(default=False)

    @property
    def competecy(self):
        return Competencies.object.filter(candidate__id = self.id)

    @property
    def education(self):
        return Education.object.filter(candidate__id = self.id)

    @property
    def certification(self):
        return Certification.object.filter(candidate__id = self.id)

    @property
    def awards(self):
        return Award.object.filter(candidate__id = self.id)

    @property
    def skills(self):
        return Skill.object.filter(candidate__id = self.id)

    @property
    def experiences(self):
        return Experience.object.filter(candidate__id = self.id)

    @property
    def roles(self):
        return Role.object.filter(candidate__id = self.id)

    @property
    def industries(self):
        return Industry.object.filter(candidate__id = self.id)

    def __str__(self):
          return self.name


class Photos(models.Model):
    candidate = models.ForeignKey(Candidate, related_name="photo", on_delete=models.CASCADE)
    photo = models.ImageField(upload_to='images/')


class Competencies(models.Model):
    candidate = models.ForeignKey(Candidate, related_name="competencies", on_delete=models.CASCADE)
    core_competencies = models.CharField(max_length=50, null=False)
    percentage = models.PositiveIntegerField(null=True, default=0)

    def __str__(self):
          return self.core_competencies


class Education(models.Model):
    candidate = models.ForeignKey(Candidate, related_name="education", on_delete=models.CASCADE)
    qualification = models.CharField(max_length=100, null=False)
    institute = models.CharField(max_length=100, null=False)
    year = models.PositiveIntegerField(null=True, default=0)

    def __str__(self):
          return self.qualification


class Certification(models.Model):
    candidate = models.ForeignKey(Candidate, related_name="certification", on_delete=models.CASCADE)
    certificate = models.CharField(max_length=100, null=False)
    institute = models.CharField(max_length=100, null=False)
    valid_upto = models.PositiveIntegerField(null=True, default=0)

    def __str__(self):
          return self.certificate



class Award(models.Model):
    candidate = models.ForeignKey(Candidate, related_name="awards", on_delete=models.CASCADE)
    award = models.TextField(null=False)
    
    def __str__(self):
          return self.award



class Skill(models.Model):
    candidate = models.ForeignKey(Candidate, related_name="skills", on_delete=models.CASCADE)
    skill = models.CharField(max_length=50, null=False)
    percentage = models.PositiveIntegerField(null=True, default=0)

    def __str__(self):
          return self.skill



class Experience(models.Model):
    candidate = models.ForeignKey(Candidate, related_name="experiences", on_delete=models.CASCADE)
    role = models.CharField(max_length=100, null=False)
    org_name = models.CharField(max_length=100, null=True, blank=True)
    org_location = models.CharField(max_length=50, null=True, blank=True)
    start_date = models.DateField(default=timezone.now, null=True, blank=True)
    end_date = models.DateField(default=timezone.now, null=True, blank=True)

    def __str__(self):
          return self.role



class JobDescription(models.Model):
    role = models.ForeignKey(Experience, related_name="jobdescription", on_delete=models.CASCADE)
    jd = models.TextField(null=False)

    def __str__(self):
          return self.jd


class Role(models.Model):
    candidate = models.ForeignKey(Candidate, related_name="role", on_delete=models.CASCADE)

    administration = models.BooleanField(default=False)
    aviation_role = models.BooleanField(default=False)
    business_development = models.BooleanField(default=False)
    facility_management= models.BooleanField(default=False)
    finance = models.BooleanField(default=False)
    hospital_administration = models.BooleanField(default=False)
    hrm = models.BooleanField(default=False)
    iot_blockchain_datascience = models.BooleanField(default=False)
    strategy_management = models.BooleanField(default=False)
    operations = models.BooleanField(default=False)
    product_management = models.BooleanField(default=False)
    project_management = models.BooleanField(default=False)
    qa_qc = models.BooleanField(default=False)
    scm = models.BooleanField(default=False)
    security = models.BooleanField(default=False)
    technical_content_writing = models.BooleanField(default=False)
    marine_weapons_systems = models.BooleanField(default=False)
    employee_relations = models.BooleanField(default=False)
    occupational_safety = models.BooleanField(default=False)
    legal_compliance = models.BooleanField(default=False)
    education_org = models.BooleanField(default=False)
    it_ites = models.BooleanField(default=False)
    
    
    def __str__(self):
          return self.administration



class Industry(models.Model):
    candidate = models.ForeignKey(Candidate, related_name="industry", on_delete=models.CASCADE)

    avionics = models.BooleanField(default=False)
    aviation = models.BooleanField(default=False)
    automobile= models.BooleanField(default=False)
    consultant= models.BooleanField(default=False)
    cyber_security= models.BooleanField(default=False)
    defence_sector= models.BooleanField(default=False)
    e_commerce= models.BooleanField(default=False)
    fmcg= models.BooleanField(default=False)
    health_care= models.BooleanField(default=False)
    infra= models.BooleanField(default=False)
    it_ites = models.BooleanField(default=False)
    logistics = models.BooleanField(default=False)
    pharma_biotech = models.BooleanField(default=False)
    r_and_d = models.BooleanField(default=False)
    service_sector= models.BooleanField(default=False)
    ship_building= models.BooleanField(default=False)
    social_service_sector= models.BooleanField(default=False)
    telecom= models.BooleanField(default=False)
    training= models.BooleanField(default=False)
    education= models.BooleanField(default=False)
    semiconductor_design_fab= models.BooleanField(default=False)
    weapon_system= models.BooleanField(default=False)
    
    def __str__(self):
          return self.aviation
