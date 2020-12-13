# coding: utf-8
import json
from django.http.response import HttpResponse, JsonResponse
from django.contrib import auth
from commons.django_model_utils import get_or_none
from commons.django_views_utils import ajax_login_required
from core.service import log_svc, globalsettings_svc, url_service
from django.views.decorators.csrf import csrf_exempt
from django.utils.datastructures import MultiValueDictKeyError


def dapau(request):
    raise Exception("break on purpose")


@csrf_exempt
def login(request):
    username = request.POST["username"]
    password = request.POST["password"]
    user = auth.authenticate(username=username, password=password)
    user_dict = None
    if user is not None:
        if user.is_active:
            auth.login(request, user)
            log_svc.log_login(request.user)
            user_dict = _user2dict(user)
    return JsonResponse(user_dict, safe=False)


def logout(request):
    if request.method.lower() != "post":
        raise Exception("Logout only via post")
    if request.user.is_authenticated:
        log_svc.log_logout(request.user)
    auth.logout(request)
    return HttpResponse("{}", content_type="application/json")


def whoami(request):
    i_am = (
        {"user": _user2dict(request.user), "authenticated": True,}
        if request.user.is_authenticated
        else {"authenticated": False}
    )
    return JsonResponse(i_am)


def settings(request):
    le_settings = globalsettings_svc.list_settings()
    return JsonResponse(le_settings)


@ajax_login_required
def url(request):
    user = request.user.pk
    if request.method.lower() == "get":
        urls = url_service.list_urls(user)
        return JsonResponse(urls, safe=False)
    if request.method.lower() == "post":
        try:
            url = url_service.add_url(request.POST["url"], user)
            return JsonResponse(url, safe=False, status=201)
        except MultiValueDictKeyError:
            return JsonResponse({"message": "Bad request"}, status=400)


@ajax_login_required
def redirect_url(request, short_url):
    user = request.user.pk
    if request.method.lower() == "get" and short_url:
        import pdb

        pdb.set_trace()
        url = url_service.get_url(short_url)
        if url:
            return JsonResponse(url, safe=False)
        return JsonResponse({"message": "Not Found"}, status=404)
    return JsonResponse({"message": "Bad request"}, status=400)


def _user2dict(user):
    d = {
        "id": user.id,
        "name": user.get_full_name(),
        "username": user.username,
        "first_name": user.first_name,
        "last_name": user.last_name,
        "email": user.email,
        "permissions": {"ADMIN": user.is_superuser, "STAFF": user.is_staff,},
    }
    return d
