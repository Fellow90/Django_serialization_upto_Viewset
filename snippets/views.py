from django.shortcuts import render
#normal function
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework import status

#function-based api_view
from rest_framework.decorators import api_view

#class based api view
from rest_framework.views import APIView
from django.http import Http404

#mixin and generic
from rest_framework import mixins
from rest_framework import generics #for optimized code

## for authentication of user related access
from django.contrib.auth.models import User

## for permission
from rest_framework import permissions
 
from snippets.models import Snippet
from snippets.serializers import SnippetSerializer , UserSerializer

from snippets.permissions import IsOwneOrReadOnly


#for relationship and hyperlink api view
from rest_framework.reverse import reverse

#for rendering (in html in our context)
from rest_framework import renderers

#using viewset in order to refactor list and detail view in one
from rest_framework import viewsets
from rest_framework.decorators import action

# ## using normal function
# @csrf_exempt
# def snippet_list(request):
#     if request.method == 'GET':
#         snippets = Snippet.objects.all()
#         serializer = SnippetSerializer(snippets, many = True)
#         return JsonResponse(serializer.data,safe=False)
#     elif request.method == 'POST':        
#         data = JSONParser().parse(request)
#         serializer = SnippetSerializer(data=data)
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data, status = 201)
#         return JsonResponse(serializer.errors, status = 400)
    
# @csrf_exempt
# def snippet_detail(request,pk):
#     try:
#         snippet = Snippet.objects.get(pk=pk)
#     except Snippet.DoesNotExist:
#         return HttpResponse(status = 404)
    
#     if request.method == 'GET':
#         serializer = SnippetSerializer(snippet)
#         return JsonResponse(serializer.data)
    
#     elif request.method == 'PUT':
#         data = JSONParser().parse(request)
#         serializer = SnippetSerializer(snippet,data=data)
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data)
#         return JsonResponse(serializer.errors,status = 400)
    
#     elif request.method == 'DELETE':
#         snippet.delete()
#         return HttpResponse(204)


# ### using function based API VIEW
## uncomment the REST_FRAMEWORK field in settings to disable the browsable api.
# @api_view(['GET','POST'])
# def snippet_list(request,format = None ):
#     if request.method == 'GET':
#         snippets = Snippet.objects.all()
#         serializer = SnippetSerializer(snippets, many = True)
#         return Response(serializer.data,status=status.HTTP_200_OK)


    
#     elif request.method == 'POST':
#         serializer = SnippetSerializer(data=request.data,many = True)
#         if serializer.is_valid():
#             serializer.save()
            
#             return Response(status=status.HTTP_201_CREATED)
#         return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
# @api_view(['GET','PUT','PATCH','DELETE'])
# def snippet_detail(request,pk,format = None ):
#     try:
#         snippet = Snippet.objects.get(id=pk)
#     except Snippet.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)
    
#     if request.method == 'GET':
#         serializer = SnippetSerializer(snippet)
#         return Response(serializer.data,status=status.HTTP_200_OK)
    
#     if request.method == 'PUT':
#         serializer = SnippetSerializer(snippet,data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
#     if request.method == 'PATCH':
#         serializer = SnippetSerializer(snippet,data=request.data,  partial = True)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
#     if request.method == 'DELETE':
#         snippet.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)


### USING CLASS BASED API VIEW
# class SnippetList(APIView):
#     def get(self,request,format = None):
#         snippets = Snippet.objects.all()
#         serializer = SnippetSerializer(snippets,many=True)
#         return Response(serializer.data,status=status.HTTP_200_OK)
    
#     def post(self,request,format = None):
#         serializer = SnippetSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(status=status.HTTP_201_CREATED)
#         return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
# class SnippetDetail(APIView):
#     def get_object(self,pk):
#         try:
#             return Snippet.objects.get(pk=pk)
#         except Snippet.DoesNotExist:
#             return Http404
        
#     def get(self,request,pk,format=None):
#         snippet = self.get_object(pk)
#         serializer = SnippetSerializer(snippet)
#         return Response(serializer.data,status=status.HTTP_200_OK)
    
#     def put(self,request,pk,format = None):
#         snippet = self.get_object(pk)
#         serializer = SnippetSerializer(snippet,data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(status=status.HTTP_201_CREATED)
#         return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
#     def patch(self,request,pk,format = None):
#         snippet = self.get_object(pk)
#         serializer = SnippetSerializer(snippet,data=request.data,partial = True)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(status=status.HTTP_200_OK)
#         return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
#     def delete(self,request,pk,format = None):
#         snippet = self.get_object(pk=pk)
#         snippet.delete()
#         return Response(status=status.HTTP_404_NOT_FOUND)


