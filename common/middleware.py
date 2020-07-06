from django.http import Http404

from themes.models import Themes


class ThemesMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # try:
        #     # user = request.user
        #     # theme = Themes.get_active_theme(user)
        #     setattr(request, 'theme', theme)
        # except Themes.DoesNotExist:
        #     raise Http404("No active theme found")

        response = self.get_response(request)
        return response


class CorsMiddleware(object):
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        response["Access-Control-Allow-Origin"] = "*"
        return response
