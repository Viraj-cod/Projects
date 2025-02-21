from rest_framework.response import Response
from rest_framework.decorators import api_view,permission_classes
from rest_framework.views import APIView
from rest_framework import status
from Info.models import Watchlist,Review,platform
from Info.api.serializer import watlistserailizer,reviewserializer,platformserializer
from rest_framework import generics
#from django_filters.rest_framework import djangofilterBackend
#from rest_framework.permissions import IsAuthenticated
from Info.api.permissions import AdminorReadOnly,Reviewuserorreadonly
from Info.api.pagination import platformpagination

@api_view(['GET','POST'])
@permission_classes([AdminorReadOnly])
def watchlistview(request):
    if request.method == 'GET':
        obj = Watchlist.objects.all()
        ser = watlistserailizer(obj,many=True)
        return Response(ser.data)

    if request.method == 'POST':
        ser = watlistserailizer(data = request.data)
        if ser.is_valid():
            ser.save()
            return Response(ser.data)
        else:
            return Response(ser.errors)

@api_view(['GET','POST'])
@permission_classes([AdminorReadOnly])
def watchlistdetailview(request,pk):
    if request.method == 'GET':
        obj = Watchlist.objects.get(pk=pk)
        ser = watlistserailizer(obj)
        return Response(ser.data)

    if request.method == 'PUT':
        obj = Watchlist.objects.get(pk=pk)
        ser = watlistserailizer(obj,data = request.data)
        if ser.is_valid():
            ser.save()
            return Response(ser.data)
        else:
            return Response(ser.errors)
        
    if request.method == 'DELETE':
        obj = Watchlist.objects.get(pk=pk)
        obj.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class reviewsview(APIView):
    permission_classes = [AdminorReadOnly]
    def get(self,request):
        obj = Review.objects.all()
        ser = reviewserializer(obj,many=True)
        return Response(ser.data)

    def post(self,request):
        ser = reviewserializer(data = request.data)
        if ser.is_valid():
            ser.save()
            return Response(ser.data)
        else:
            return Response(ser.errors)

class reviewsdetailview(APIView):
    permission_classes = [AdminorReadOnly]

    def get(self,request,pk):
        obj = Review.objects.get(pk=pk)
        ser = reviewserializer(obj)
        return Response(ser.data)

    def put(self,request,pk):
        obj = Review.objects.get(pk=pk)
        ser = reviewserializer(obj,data = request.data)
        if ser.is_valid():
            ser.save()
            return Response(ser.data)
        else:
            return Response(ser.errors)
    
    def delete(self,request,pk):
        obj = Review.objects.get(pk=pk)
        obj.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
'''
class platformview(APIView):
    permission_classes = [AdminorReadOnly]

    def get(self,request):
        obj = platform.objects.all()
        ser = platformserializer(obj,many=True)
        return Response(ser.data)

    def post(self,request):
        ser = platformserializer(data = request.data)
        if ser.is_valid():
            ser.save()
            return Response(ser.data)
        else:
            return Response(ser.errors)
'''
class platformdetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [AdminorReadOnly]
    serializer_class = platformserializer
    queryset = platform.objects.all()

class platform(generics.ListCreateAPIView):
    serializer_class = platformserializer
    queryset = platform.objects.all()
    pagination_class = platformpagination
    permission_classes = [AdminorReadOnly]
    
    #filter_backends = [djangofilterBackend]
    #filterset_fields = ['content__names']
    #search_fields = ['content__names']
#http://127.0.0.1:8000/imdb/platform/?content__names=ABCD 
# filter backends works only with generic not on APIView

#filter finds the exact math and search find related data to query


'''
class YourModelListView(APIView):
    pagination_class = CustomPagination  # Set your pagination class

    def get(self, request):
        # Get the queryset
        queryset = YourModel.objects.all()
        
        # Apply pagination
        paginator = self.pagination_class()
        page = paginator.paginate_queryset(queryset, request)
        if page is not None:
            # Serialize the paginated data
            serializer = YourModelSerializer(page, many=True)
            return paginator.get_paginated_response(serializer.data)
        
        # If pagination is not applied, return all results
        serializer = YourModelSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

'''