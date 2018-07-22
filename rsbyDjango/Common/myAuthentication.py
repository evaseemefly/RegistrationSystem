# coding=utf-8
from rest_framework_jwt.settings import api_settings
from rest_framework_jwt.authentication import BaseJSONWebTokenAuthentication


class CookieAuthentication(BaseJSONWebTokenAuthentication):
    """自定义JWT认证，从cookie中获取认证信息"""

    def get_jwt_value(self, request):
        # print request.COOKIES
        return request.COOKIES.get(api_settings.JWT_AUTH_HEADER_PREFIX.upper(), '')

    # def authenticate_header(self, request):
    #     """
    #     注意这里：
    #     返回一个字符串作为`WWW-Authenticate`的值，http响应头中有`WWW-Authenticate`才会返回401.
    #     否则返回403.
    #     """
    #     return '{0} realm="{1}"'.format(api_settings.JWT_AUTH_HEADER_PREFIX, self.www_authenticate_realm)