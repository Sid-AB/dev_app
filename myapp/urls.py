from django.urls import path
from . import views
urlpatterns = [
    path('operation/<int:id_projet>/',views.app_view,name='app_view'),
    path('operation/add/<int:id_projet>/',views.add_op,name='add_op'),
    path('operation/update/',views.opr_update,name='opr_update'),
    path('projet/',views.proj_add,name='proj_add'),
    path('projet/update/',views.proj_update,name='proj_update')
    
]