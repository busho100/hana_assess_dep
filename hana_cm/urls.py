from django.urls import path
from . import views

app_name = 'hana_cm'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/',views.DetailView.as_view(), name='detail'),
    path('create/', views.CreateView.as_view(), name='create'),
    path('<int:pk>/update/', views.UpdateView.as_view(), name='update'),
    path('<int:pk>/delete/', views.DeleteView.as_view(), name='delete'),
    path('attributes/', views.AttributesIndexView.as_view(), name='attributes'),
    path('attributes/<int:pk>/',views.AttributesDetailView.as_view(), name='attributesdetail'),
    path('attributes/create/', views.AttributesCreateView.as_view(), name='attributescreate'),
    path('attributes/<int:pk>/update/', views.AttributesUpdateView.as_view(), name='attributesupdate'),
    path('attributes/<int:pk>/delete/', views.AttributesDeleteView.as_view(), name='attributesdelete'),
    path('attributes/<int:num>/overwrite/', views.overwrite, name='attributesoverwrite'),
    #path('k_create/', views.youkaigo_create.as_view(), name='kcreate'),
    # path('k_detail/<int:pk>/',views.youkaigo_DetailView.as_view(), name='kdetail'),
    # path('k_update/<int:pk>/', views.youkaigo_UpdateView.as_view(), name='kupdate'),
    # path('youkaigodo/', views.Youkaigodo_IndexView.as_view(), name='youkaigodo'),
    # path('k_delete/<int:pk>/', views.Youkaigodo_DeleteView.as_view(), name='kdelete'),
]