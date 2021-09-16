from django.urls import path
from .views import CookieStandList, CookieStandDetail , CookieStandCreateView

urlpatterns = [
    path("/", CookieStandList.as_view(), name="cookie_list"),
    path("<int:pk>/", CookieStandDetail.as_view(), name="cookie_detail"),
    path("create/",CookieStandCreateView.as_view() , name="cookie_create" )
]



