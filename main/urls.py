from django.urls import path
from main.views import show_main, create_item, delete_item, show_xml, show_json, show_xml_by_id, show_json_by_id, register, login_user, logout_user, inc_amount, dec_amount  

app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'),
    path('create-item', create_item, name='create_item'),
    path('inc-amount/<int:item_id>/', inc_amount, name='inc_amount'),  
    path('dec-amount/<int:item_id>/', dec_amount, name='dec_amount'),  
    path('delete_item/<int:item_id>/', delete_item, name='delete_item'),
    path('xml/', show_xml, name='show_xml'), 
    path('json/', show_json, name='show_json'), 
    path('xml/<int:id>/', show_xml_by_id, name='show_xml_by_id'),
    path('json/<int:id>/', show_json_by_id, name='show_json_by_id'),
    path('register/', register, name='register'),
    path('login/', login_user, name='login_user'),
    path('logout/', logout_user, name='logout_user'),
]