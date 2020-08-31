from django.shortcuts import render, get_object_or_404, redirect
import urllib
# Create your views here.
def oauth(request):
    code = request.GET['code']
    print('code= ' + str(code))

    client_id = '13839c3b390207f7c0c7eaa789139e34'
    redirect_uri = 'http://127.0.0.1:8000/account/login/kakao/callback'
    access_token_request_uri = "https://kauth.kakao.com/oauth/token?grant_type=authorization_code&"

    access_token_request_uri += "client_id=" + client_id
    access_token_request_uri += "&redirect_uri=" + redirect_uri
    access_token_request_uri += "&code=" + code
    print(access_token_request_uri)

    access_token_request_uri_data = requests.get(access_token_request_uri)
    json_data = access_token_request_uri_data.json()
    access_token = json_data['access_token']
    print(access_token)

    user_profile_info_uri = "https://kapi.kakao.com/v2/user/me?access_token="
    user_profile_info_uri += str(access_token)
    print(user_profile_info_uri)

    user_profile_info_uri_data = requests.get(user_profile_info_uri)
    user_json_data = user_profile_info_uri_data.json()
    user_nickname = user_json_data['properties']['nickname']
    print(user_nickname)

    return redirect('index')

def kakao_login(request):
    login_request_uri = 'https://kauth.kakao.com/oauth/authorize?'
    client_id = '13839c3b390207f7c0c7eaa789139e34'
    redirect_uri = 'http://127.0.0.1:8000/account/login/kakao/callback'

    login_request_uri += 'client_id=' + client_id
    login_request_uri += '&redirect_uri=' + redirect_uri
    login_request_uri += '&response_type=code'

    return redirect(login_request_uri)