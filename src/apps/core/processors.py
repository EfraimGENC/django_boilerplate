from django.conf import settings


def app_settings(request):
    return {
        "DEBUG": settings.DEBUG,
        "APP_VERSION": settings.APP_VERSION
    }
