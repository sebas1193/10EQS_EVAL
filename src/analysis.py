import matplotlib.pyplot as plt

def plot_inventory_kpis(out_of_stock_products, restock_needed_products):
    """
    Plot a bar chart showing inventory KPIs for products that are out of stock 
    and those that need restocking.

    Parameters:
    - out_of_stock_products (list): A list containing out-of-stock products.
    - restock_needed_products (list): A list containing products that need restocking.

    The function creates a bar chart with two categories: 'Out of Stock' and 
    'Restocking Needed', displaying the number of products in each category.
    """
    plt.close('all')

    plt.figure(figsize=(8, 6))

    categories = ['Out of Stock', 'Restocking Needed']
    values = [len(out_of_stock_products), len(restock_needed_products)]
    colors = ['#FF4C4C', '#FFA500']

    bars = plt.bar(categories, values, color=colors, edgecolor='black', alpha=0.8)

    plt.title('Product Inventory KPIs', fontsize=16, fontweight='bold')
    plt.xlabel('Categories', fontsize=14)
    plt.ylabel('Number of Products', fontsize=14)

    for bar in bars:
        height = bar.get_height()
        plt.text(bar.get_x() + bar.get_width() / 2, height + 0.1, f'{height}', 
                 ha='center', va='bottom', fontsize=12, fontweight='bold', color='black')

    plt.grid(axis='y', linestyle='--', alpha=0.7)

    plt.ylim(0, max(values) + 1)

    # show plot
    plt.tight_layout()
    plt.show()
