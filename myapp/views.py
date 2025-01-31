from django.http import JsonResponse
from datetime import datetime, timezone

def home(request):
    current_date = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    return JsonResponse({"email": "charlesigboanugo033@gmail.com",
                         "current_datetime": current_date,
                         "github_url": "https://github.com/charlesigboanugo/Retriver-API"})
