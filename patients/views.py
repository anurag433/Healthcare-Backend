from rest_framework.views import APIView
from .models import Patient
from .serializers import PatientSerializers
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status

class PatientAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get_object(self, id, user):
        try:
            return Patient.objects.get(
                id=id,
                created_by=user
            )
        except Patient.DoesNotExist:
            return None
        
    def get(self, request, id=None):
        if id:
            patient = self.get_object(id, request.user)
            if not patient:
                return Response(
                    {
                        "error": "Patient not found"
                    },
                    status=status.HTTP_404_NOT_FOUND
                )
            
            serializer = PatientSerializers(patient)
            return Response(serializer.data, status=status.HTTP_200_OK)
        
        patients = Patient.objects.filter(created_by=request.user)
        serializer = PatientSerializers(patients, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request):
        serializer = PatientSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save(
                created_by = request.user
            )
            return Response(
                {
                    "message": "Patient created successfully",
                    "data": serializer.data
                },
                status=status.HTTP_201_CREATED
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, id):
        patient = self.get_object(id, request.user)
        if not patient:
            return Response(
                {
                    "error": "Patient not found"
                },
                status=status.HTTP_404_NOT_FOUND
            )
        serializer = PatientSerializers(patient, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(
                {
                    "message": "Patient updated",
                    "data": serializer.data
                },
                status=status.HTTP_200_OK
            )

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)      
        
    def delete(self, request, id):
        patient = self.get_object(id,request.user)
        if not patient:
            return Response(
                {
                    "error": "Patient not found"
                },
                status=status.HTTP_404_NOT_FOUND
            )

        patient.delete()
        return Response(
            {
                "message": "Patient deleted "
            },
            status=status.HTTP_200_OK
        )

