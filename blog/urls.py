from django.urls import path

from blog import views

app_name = "blog"
urlpatterns = [
    path("", view=views.post_list, name="post_list"),
    path(
        "<int:year>/<int:month>/<int:day>/<slug:post>",
        view=views.post_detail,
        name="post_detail",
    ),
]
