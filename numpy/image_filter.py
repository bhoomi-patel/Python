# ---- create basic image filters 
import numpy as np 
def apply_image_filters(image):
    image = np.array(image)
    # 1. Blur filter
    blurred = np.zeros_like(image)
    for i in range(1,image.shape[0]-1):
        for j in range(1,image.shape[1]-1):
            # average the 3x3 neighborhood
            blurred[i,j] = np.mean(image[i-1:i+2, j-1:j+2])
    # 2. simple gradient
    edges = np.zeros_like(image)
    for i in range(1,image.shape[0]-1):
        for j in range(1,image.shape[1]-1):
            # gradient magnitude
            gx = image[i+1,j] - image[i-1,j] #Horizontal gradient
            gy= image[i,j+1] - image[i,j-1] #Vertical gradient
            edges[i,j] = np.sqrt(gx**2 + gy**2)
    return blurred , edges

# Test with simple image 
test_image = np.array([
    [10, 10, 10, 10, 10], # dark border
    [10, 50, 50, 50, 10], # medium square inside
    [10, 50,100, 50, 10], # bright center
    [10, 50, 50, 50, 10], # medium square 
    [10, 10, 10, 10, 10]  # dark border
])
blurred , edges = apply_image_filters(test_image)
print("Original Image:\n", test_image.shape)
print("Blur effect applied successfully.")
print("Blurred Image:\n", blurred)
print("Edge detection applied successfully.")
print("Edges Image:\n", edges)
