from core import views
from django.urls import path

urlpatterns = [
    path("api/dapau", views.dapau),
    path("api/login", views.login),
    path("api/logout", views.logout),
    path("api/whoami", views.whoami),
    path("api/settings", views.settings),
    path("api/url", views.url),
    path("api/redirect_url/<str:short_url>", views.redirect_url),
]
#     path('api/add_todo', views.add_todo),
#     path('api/list_todos', views.list_todos),
# ]
