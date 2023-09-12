from django.shortcuts import render

def show_main(request):
    context = {
        'name': 'Henry Soedibjo',
        'class': 'PBP A',
        'amount': '100',
        'description': 'henrysoed Investment Portofolio Inventory for individu task 2 PBP'
    }

    return render(request, "main.html", context)
