from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),

    # This includes your API routes
    path('api/', include('demand_forecast.api_urls')),  # ✅ Correct

    # Optional: if urls.py is used for web views or others
    # path('', include('demand_forecast.urls')),
]
