from rest_framework import serializers
from rest_framework.relations import ManyRelatedField

from .models import Course, Candidate, Competencies, Education, Role
from .models import Certification, Award, Skill, Experience
from .models import JobDescription, Industry, User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'id',
            'email',
            'first_name',
            'last_name',
            'gender',
            'mobile'
        ]


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'
        read_only_fields = list(fields)


class CandidateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Candidate
        fields = '__all__'


class CompetenciesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Competencies
        fields = '__all__'


class EducationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Education
        fields = '__all__'


class CertificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Certification
        fields = '__all__'


class AwardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Award
        fields = '__all__'


class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skill
        fields = '__all__'


class ExperienceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Experience
        fields = '__all__'

class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Role
        fields = '__all__'


class JobDescriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = JobDescription
        fields = '__all__'


class IndustrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Industry
        fields = '__all__'
        

class CommonSerializer(serializers.ModelSerializer):

    competency = CompetenciesSerializer(source='competencies', many=True)
    edn = EducationSerializer(source='education', many=True)
    certificate = CompetenciesSerializer(source='certification', many=True)
    awrd = AwardSerializer(source='awards', many=True)
    skl = SkillSerializer(source='skills', many=True)
    expernc = ExperienceSerializer(source='experiences', many=True)
    # rl = RoleSerializer(source='roles', many=True)
    # indst = IndustrySerializer(source='industries', many=True)
    class Meta:
        model = Candidate
        fields = [
    'id_email', 
    'course',
    'name',
    'rank',
    'service',
    'experience',
    'qualification',
    'gender',
    'phone_no',
    'email',
    'linkedIn',
    'image_url',
    'introduction',
    'hrm_role',
    'scm_role',
    'operation_role',
    'project_role',
    'security_role',
    'admin_role',
    'it_role',
    'aviation_role',
    'competency',
    'edn',
    'certificate',
    'awrd',
    'skl',
    'expernc',
    # 'rl',
    # 'indst'
    ]
