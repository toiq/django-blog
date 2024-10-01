from django.urls import path

from blog import feeds, views

app_name = "blog"
urlpatterns = [
    path("", view=views.post_list, name="post_list"),
    # path("", view=views.PostListView.as_view(), name="post_list"),
    path("tag/<slug:tag_slug>/", view=views.post_list, name="post_list_by_tag"),
    path(
        "<int:year>/<int:month>/<int:day>/<slug:post>",
        view=views.post_detail,
        name="post_detail",
    ),
    path("<int:post_id>/share", views.post_share, name="post_share"),
    path("<int:post_id>/comment", views.post_comment, name="post_comment"),
    path("search/", views.post_search, name="post_search"),
    path("feed/", feeds.LatestPostsFeed(), name="post_feed"),
]
