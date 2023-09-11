from django.shortcuts import render

def show_main(request):
    context = {
        'name': 'Syazantri Salsabila',
        'class': 'PBP D'
    }

    return render(request, "main.html", context)