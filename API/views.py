from django.shortcuts import render
from django.http import HttpResponse
from .models import EmployeeDetails, Department, Skill, Training, EmployeeSkill, JobRequirement, TrainingNeed

from rest_framework import viewsets, permissions

from .serializers import EmployeeDetailsSerializers, TrainingneedSerializer, JobRequirementSerializer, DepartmentSerializer, SkillSerializer, TrainingSerializer, EmployeeSkillSerializer

from rest_framework.response import Response

from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly

from rest_framework import status



# Create your views here.

def home(request):
    
    return HttpResponse('Welcome to our home page')



class EmpAPIviewset(viewsets.ViewSet):
    #permission_classes = [permissions.AllowAny]
    #permission_classes = [IsAuthenticated]
    
    queryset = EmployeeDetails.objects.all()
    serializer_class = EmployeeDetailsSerializers
    
    def list(self, request):
        queryset = self.queryset
        serializer = self.serializer_class(queryset, many = True) #to display many records
        return Response(serializer.data)
        #At this point point you can check the url and you would see all records
        
    def create(self, request):
        serializer = self.serializer_class(data= request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=400) 
        

    def retrieve(self, request, pk=None):
        mevabemp= self.queryset.get(pk=pk)
        serializer = self.serializer_class(mevabemp)
        return Response(serializer.data)

    def update(self, request, pk=None):
        mevabemp = self.queryset.get(pk=pk)
        serializer = self.serializer_class(mevabemp, data= request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=400) 
        
        

    def destroy(self, request, pk=None):
        mevabemp = self.queryset.get(pk=pk)
        mevabemp.delete()
        return Response(status=204)
        


