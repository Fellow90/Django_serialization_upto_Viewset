from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns
from snippets import views

#working with viewset
from snippets.views import SnippetViewSet, UserViewSet
# from snippets.views import api_root
from rest_framework import renderers

#use router for viewset
from rest_framework.routers import DefaultRouter

# urlpatterns = [
#     #upto function based view
#     # path('snippets/',views.snippet_list),
#     # path('snippets/<int:pk>/',views.snippet_detail),

#     #for class based view,same for mixins generics and generics
#     path('snippets/',views.SnippetList.as_view()),
#     path('snippets/<int:pk>/',views.SnippetDetail.as_view()),
#     #for user related view
#     path('users/',views.UserList.as_view()),
#     path('users/<int:pk>/', views.UserDetail.as_view()),
#     #url for newly added view api_root
#     path('',views.api_root),
#     #add url pattern for snippet highlight
#     path('snippets/<int:pk>/highlight/',views.SnippetHighlight.as_view()),
# ]
# urlpatterns = format_suffix_patterns(urlpatterns)


# #API ENDPOINTS for hyperlinked api
# urlpatterns = format_suffix_patterns([
#     path('',views.api_root),
#     path('snippets/',views.SnippetList.as_view(),name = 'snippet-list'),
#     path('snippets/<int:pk>/',views.SnippetDetail.as_view(),name = 'snippet-detail'),
#     path('snippets/<int:pk>/highlight/',views.SnippetHighlight.as_view(),name = 'snippet-highlight'),
#     path('users/',views.UserList.as_view(),name = 'user-list'),
#     path('users/<int:pk>/',views.UserDetail.as_view(),name = 'user-detail'),
# ])







# ##applying the viewset in url
# snippet_list = SnippetViewSet.as_view({
#     'get':'list',
#     'post': 'create'
# })
# snippet_detail = SnippetViewSet.as_view({
#     'get':'retrieve',
#     'put' : 'update',
#     'patch' : 'partial_update',
#     'delete': 'destroy'
# })
# snippet_highlight = SnippetViewSet.as_view({
#     'get':'highlight'
# },
# renderer_classes = [renderers.StaticHTMLRenderer])
# user_list = UserViewSet.as_view({
#     'get':'list'
# })
# user_detail = UserViewSet.as_view({
#     'get':'retrieve'
# })



# urlpatterns = format_suffix_patterns([
#     path('',api_root),
#     path('snippets/',snippet_list,name = 'snippet-list'),
#     path('snippets/<int:pk>/',snippet_detail,name = 'snippet-detail'),
#     path('snippets/<int:pk>/highlight/',snippet_highlight,name = 'snippet-highlight'),
#     path('users/',user_list,name = 'user-list'),
#     path('users/<int:pk>/',user_detail,name = 'user-detail'),
# ])

#using viewset doesnot need to define url, we can use router object instead
router = DefaultRouter()
router.register(r'snippets',views.SnippetViewSet,basename='snippet')
router.register(r'users',views.UserViewSet,basename = 'user')

urlpatterns = [
    path('',include(router.urls)),
]