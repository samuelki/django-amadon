from django.shortcuts import render, HttpResponse, redirect

def index(req):
    return render(req, 'amadon_app/index.html')

def process(req):
    if 'total_items' not in req.session:
        req.session['total_items'] = 0

    if 'total_cost' not in req.session:
        req.session['total_cost'] = 0

    price = {
        '01': '19.99', 
        '02': '29.99',
        '03': '4.99',
        '04': '49.99'
    }

    req.session['product_id'] = req.POST['product']
    req.session['product_price'] = price[req.POST['product']]
    req.session['product_quantity'] = req.POST['quantity']
    req.session['order_total'] = float(price[req.POST['product']]) * int(req.POST['quantity'])

    req.session['total_items'] += int(req.POST['quantity'])
    req.session['total_cost'] += float(price[req.POST['product']]) * int(req.POST['quantity'])

    return redirect('/amadon/checkout')

def checkout(req):
    return render(req, 'amadon_app/checkout.html')

def goback(req):
    req.session.pop('product_id')
    req.session.pop('product_price')
    req.session.pop('product_quantity')
    req.session.pop('order_total')

    return redirect('/')