from django.urls import path
from .views import CarsListView, CarsDetailView
from rest_framework_simplejwt import views as jwt_views

urlpatterns = [
    path('', CarsListView.as_view(), name='carss_list'),
    path('cars-detail/<int:pk>', CarsDetailView.as_view(), name='cars_detail'),
    path('token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
]

# {
#     "refresh": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTY1NDAxNzQ2MCwiaWF0IjoxNjUzOTMxMDYwLCJqdGkiOiJmMjM1MTFmMzE1YzM0YTViYjY1YzliNTk0OGYxYjkxNSIsInVzZXJfaWQiOjF9.fgDlt9TBXN2ty1ddd2dJk_HDPhaXqhBZQtKZrgHFfAQ",
#     "access": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjUzOTMxMzYwLCJpYXQiOjE2NTM5MzEwNjAsImp0aSI6ImJlZThmODRlZGE4MTQxZmE4ZDY0NDk4NjU5NjBlZDhlIiwidXNlcl9pZCI6MX0.-6_0wmPJAgTTkj0iuLJ76TpxXc8yCKHW0eAmUfj8Om4"
# }