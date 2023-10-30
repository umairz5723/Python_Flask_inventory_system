from flask import Flask, request, render_template
import products
from sql_connection import get_sql_connection

app = Flask(__name__)
app.json.sort_keys = False
connection = get_sql_connection()




@app.route('/', methods = ['GET'])
def get_products():
    cursor = connection.cursor()
    cursor.execute("SELECT product_id, product_company, product_name, product_weight FROM iventory_system.products;")
    data = cursor.fetchall()
    cursor.close()
    return render_template('./html/index.html', products = data)


@app.route('/addProduct', methods=['GET', 'POST'])
def add_product():
    if request.method == 'POST':
        name = request.form['name']
        company = request.form['company']
        product_type = request.form['type']
        weight = request.form['weight']
        current_stock = request.form['current_stock']
        threshold = request.form['threshold']
        
        cursor = connection.cursor()
        cursor.execute("INSERT INTO iventory_system.products (product_name, product_company, type, product_weight, product_current_stock, product_threshold) VALUES (%s, %s, %s, %s, %s, %s )", (name, company, product_type, weight, current_stock, threshold))
        connection.commit()

    return render_template('./html/add_product.html')


@app.route('/removeProduct', methods=['GET','POST'])
def remove_product():
    if request.method == 'POST':
        name = request.form['name']
        id = request.form['id']

        cursor = connection.cursor()
        cursor.execute("DELETE FROM iventory_system.products WHERE product_name = %s  AND product_id =%s", (name,id))
        connection.commit()
    return render_template('./html/remove_product.html')

@app.route('/order', methods = ['GET'])
def re_order():
    data = products.get_all_restock(connection)
    return render_template('./html/reorder.html', products = data)





if __name__ == "__main__":
    app.run(debug=True, port = 5000)
    print("Flask server running on port 5000")