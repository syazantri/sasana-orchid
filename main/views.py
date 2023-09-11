from django.shortcuts import render

def show_main(request):
    # Define a list of product dictionaries
    items = [
        {
            'name': 'Anggrek Dendrobium Alien',
            'amount': 5,
            'price': 40000,
            'description': 'Kondisi dewasa siap bunga, jenis tanaman mini',
        },
        {
            'name': 'Anggrek Dendrobium Pure Glory "Dwarft"',
            'amount': 68,
            'price': 25000,
            'description': 'Anggrek ini merupakan anggrek jenis dendrobium dengan tipe yang mudah berbunga. Dari remaja sudah mulai spike dan belajar berbunga. Anggrek ini mempunyai bunga berwarna putih, bentuk bunga mirip phalaenopsis/anggrek bulan.',
        },
        {
            'name':'Anggrek Dendrobium Salaya Fancy',
            'amount': 138,
            'price': 15000,
            'description': 'Anggrek ini merupakan tipe anggrek yang mudah sekali berbunga, sedari kecil sudah banyak spike. Warna bunga pink dan putih cantik'
        },
        {
            'name':'Anggrek Dendrobium Pure Stripe',
            'amount': 101,
            'price': 13000,
            'description': 'Anggrek ini mudah berbunga. Warna bunga pink strip'
        }
    ]

    context = {
        'items': items,
    }

    return render(request, "main.html", context)
