from rest_framework import serializers
from .models import KafkaDemo

class KafkaDemoSerializer(serializers.ModelSerializer):
    class Meta:
        model = KafkaDemo
        fields = '__all__'

