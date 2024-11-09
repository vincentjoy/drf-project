from rest_framework import serializers
from .models import Movie

# def description_length(value):
#     if len(value) > 200:
#         raise serializers.ValidationError("Description should be less than or equal to 200 characters.")

# class MovieSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     name = serializers.CharField()
#     description = serializers.CharField(validators=[description_length])
#     active = serializers.BooleanField()

#     def create(self, validated_data):
#         return Movie.objects.create(**validated_data)

#     def update(self, instance, validated_data):
#         instance.name = validated_data.get('name', instance.name)
#         instance.description = validated_data.get('description', instance.description)
#         instance.active = validated_data.get('active', instance.active)
#         instance.save()
#         return instance

#     def validate(self, data):
#         if data['name'] == data['description']:
#             raise serializers.ValidationError("Title and description cannot be the same.")
#         return data

#     def validate_name(self, value):
#         if len(value) < 3:
#             raise serializers.ValidationError("Name should be at least 3 characters long.")
#         return value