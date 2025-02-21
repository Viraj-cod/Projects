from Info.models import Watchlist,Review,platform

from rest_framework import serializers

class reviewserializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ['id','rating','description','movie']

class watlistserailizer(serializers.ModelSerializer):
    review = reviewserializer(many=True,read_only = True)
    class Meta:
        model = Watchlist
        fields = ['id','name','description','date','review']

class platformserializer(serializers.ModelSerializer):
    content = serializers.StringRelatedField(many = True,read_only = True)
    class Meta:
        model = platform
        fields = ['id','name','content','url','description']


