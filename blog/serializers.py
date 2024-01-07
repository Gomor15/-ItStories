from rest_framework import serializers

from .models import Stories


class StoriesSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Stories
        fields = "__all__"
