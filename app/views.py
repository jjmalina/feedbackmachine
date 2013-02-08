from django.shortcuts import render


def index(request):
    return render(request, 'index.html')

def demo(request):
    # demo = Demos.find(request.id)
    demo = dict(id=1)
    return render(request, 'demo.html', { 'demo': demo })
