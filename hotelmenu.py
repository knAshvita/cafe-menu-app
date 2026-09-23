import os
from dotenv import load_dotenv
from flask import Flask, jsonify, request, send_from_directory
from openai import OpenAI

load_dotenv()

app = Flask(__name__, static_folder='.', static_url_path='')

# ----------------- API CREDENTIALS -----------------
# Only fetch from .env, do not write secret keys here
API_KEY = os.environ.get("OPENAI_API_KEY")
BASE_URL = os.environ.get("OPENAI_BASE_URL")
MODEL_NAME = os.environ.get("MODEL_NAME", "gpt-4o-mini-tts")

client = OpenAI(
    api_key=API_KEY,
    base_url=BASE_URL
)
# ---------------------------------------------------

# Master menu data with prices & attributes for frontend rendering
menu = {
    'Pizza':  {'price': 160, 'type': 'food',     'emoji': '🍕', 'desc': 'Crispy stone-baked with mozzarella & herbs'},
    'Pasta':  {'price': 100, 'type': 'food',     'emoji': '🍝', 'desc': 'Creamy penne tossed in rich parmesan sauce'},
    'Burger': {'price': 80,  'type': 'food',     'emoji': '🍔', 'desc': 'Grilled spiced patty with fresh veggies'},
    'Salad':  {'price': 85,  'type': 'food',     'emoji': '🥗', 'desc': 'Garden fresh greens with honey vinaigrette'},
    'Coffee': {'price': 55,  'type': 'beverage', 'emoji': '☕', 'desc': 'Freshly brewed aromatic espresso roast'},
    'Tea':    {'price': 45,  'type': 'beverage', 'emoji': '🍵', 'desc': 'Classic spiced masala chai blend'},
}

# 1. Route: Serve index.html
@app.route('/')
def home():
    return send_from_directory('.', 'index.html')

# 2. Route: Send menu catalogue to frontend
@app.route('/api/menu', methods=['GET'])
def get_menu():
    menu_list = [{'id': k.lower(), 'name': k, **v} for k, v in menu.items()]
    return jsonify(menu_list)

# 3. Route: AI Barista Pairing Recommendation
@app.route('/api/recommend', methods=['POST'])
def recommend():
    data = request.get_json() or {}
    cart_items = data.get('items', [])

    # Filter out items already in the customer's tray
    remaining_items = [k for k in menu.keys() if k not in cart_items]
    if not remaining_items:
        remaining_items = list(menu.keys())

    prompt = (
        f"The customer ordered: {cart_items}. "
        f"From this list of available menu items: {remaining_items}, pick the single BEST complementary item to recommend. "
        f"Respond ONLY with the exact item name from the list, nothing else."
    )

    suggested_item = remaining_items[0]
    try:
        response = client.chat.completions.create(
            model=MODEL_NAME,
            messages=[
                {"role": "system", "content": "You are a cafe recommendation bot. Respond with only a single item name from the available menu."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.3,
            max_tokens=10
        )
        rec = response.choices[0].message.content.strip().title()
        for valid_item in menu.keys():
            if valid_item.lower() in rec.lower():
                suggested_item = valid_item
                break
    except Exception as e:
        print(f"AI recommendation fallback triggered: {e}")

    return jsonify({
        'item': suggested_item,
        'price': menu[suggested_item]['price'],
        'emoji': menu[suggested_item]['emoji']
    })

# 4. Route: Validate order and compute bill
@app.route('/api/order', methods=['POST'])
def place_order():
    data = request.get_json() or {}
    cart_items = data.get('cart', {})
    customer = data.get('customer', 'Walk-in Guest')

    subtotal = 0
    verified_items = []

    for name, item in cart_items.items():
        qty = item.get('qty', 0)
        if name in menu and qty > 0:
            price = menu[name]['price']
            line_total = price * qty
            subtotal += line_total
            verified_items.append({
                'name': name,
                'price': price,
                'qty': qty,
                'line_total': line_total
            })

    tax = round(subtotal * 0.05)
    grand_total = subtotal + tax

    return jsonify({
        'status': 'confirmed',
        'customer': customer,
        'items': verified_items,
        'subtotal': subtotal,
        'tax': tax,
        'grand_total': grand_total
    })

if __name__ == '__main__':
    print("🚀 Server running at http://127.0.0.1:5000")
    app.run(debug=True, port=5000)