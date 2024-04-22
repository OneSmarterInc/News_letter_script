from django.utils.deprecation import MiddlewareMixin
from django.http import JsonResponse

class SignInRequiredMiddleware(MiddlewareMixin):  
    def process_request(self, request):
        if request.path == '/add_credentials' or request.path == '/get_credentials':
            if not request.session.get('user_signed_in', False):
                return JsonResponse({"detail": "Please sign in to add an article."}, status=401)