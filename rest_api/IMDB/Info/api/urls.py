from django.urls import path
from Info.api.view import watchlistview,reviewsview,platformdetail,watchlistdetailview,reviewsdetailview,platform

urlpatterns = [
    path('watchlist/',watchlistview),
    path('review/',reviewsview.as_view()),
    path('platform/',platform.as_view()),
    path('platform/<int:pk>',platformdetail.as_view()),
    path('review/<int:pk>',reviewsdetailview.as_view()),
    path('watchlist/<int:pk>',watchlistdetailview)
]
