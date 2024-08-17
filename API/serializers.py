from rest_framework import serializers
from .models import EmployeeDetails, Department, Skill, Training, EmployeeSkill, JobRequirement, TrainingNeed


from django_countries.fields import Country
from django_countries import countries

class CountryField(serializers.ChoiceField):
    def __init__(self, **kwargs):
        # Initialize with the list of countries from django_countries
        kwargs['choices'] = countries
        super().__init__(**kwargs)

    def to_representation(self, value):
        # Convert the Country object to its string representation (e.g., 'US')
        if isinstance(value, Country):
            return str(value)
        return str(value)

    def to_internal_value(self, data):
        # Convert the string back to a Country object
        if data in countries:
            return data
        self.fail('invalid_choice', input=data)
    

class EmployeeDetailsSerializers(serializers.ModelSerializer):
    nationality = CountryField() 
    
    class Meta:
        model = EmployeeDetails
        #fields = ('project_name', 'project_owner', 'start_date', 'end_date', 'comments', 'status')
        exclude = ('created_at', 'modified_at')
        #if you want to include all fields just stop at model = EmployeeDetails
        
        
        


# class DepartmentSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Department
#         fields = ('name_of_department', 'department_code', 'department_head', 'description')
        

class DepartmentSerializer(serializers.ModelSerializer):
    department_head = serializers.PrimaryKeyRelatedField(
        queryset=EmployeeDetails.objects.all(),  # Allows selection by ID
        allow_null=True,  # Allow null values if the department head is optional
        required=False  # Make it optional during creation
    )

    class Meta:
        model = Department
        fields = ('id', 'name_of_department', 'department_code', 'department_head', 'description')


class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skill
        fields = '__all__'
        #exclude = ('created_at', 'modified_at') bcos i want to display created at and modified at
        #i made fields to be all and made them read only so they wont be required during creation
        #but would be displayed on my front end
        read_only_fields = ('created_at', 'modified_at') 
        

class TrainingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Training
        fields = '__all__'
       


class EmployeeSkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmployeeSkill
        fields = '__all__'     


class JobRequirementSerializer(serializers.ModelSerializer):
    class Meta:
        model = JobRequirement
        fields = '__all__'     



class TrainingneedSerializer(serializers.ModelSerializer):
    class Meta:
        model = TrainingNeed
        fields = '__all__'     

