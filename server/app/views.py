from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import JobListing
from .serializers import JobListingSerializer

@api_view(['POST'])
def create_job(request):
    if request.method == 'POST':
        serializer = JobListingSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def get_jobs(request, employer_id):
    if request.method == 'GET':
        jobs = JobListing.objects.filter(employer_id=employer_id)
        serializer = JobListingSerializer(jobs, many=True)
        return Response(serializer.data)

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