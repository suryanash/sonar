from django.conf.urls import url
from api import views

urlpatterns = [
	url(r'^api/price_data/$', views.PriceDataList.as_view()),
]