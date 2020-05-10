from flask import Flask, request, jsonify
from flask_cors import CORS
import json

app = Flask(__name__)
CORS(app)

items = [
    {
        'description': 'Drake Sweatpants',
        'image': 'https://i.pinimg.com/236x/a4/45/eb/a445eb4e5562a94093fb7555be62446a--couch-drake.jpg',
        'itemId': 'd83ff143-9f8b-445a-8d8f-b9b8fe0f9f29',
        'price': 30,
    },
    {
        'description': 'Drake Sweatshirt',
        'image': 'https://bkstr.scene7.com/is/image/Bkstr/1623-CS1220-P2082781-Black',
        'itemId': '22e83b18-bf9e-4797-b859-6c3497e0da37',
        'price': 50
    }
]

customers = [
    {
        'customerId': 'd83ff143-9f8b-445a-8d8f-b9b8fe0f9f28',
        'email': 'jason.bradley@drake.edu',
        'firstName': 'Jason',
        'lastName': 'Bradley'
    }
]

carts = [
    {
        'cartId': '44ef41f4-485b-44d6-8635-7418e026be89',
        'customerId': 'd83ff143-9f8b-445a-8d8f-b9b8fe0f9f28'
    },
    {
        'cartId': '5581858f-a20e-4ada-9ccf-dd3e2cea0eb3',
        'customerId': 'd83ff143-9f8b-445a-8d8f-b9b8fe0f9f28'
    }
]

cartItems = [
    {
        'cartId': '44ef41f4-485b-44d6-8635-7418e026be89',
        'cartItemId': 'd83ff143-9f8b-445a-8d8f-b9b8fe0f9f30',
        'itemId': 'd83ff143-9f8b-445a-8d8f-b9b8fe0f9f29',
        'quantity': 2
    }
]


def getSpecificItem(actualItemId):
    for item in items:
        if item['itemId'] == actualItemId:
            return item

@app.route('/items')
def itemsReturn():
    return json.dumps(items)

@app.route('/items/<itemId>')
def itemIdReturn(itemId):
    return json.dumps(getSpecificItem(itemId))

@app.route('/customers')
def customersReturn():
    return json.dumps(customers)

@app.route('/customers/<actualCustomerId>/carts')
def customerCart(actualCustomerId):
    customerCarts = []
    for cart in carts:
        if cart['customerId'] == actualCustomerId:
            customerCarts.append(cart)
    return json.dumps(customerCarts)

@app.route('/carts/<actualCartId>/cart-items')
def cartItemReturns(actualCartId):
    actualCartItems = []
    for cartItem in cartItems:
        if cartItem['cartId'] == actualCartId:
            actualCartItems.append(cartItem)
    return json.dumps(actualCartItems)

@app.route('/cart-items', methods=['POST'])
def addCartItem():
    data = request.get_json()
    cartItems.append(data)
    return ''

@app.route('/cart-items/<actualCartItemId>', methods=["DELETE"])
def deleteCartItem(actualCartItemId):
    for cartItem in cartItems:
        if cartItem['cartItemId'] == actualCartItemId:
            cartItems.remove(cartItem)
            return ''
