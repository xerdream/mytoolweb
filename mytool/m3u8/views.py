from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return render(request, "m3u8/index.html")


def test(request):
    try:
        test_str = request.POST["url"]
    except KeyError:
        return HttpResponse("未使用post,或无url字段")
    else:
        return HttpResponse(f"test_str:{test_str}")


def download(request):
    return render(request, "m3u8/download.html")
