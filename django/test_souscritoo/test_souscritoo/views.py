from django.http import HttpResponse


def home(request):
    text = """<p><a href=https://www.souscritoo.com/>Lien vers Souscritoo</a></p>"""
    return HttpResponse(text)
