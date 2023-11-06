from django.shortcuts import render

from django.shortcuts import render

def custom_404_middleware(get_response):
    def middleware(request):
        response = get_response(request)

        if response.status_code == 404:
            return render(request, 'shop/404.html', status=404)

        return response

    return middleware
