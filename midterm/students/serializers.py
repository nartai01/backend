from rest_framework import serializers
from students.models import Student

class StudentSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(allow_null=False, allow_blank=False, min_length=5, max_length=100)

    def create(self, validated_data):
        student = Student(**validated_data)
        student.save()
        return student

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.save()
        return instance


class StudentSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(allow_null=False, allow_blank=False)
    surname = serializers.CharField(allow_null=False, allow_blank=False)
    year_of_study = serializers.IntegerField()

    def create(self, validated_data):
        product = Student(**validated_data)
        product.save()
        return product

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.price = validated_data.get('price', instance.price)
        instance.code = validated_data.get('code', instance.code)
        instance.category_id = validated_data.get('category_id', instance.category_id)
        instance.save()
        return instance








