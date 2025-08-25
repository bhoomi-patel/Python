# ------ normalize sales data to 0-1 range ------
import numpy as np
def normalize_sales_data(sales_data):
    sales = np.array(sales_data)
    # min-max normalization : (x - min) / (max - min)
    normalized = (sales - np.min(sales)) / (np.max(sales)-np.min(sales))
    return normalized , {
        'original_min' : np.min(sales),
        'original_max' : np.max(sales),
        'original_mean' : np.mean(sales)
    }

# Example usage
monthly_sales = [1200, 1500, 1700, 1300, 1600]
normalized_sales , stats = normalize_sales_data(monthly_sales)
print("Original sales :", monthly_sales)
print("Normalized Sales Data:", normalized_sales)
print("Stats : ",stats)