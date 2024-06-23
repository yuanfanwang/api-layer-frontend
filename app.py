from flask import Flask, request, jsonify
from flask_cors import CORS
import requests

app = Flask(__name__)
CORS(app)

@app.route('/api/products/<int:product_id>', methods=['GET'])
def get_product(product_id):
    response = requests.get(f'http://product-domain:5002/products/{product_id}')
    return jsonify(response.json())

@app.route('/api/buy', methods=['POST'])
def buy_product():
    data = request.get_json()
    product_id = data['productId']

    # 決済処理
    payment_response = requests.post('http://payment-domain:5003/payments', json={
        'user_id': 1,  # デモ用の固定ユーザーID
        'amount': 100,  # デモ用の固定金額
        'product_id': product_id
    })

    # 購入記録
    purchase_response = requests.post('http://purchase-domain:5004/purchases', json={
        'user_id': 1,  # デモ用の固定ユーザーID
        'product_id': product_id
    })

    return jsonify({'payment': payment_response.json(), 'purchase': purchase_response.json()})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5001)