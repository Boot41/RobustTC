from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import JobListing, JobApplication, JobSeekerProfile
from .serializers import JobListingSerializer, JobApplicationSerializer
from .serializers import JobSeekerProfileSerializer

class JobSeekerProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = JobSeekerProfile
        fields = ['seeker_id', 'work_history', 'skills', 'education']

@api_view(['POST'])
def create_job_seeker_profile(request):
    if request.method == 'POST':
        serializer = JobSeekerProfileSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def get_job_seeker_profile(request, seeker_id):
    if request.method == 'GET':
        try:
            profile = JobSeekerProfile.objects.get(seeker_id=seeker_id)
            serializer = JobSeekerProfileSerializer(profile)
            return Response(serializer.data)
        except JobSeekerProfile.DoesNotExist:
            return Response({'error': 'Profile not found'}, status=status.HTTP_404_NOT_FOUND)

@api_view(['PUT'])
def update_job_seeker_profile(request, seeker_id):
    try:
        profile = JobSeekerProfile.objects.get(seeker_id=seeker_id)
    except JobSeekerProfile.DoesNotExist:
        return Response({'error': 'Profile not found'}, status=status.HTTP_404_NOT_FOUND)

    serializer = JobSeekerProfileSerializer(profile, data=request.data, partial=True)  # Allow partial updates
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
