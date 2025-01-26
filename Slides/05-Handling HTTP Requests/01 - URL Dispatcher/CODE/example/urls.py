from django.contrib import admin
from django.urls import include, path, register_converter, re_path
from app.views import *
from .converter import FourYearConverter

register_converter(converter=FourYearConverter, type_name="YYYY")

extra_patterns = [
    # default value in the view
    path("def/", defaultView, name="def"),
    path("def/<int:pk>/", defaultView, name="def"),
]

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", home, name="home"),
    path("room/<int:pk>/", room, name="home"),
    path("host/<int:pk>/<str:name>/", host, name="host"),
    # path("Year/<int:pk>/<str:name>/<YYYY:year>/",year,name="Year"),
    # regular expression paths
    re_path(
        r"^Year/(?P<pk>[0-9]{1})/(?P<year>[0-9]{4})/(?P<name>[a-z]{4})/$",
        year,
        name="year",
    ),
    re_path(r"^blog/page-([0-9]+/)?$", blog, name="blog"),
    re_path(
        r"^other_blog/(?:page-(?P<pagenumber>[0-9]+)/)?$", otherblog, name="otherblog"
    ),
    # default value in the view
    path("def/", defaultView, name="def"),
    path("def/<int:pk>/", defaultView, name="def"),
    # error handling
    path("error/", error, name="error"),
    # including others in the patterns
    path("app/", include("app.urls"), name="app"),
    
    # extra patterns
    path("extra/<ott>/",include(extra_patterns)),
    
    #extra args
    path("extr/",extr,{"foo":"bar"}),
    
    # def template renderer
    path("homie/",homeReturn,name="omie")

]
