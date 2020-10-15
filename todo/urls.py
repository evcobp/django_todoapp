from django.urls import path
from todo import views


urlpatterns = [
###homepage###
path('',views.index, name="todo"),
###give id numberitem_id or item_id = i.id###
path('del/<int:item_id>', views.remove, name="del")
]