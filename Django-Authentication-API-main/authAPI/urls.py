from django.contrib import admin
from django.urls import path, include
from django.http import JsonResponse

# Optional welcome view at root URL
def home(request):
    return JsonResponse({'message': 'Welcome to the Django Auth API!'})

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home),  # Root welcome route
    path('api/user/', include('account.urls')),  # All user auth endpoints
]
