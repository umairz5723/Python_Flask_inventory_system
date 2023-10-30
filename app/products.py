from sql_connection import get_sql_connection

def get_all_products(connection):
    
    cursor = connection.cursor()
    query = ("SELECT product_id, product_name, product_company, product_current_stock, product_image FROM iventory_system.products;")
    cursor.execute(query)
    
    response = []

    for (id, company, name, stock, image) in cursor:
        response.append(
            {
                'Name ': name,
                'Company': company,
                'ID': id,
                'Current Stock' : stock,
                'Image:': image
            }
        )
    print(response)
    return response


def get_all_restock(connection):
    
    cursor = connection.cursor()
    cursor.execute("SELECT product_id, product_name, product_company, product_weight, product_current_stock, product_threshold FROM iventory_system.products WHERE product_current_stock <= product_threshold;;")
    data = cursor.fetchall()
    cursor.close()
    
    return data


def delete_product(connection):
    cursor = connection.cursor()
    query = ("DELETE FROM iventory.products WHERE product_name=" + str(prod_name) + "AND product_id=" + prod_id )
    cursor.execute(query)
    connection.commit()
    return prod_id