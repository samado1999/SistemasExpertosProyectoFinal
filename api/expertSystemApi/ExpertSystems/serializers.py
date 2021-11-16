from rest_framework import serializers
from ExpertSystems.models import symptoms, expertreponse

# class diseaseSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = disease
#         fields = ('description', 'symptoms', 'treatment')

class symptomsSerializer(serializers.ModelSerializer):
    class Meta:
        model = symptoms
        fields = ('gender', 'age', 'pas_no_trat', 'pas_trat', 'diabetes', 'smoking_status', 'ecv', 'fa', 'hvi')

class expertreponseSerializer(serializers.ModelSerializer):
    class Meta:
        model = expertreponse
        fields = ('id_disease', 'description', 'treatment')