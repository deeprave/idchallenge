from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework import generics

from api.serializers import GenderSerializer, AgeSerializer, StateSerializer, RegionTypeSerializer, RegionSerializer, YearSerializer, StatisticSerializer
from api.models import Gender, Age, State, RegionType, Region, Year, Statistic


class GenderList(generics.ListCreateAPIView):
    
    def get_queryset(self):
        queryset = Gender.objects.all()        
        return queryset

    permission_classes = ( IsAuthenticatedOrReadOnly,)
    serializer_class = GenderSerializer

class GenderDetail(generics.RetrieveUpdateDestroyAPIView):
    
    def get_queryset(self):
        queryset = Gender.objects.all()        
        return queryset
    serializer_class = GenderSerializer
    permission_classes = ( IsAuthenticatedOrReadOnly,)



class AgeList(generics.ListCreateAPIView):
    
    def get_queryset(self):
        queryset = Age.objects.all()        
        return queryset

    permission_classes = ( IsAuthenticatedOrReadOnly,)
    serializer_class = AgeSerializer

class AgeDetail(generics.RetrieveUpdateDestroyAPIView):
    
    def get_queryset(self):
        queryset = Age.objects.all()        
        return queryset
    serializer_class = AgeSerializer
    permission_classes = ( IsAuthenticatedOrReadOnly,)



class StateList(generics.ListCreateAPIView):
    
    def get_queryset(self):
        queryset = State.objects.all()        
        return queryset

    permission_classes = ( IsAuthenticatedOrReadOnly,)
    serializer_class = StateSerializer

class StateDetail(generics.RetrieveUpdateDestroyAPIView):
    
    def get_queryset(self):
        queryset = State.objects.all()        
        return queryset
    serializer_class = StateSerializer
    permission_classes = ( IsAuthenticatedOrReadOnly,)



class RegionTypeList(generics.ListCreateAPIView):
    
    def get_queryset(self):
        queryset = RegionType.objects.all()        
        return queryset

    permission_classes = ( IsAuthenticatedOrReadOnly,)
    serializer_class = RegionTypeSerializer

class RegionTypeDetail(generics.RetrieveUpdateDestroyAPIView):
    
    def get_queryset(self):
        queryset = RegionType.objects.all()        
        return queryset
    serializer_class = RegionTypeSerializer
    permission_classes = ( IsAuthenticatedOrReadOnly,)



class RegionList(generics.ListCreateAPIView):
    
    def get_queryset(self):
        queryset = Region.objects.all()        
        return queryset

    permission_classes = ( IsAuthenticatedOrReadOnly,)
    serializer_class = RegionSerializer

class RegionDetail(generics.RetrieveUpdateDestroyAPIView):
    
    def get_queryset(self):
        queryset = Region.objects.all()        
        return queryset
    serializer_class = RegionSerializer
    permission_classes = ( IsAuthenticatedOrReadOnly,)



class YearList(generics.ListCreateAPIView):
    
    def get_queryset(self):
        queryset = Year.objects.all()        
        return queryset

    permission_classes = ( IsAuthenticatedOrReadOnly,)
    serializer_class = YearSerializer

class YearDetail(generics.RetrieveUpdateDestroyAPIView):
    
    def get_queryset(self):
        queryset = Year.objects.all()        
        return queryset
    serializer_class = YearSerializer
    permission_classes = ( IsAuthenticatedOrReadOnly,)



class StatisticList(generics.ListCreateAPIView):
    
    def get_queryset(self):
        queryset = Statistic.objects.all()        
        return queryset

    permission_classes = ( IsAuthenticatedOrReadOnly,)
    serializer_class = StatisticSerializer

class StatisticDetail(generics.RetrieveUpdateDestroyAPIView):
    
    def get_queryset(self):
        queryset = Statistic.objects.all()        
        return queryset
    serializer_class = StatisticSerializer
    permission_classes = ( IsAuthenticatedOrReadOnly,)

