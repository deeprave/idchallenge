from rest_framework.serializers import ModelSerializer
from api.models import Gender, Age, State, RegionType, Region, Year, Statistic


class GenderSerializer(ModelSerializer):

    class Meta:
        model = Gender
        fields = '__all__'


class AgeSerializer(ModelSerializer):

    class Meta:
        model = Age
        fields = '__all__'


class StateSerializer(ModelSerializer):

    class Meta:
        model = State
        fields = '__all__'


class RegionTypeSerializer(ModelSerializer):

    class Meta:
        model = RegionType
        fields = '__all__'


class RegionSerializer(ModelSerializer):

    class Meta:
        model = Region
        fields = '__all__'


class YearSerializer(ModelSerializer):

    class Meta:
        model = Year
        fields = '__all__'


class StatisticSerializer(ModelSerializer):

    class Meta:
        model = Statistic
        fields = '__all__'
