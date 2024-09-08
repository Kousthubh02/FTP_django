from django.http import JsonResponse
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated  # Add authentication permission
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from .models import CV
from .serializers import *


    
def get (*args, **kwargs):
        # Retrieve all Pdfs if user is not authenticated
        file_names = CV.objects.all()

        serializer = CVSerializer(file_names, many=True)
        return JsonResponse(serializer.data, status=status.HTTP_200_OK,safe=False)
    
    
@csrf_exempt
def upload_CV(request, *args, **kwargs):
        if request.method == 'POST':
            pdf_file = request.FILES['file']
            pdf_document = CV(name=pdf_file.name, CV=pdf_file)
            pdf_document.save()
            return JsonResponse({'message': 'File uploaded successfully'}, status=status.HTTP_201_CREATED)
        else:
            return JsonResponse({'message': 'File upload failed'}, status=status.HTTP_400_BAD_REQUEST)

@csrf_exempt
def upload_publications(request, *args, **kwargs):
        if request.method == 'POST':
            pdf_file = request.FILES['file']
            pdf_document = Publications(name=pdf_file.name, publications=pdf_file)
            pdf_document.save()
            return JsonResponse({'message': 'File uploaded successfully'}, status=status.HTTP_201_CREATED)
        else:
            return JsonResponse({'message': 'File upload failed'}, status=status.HTTP_400_BAD_REQUEST)


@csrf_exempt
@api_view(['POST'])
def create_personal_details(request):
    serializer = PersonalDetailsSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({'message': 'Personal details saved successfully'}, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)        



from django.core.exceptions import ValidationError
from rest_framework.decorators import api_view  # Assuming using Django REST Framework
from rest_framework import status

@csrf_exempt
@api_view(['POST'])
def upload_profile_image(request):
    if request.method=='POST':
        image= request.FILES['image']
        image_file=ProfileSerializer(data={'teacher_id':request.data['teacher_id'],'image_path':image})
        if image_file.is_valid():
            image_file.save()
            return JsonResponse({'message': 'Profile image uploaded successfully'}, status=status.HTTP_201_CREATED)
        else :
            return Response(image_file.errors, status=status.HTTP_400_BAD_REQUEST)
@csrf_exempt
@api_view(['POST'])
def create_specialization_details(request):
    serializer = SpecializationSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({'message': 'Specialization details saved successfully'}, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)        

@csrf_exempt
@api_view(['POST'])
def create_subject_details(request):
    serializer = SubjectSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({'message': 'Subject details saved successfully'}, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)        

@csrf_exempt
@api_view(['POST'])
def create_research_details(request):
    serializer = ResearchProjectSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({'message': 'research details saved successfully'}, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)        

@csrf_exempt
@api_view(['POST'])
def create_consultancy_details(request):
    serializer = ConcultancyProjectSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({'message': 'research details saved successfully'}, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)        


