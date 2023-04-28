from rest_framework import serializers
from ..models import Vote


class VoteCreateSerializer(serializers.ModelSerializer):
    score = serializers.IntegerField()

    class Meta:
        model = Vote
        fields = ['score']

    def validate(self, attrs):
        if attrs['score'] > 5 or attrs['score'] < 1:
            raise serializers.ValidationError('Score is not between 1 and 5')

        return super().validate(attrs)
