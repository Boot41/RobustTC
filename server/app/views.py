from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import JobListing, JobApplication
from .serializers import JobListingSerializer
from .serializers import JobApplicationSerializer

class JobApplicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = JobApplication
        fields = ['job_listing', 'seeker_id', 'status', 'date_applied']

@api_view(['POST'])
def apply_for_job(request, job_id):
    if request.method == 'POST':
        serializer = JobApplicationSerializer(data=request.data)
        if serializer.is_valid():
            job_listing = JobListing.objects.filter(id=job_id, is_active=True).first()
            if job_listing:
                serializer.save(job_listing=job_listing)
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response({'error': 'Job not found or inactive'}, status=status.HTTP_404_NOT_FOUND)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def get_application_status(request, seeker_id):
    if request.method == 'GET':
        applications = JobApplication.objects.filter(seeker_id=seeker_id)
        serializer = JobApplicationSerializer(applications, many=True)
        return Response(serializer.data)

@api_view(['GET'])
def get_applications_for_job(request, job_id):
    if request.method == 'GET':
        applications = JobApplication.objects.filter(job_listing_id=job_id)
        serializer = JobApplicationSerializer(applications, many=True)
        return Response(serializer.data)

@api_view(['PUT'])
def update_application_status(request, application_id):
    try:
        application = JobApplication.objects.get(id=application_id)
    except JobApplication.DoesNotExist:
        return Response({'error': 'Application not found'}, status=status.HTTP_404_NOT_FOUND)

    serializer = JobApplicationSerializer(application, data=request.data, partial=True)  # Allow partial updates
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def withdraw_application(request, application_id):
    try:
        application = JobApplication.objects.get(id=application_id)
        application.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    except JobApplication.DoesNotExist:
        return Response({'error': 'Application not found'}, status=status.HTTP_404_NOT_FOUND)

@api_view(['POST'])
def create_job(request):
    if request.method == 'POST':
        serializer = JobListingSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def get_jobs(request):
    if request.method == 'GET':
        title = request.query_params.get('title', None)
        location = request.query_params.get('location', None)
        job_type = request.query_params.get('type', None)
        date_posted = request.query_params.get('date_posted', None)

        jobs = JobListing.objects.all()
        if title:
            jobs = jobs.filter(title__icontains=title)
        if location:
            jobs = jobs.filter(location__icontains=location)
        if job_type:
            jobs = jobs.filter(job_type=job_type)
        if date_posted:
            jobs = jobs.filter(date_posted=date_posted)

        serializer = JobListingSerializer(jobs, many=True)
        return Response(serializer.data)

@api_view(['GET'])
def get_job_detail(request, job_id):
    try:
        job = JobListing.objects.get(id=job_id)
    except JobListing.DoesNotExist:
        return Response({'error': 'Job not found'}, status=status.HTTP_404_NOT_FOUND)
    serializer = JobListingSerializer(job)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['PUT'])
def update_job(request, job_id):
    try:
        job = JobListing.objects.get(id=job_id)
    except JobListing.DoesNotExist:
        return Response({'error': 'Job not found'}, status=status.HTTP_404_NOT_FOUND)

    serializer = JobListingSerializer(job, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def delete_job(request, job_id):
    try:
        job = JobListing.objects.get(id=job_id)
    except JobListing.DoesNotExist:
        return Response({'error': 'Job not found'}, status=status.HTTP_404_NOT_FOUND)
    job.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)