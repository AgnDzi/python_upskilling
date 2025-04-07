import requests

def get_category(user_id: int) -> str:
    api_url_products = 'https://dummyjson.com/products/category/'
    api_url_categories = "https://dummyjson.com/products/category-list"
    api_url_carts = f"https://dummyjson.com/carts/user/{user_id}"
    category_id = {}
    category_count = {}
    
    response_category = requests.get(api_url_categories)
    category_data = response_category.json()
    
    for category in category_data:
        response_prod = requests.get(f"{api_url_products}{category}")
        product_data = response_prod.json()

        for product in product_data['products']: 
            category_id[product['id']] = category

    response_carts = requests.get(api_url_carts)
    carts_by_user = response_carts.json()
                
    for cart in carts_by_user['carts']:
        for product in cart['products']:
            product_category = category_id[product['id']] 
            category_count[product_category] = category_count.get(product_category, 0) + product['quantity']
            
    sorted_count = sorted(category_count.items(), key=lambda x: x[1], reverse=True) 

    if len(sorted_count) > 0:
        return sorted_count[0][0]
    else:
        return 'none'


print(get_category(11))