##using mixin and generic
# class SnippetList(mixins.ListModelMixin,mixins.CreateModelMixin,generics.GenericAPIView):
#     queryset = Snippet.objects.all()
#     serializer_class = SnippetSerializer

#     def get(self,request,*args,**kwargs):
#         return  self.list(request,*args,**kwargs)
    
#     def post(self, request, *args, **kwargs):
#         return self.create(request, *args, **kwargs)
    
# class SnippetDetail(mixins.RetrieveModelMixin,mixins.UpdateModelMixin,mixins.DestroyModelMixin, generics.GenericAPIView):
#     queryset = Snippet.objects.all()
#     serializer_class = SnippetSerializer

#     def get(self, request, *args, **kwargs):
#         return self.retrieve(request, *args, **kwargs)
    
#     def put(self, request, *args, **kwargs):
#         return self.update(request, *args, **kwargs)
    
#     def delete(self, request, *args, **kwargs):
#         return super().destroy(request, *args, **kwargs)
    



# ## the optimized code that use listapiview and retrieveupdatedestroyapiview of generics
# class SnippetList(generics.ListCreateAPIView):
#     queryset = Snippet.objects.all()
#     serializer_class = SnippetSerializer
#     #add this class to ensure authenticated request get read write whereas unauthenticated get read only access
#     permission_classes = [permissions.IsAuthenticatedOrReadOnly,IsOwneOrReadOnly]

#     # #to send user along with snippet in create() method
#     def perform_create(self, serializer):
#         serializer.save(owner = self.request.user)
    
# class SnippetDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Snippet.objects.all()
#     serializer_class = SnippetSerializer
#     permission_classes = [permissions.IsAuthenticatedOrReadOnly,IsOwneOrReadOnly]


# ## user related view
# class UserList(generics.ListAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer

# class UserDetail(generics.RetrieveAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer




# # ##for hyperlinking relationship
# @api_view(['GET'])
# def api_root(request,format = None):
#     return Response(
#         {
#             'users':reverse('user-list',request = request,format=format),
#             'snippets':reverse('snippet-list',request = request,format=format),
#         }
#     )

# class SnippetHighlight(generics.GenericAPIView):
#     queryset = Snippet.objects.all()
#     renderer_classes = [renderers.StaticHTMLRenderer]

#     def get(self, request, *args, **kwargs):
#         snippet = self.get_object()
#         return Response(snippet.highlighted)




# # ##using the concept of viewset
class UserViewSet(viewsets.ReadOnlyModelViewSet):
    '''for list and retrieve actions'''
    queryset = User.objects.all()
    serializer_class = UserSerializer

class SnippetViewSet(viewsets.ModelViewSet):
    '''for list, create, retrieve, update and destroy'''
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwneOrReadOnly]

    
    # def perform_create(self, serializer):
    #     serializer.save(owner = self.request.user)


### SIMPLY ADDING is_deleted attribute in model and then running all below code will help you out performing soft delete and restoring the deleting data back.
    def list(self, request, *args, **kwargs):
        snippets = Snippet.objects.filter(is_deleted=False)
        serializer = SnippetSerializer(snippets,many = True,context = {'request':request})
        return Response(serializer.data,status=status.HTTP_200_OK)

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        if instance.is_deleted:
            return Response({'msg':'Record not found'}, status=status.HTTP_400_BAD_REQUEST)
        serializer = self.get_serializer(instance)
        return Response(serializer.data,status=status.HTTP_200_OK)
    
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.is_deleted = True
        instance.save()
        return Response({'msg':'Record moved to trash'}, status=status.HTTP_204_NO_CONTENT)
    
    @action(detail=True, renderer_classes = [renderers.StaticHTMLRenderer])
    def highlight(self,request,*args,**kwargs):
        snippet = self.get_object()
        return Response(snippet.highlighted)
    
    @action(detail=True,methods=['get'])
    def restore(self,request, *args, **kwargs):
        instance = self.get_object()
        if instance.is_deleted:
            instance.is_deleted = False
            instance.save()
            return Response({'msg':"Record restored successfully"}, status=status.HTTP_200_OK)
        return Response({'msg':'Record not found on trash'},status=status.HTTP_400_BAD_REQUEST)
    

    

    
    
