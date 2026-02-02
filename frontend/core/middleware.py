from django.http import JsonResponse, response
import jwt

from frontend.frontend import settings

class GatewayAuthMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        self.public_paths = ["/auth/login/", "/auth/signup/", "/static/"]

    def __call__(self, request, *args, **kwds):
        path = request.path
        method = request.method
        if any(path.startswith(p) for p in self.public_paths):
            return self.get_response(request)
        
        token = request.session.get('auth_token')

        if not token:
                return JsonResponse({'detail': 'Authentication required'}, status=401)
        
        try:
            payload = jwt.decode(
                  token, settings.JWT_PUBLIC_KEY,
                  algorithms=["RS256"],
            )
        except jwt.ExpiredSignatureError:
            return JsonResponse({"detail": "Token expired"}, status=401)
        except jwt.InvalidTokenError:
            return JsonResponse({"detail": "Invalid token"}, status=401)

        request.user_id = payload.get('user_id')
        request.user_role = payload.get('role')

        request.META["HTTP_X_USER_ID"] = str(request.user_id)
        request.META["HTTP_X_USER_ROLE"] = request.user_role

        return self.get_response(request)