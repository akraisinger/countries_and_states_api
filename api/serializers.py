from rest_framework import serializers
from .models import Country, State

class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = ['id', 'code', 'name']

class StateSerializer(serializers.Serializer):
    
    code = serializers.CharField(required=True, max_length=4)
    name = serializers.CharField(required=True, max_length=100)
    countryId = serializers.IntegerField(source='country_id')

    def create(self, validated_data):
        return State.objects.create(**validated_data)

# Old StateSerializer
# class StateSerializer(serializers.ModelSerializer):
#     #countryId = serializers.SerializerMethodField('get_alternate_country_id_name')

#     class Meta:
#         model = State
#         fields = ['id', 'code', 'name', 'country']

#     # def get_alternate_country_id_name(self, obj):
#     #     return obj.country_id