class Departmentviewset(viewsets.ModelViewSet):
    #permission_classes = [IsAuthenticated]
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer

    def list(self, request):
        queryset = self.queryset
        serializer = self.serializer_class(queryset, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            print(serializer.data)  # Log the serializer data
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            print(serializer.errors)  # Log serializer errors
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        dept = self.queryset.get(pk=pk)
        serializer = self.serializer_class(dept)
        return Response(serializer.data)

    def update(self, request, pk=None):
        dept = self.queryset.get(pk=pk)
        serializer = self.serializer_class(dept, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=400)
        
    def destroy(self, request, pk=None):
        try:
            dept = self.queryset.get(pk=pk)
        except Department.DoesNotExist:
            return Response({"error": "Department not found."}, status=status.HTTP_404_NOT_FOUND)
        
        dept.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



# class Departmentviewset(viewsets.ViewSet):
    
#     # permission_classes = [IsAuthenticated]
    
#     queryset = Department.objects.all()
#     serializer_class = DepartmentSerializer
    
#     def list(self, request):
#         queryset = self.queryset
#         serializer = self.serializer_class(queryset, many = True) 
#         return Response(serializer.data)
       
        
#     def create(self, request):
#         serializer = self.serializer_class(data= request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         else:
#             return Response(serializer.errors, status=400) 
        

#     def retrieve(self, request, pk=None):
#         dept= self.queryset.get(pk=pk)
#         serializer = self.serializer_class(dept)
#         return Response(serializer.data)

#     def update(self, request, pk=None):
#         dept = self.queryset.get(pk=pk)
#         serializer = self.serializer_class(dept, data= request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         else:
#             return Response(serializer.errors, status=400) 
        
        

#     def destroy(self, request, pk=None):
#         dept = self.queryset.get(pk=pk)
#         dept.delete()
#         return Response(status=204)
    

class Skillviewset(viewsets.ViewSet):
    
    #permission_classes = [IsAuthenticated]
    
    queryset = Skill.objects.all()
    serializer_class = SkillSerializer
    
    def list(self, request):
        queryset = self.queryset
        serializer = self.serializer_class(queryset, many = True) 
        return Response(serializer.data)
       
        
    def create(self, request):
        serializer = self.serializer_class(data= request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=400) 
        

    def retrieve(self, request, pk=None):
        skill= self.queryset.get(pk=pk)
        serializer = self.serializer_class(skill)
        return Response(serializer.data)

    def update(self, request, pk=None):
        skill = self.queryset.get(pk=pk)
        serializer = self.serializer_class(skill, data= request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=400) 
        
        

    def destroy(self, request, pk=None):
        skill = self.queryset.get(pk=pk)
        skill.delete()
        return Response(status=204)
    



class Departmentviewset(viewsets.ViewSet):
    
    #permission_classes = [IsAuthenticated]
    
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer
    
    def list(self, request):
        queryset = self.queryset
        serializer = self.serializer_class(queryset, many = True) 
        return Response(serializer.data)
       
        
    def create(self, request):
        serializer = self.serializer_class(data= request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=400) 
        

    def retrieve(self, request, pk=None):
        dept= self.queryset.get(pk=pk)
        serializer = self.serializer_class(dept)
        return Response(serializer.data)

    def update(self, request, pk=None):
        dept = self.queryset.get(pk=pk)
        serializer = self.serializer_class(dept, data= request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=400) 
        
        

    def destroy(self, request, pk=None):
        dept = self.queryset.get(pk=pk)
        dept.delete()
        return Response(status=204)
    

class Trainingviewset(viewsets.ViewSet):
    
    #permission_classes = [IsAuthenticated]
    
    queryset = Training.objects.all()
    serializer_class = TrainingSerializer
    
    def list(self, request):
        queryset = self.queryset
        serializer = self.serializer_class(queryset, many = True) 
        return Response(serializer.data)
       
        
    def create(self, request):
        serializer = self.serializer_class(data= request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=400) 
        

    def retrieve(self, request, pk=None):
        training= self.queryset.get(pk=pk)
        serializer = self.serializer_class(training)
        return Response(serializer.data)

    def update(self, request, pk=None):
        training = self.queryset.get(pk=pk)
        serializer = self.serializer_class(training, data= request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=400) 
        
        

    def destroy(self, request, pk=None):
        training = self.queryset.get(pk=pk)
        training.delete()
        return Response(status=204)
    
    
    


class   EmployeeSkillviewset(viewsets.ViewSet):
    
    #permission_classes = [IsAuthenticated]
    
    queryset = EmployeeSkill.objects.all()
    serializer_class = EmployeeSkillSerializer
    
    def list(self, request):
        queryset = self.queryset
        serializer = self.serializer_class(queryset, many = True) 
        return Response(serializer.data)
       
        
    def create(self, request):
        serializer = self.serializer_class(data= request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=400) 
        

    def retrieve(self, request, pk=None):
        empskill= self.queryset.get(pk=pk)
        serializer = self.serializer_class(empskill)
        return Response(serializer.data)

    def update(self, request, pk=None):
        empskill = self.queryset.get(pk=pk)
        serializer = self.serializer_class(empskill, data= request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=400) 
        
        

    def destroy(self, request, pk=None):
        empskill = self.queryset.get(pk=pk)
        empskill.delete()
        return Response(status=204)
    
    


class   JobRequirementviewset(viewsets.ViewSet):
    
    #permission_classes = [IsAuthenticated]
    
    queryset = JobRequirement.objects.all()
    serializer_class = JobRequirementSerializer
    
    def list(self, request):
        queryset = self.queryset
        serializer = self.serializer_class(queryset, many = True) 
        return Response(serializer.data)
       
        
    def create(self, request):
        serializer = self.serializer_class(data= request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=400) 
        

    def retrieve(self, request, pk=None):
        jobreq= self.queryset.get(pk=pk)
        serializer = self.serializer_class(jobreq)
        return Response(serializer.data)

    def update(self, request, pk=None):
        jobreq = self.queryset.get(pk=pk)
        serializer = self.serializer_class(jobreq, data= request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=400) 
        
        

    def destroy(self, request, pk=None):
        jobreq = self.queryset.get(pk=pk)
        jobreq.delete()
        return Response(status=204)


class Trainingneedviewset(viewsets.ViewSet):
    
    #permission_classes = [IsAuthenticated]
    
    queryset = TrainingNeed.objects.all()
    serializer_class = TrainingneedSerializer
    
    def list(self, request):
        queryset = self.queryset
        serializer = self.serializer_class(queryset, many = True) 
        return Response(serializer.data)
       
        
    def create(self, request):
        serializer = self.serializer_class(data= request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=400) 
        

    def retrieve(self, request, pk=None):
        trainneed= self.queryset.get(pk=pk)
        serializer = self.serializer_class(trainneed)
        return Response(serializer.data)

    def update(self, request, pk=None):
        trainneed = self.queryset.get(pk=pk)
        serializer = self.serializer_class(trainneed, data= request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=400) 
        
        

    def destroy(self, request, pk=None):
        trainneed = self.queryset.get(pk=pk)
        trainneed.delete()
        return Response(status=204)

