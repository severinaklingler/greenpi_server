from rest_framework import serializers

from api.models import Measurement

class MeasurementSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Measurement
        fields = ['when','sensor','tree_id','value']