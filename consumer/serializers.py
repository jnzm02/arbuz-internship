from django.contrib.auth import get_user_model

from rest_framework import serializers


class ConsumerSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ['id', 'email', 'phone', 'name']
        extra_kwargs = {'password': {'write_only': True, 'min_length': 5}}

    def create(self, validated_data):
        return get_user_model().objects.create_consumer(**validated_data)

    def update(self, instance, validated_data):
        password = validated_data.pop('password', None)
        consumer = super().update(instance, validated_data)

        if password:
            consumer.set_password(password)
            consumer.save()

        return consumer
