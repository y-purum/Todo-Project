from django.shortcuts import redirect
import urllib


def kakao_login(request):
    app_rest_api_key = "81c03379fa2e69b0a3170c2e422e861a"
    redirect_uri = "http://127.0.0.1:8000/login/kakao/callback"
    return redirect(
        f"https://kauth.kakao.com/oauth/authorize?client_id={app_rest_api_key}&redirect_uri={redirect_uri}&response_type=code"
    )


def kakao_callback(request):                                                                  
    params = urllib.parse.urlencode(request.GET)                                      
    return redirect(f'http://127.0.0.1:8000/login/kakao/callback?{params}')