from . import views
from django.urls import path

urlpatterns = [
    path('create/',views.createbook,name='create'),
    path('details/<int:pk>/',views.detailsView,name='details'),
    path('update/<int:pk>/',views.updateBook,name='update'),
    path('delete/<int:pk>/',views.deleteView,name='delete'),
    path('author/',views.Create_Author,name='author'),
    path('index/',views.index,name='index'),
    path('list/',views.ListBook,name='list'),
    path('search/',views.search_Book,name='search'),
    path('register/', views.Register_user, name='register'),
    path('',views.loginUser,name='login'),
    path('logout/',views.logOut,name='logout'),
    path('adminlogin/',views.admin_login,name='adminlogin')

]