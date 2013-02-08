from settings import STATIC_URL
import re

class StaticUrlMiddleware(object):
    """
    Automatically prepends the sitewide STATIC_URL setting
    to HTML src or href attributes that point to the images, css, or js directories
    so we don't have to do it manually throughout all the templates
    """
    def process_response(self,request,response):
        if response['Content-Type'].split(';')[0] != 'text/html':
            return response
        content = response.content
        p = re.compile('(src|href)=("|\')/(images|css|js)/')
        response.content = p.sub(r'\1=\2' + STATIC_URL + r'\3/',content)
        return response
