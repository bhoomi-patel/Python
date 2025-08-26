import numpy as np
import matplotlib.pyplot as plt

#-->METHOD 1 : pyplot interface
plt.plot([1, 2, 3, 4],[1,4,2,3])
plt.title("my first plot")
plt.show()

#-->METHOD 2 : object oriented interface
fig , ax = plt.subplots() # create a figure and an axes
ax.plot([1, 2, 3, 4],[1,4,2,3]) # plot on the axes
ax.set_title("my first plot") # add a title to the axes
plt.show() # display the figure

# ---> sample data
x=np.linspace(0,10,100)
y=np.sin(x)
# ===== Line plot ======
plt.figure(figsize=(10,6))
plt.plot(x,y,label='sin(x)',linewidth=2,color='blue')
plt.plot(x,np.cos(x),label='cos(x)',linewidth=2,color='red',linestyle='--')
plt.legend() # plotted objects that have a label and creates a legend box.
plt.title('Trigonometric Functions')
plt.xlabel('x')
plt.ylabel('y')
plt.grid(True)
plt.show()

# ===== Histogram =====
data = [1,2,2,3,3,3,4,4,4,4,5,5,5,5,5]
plt.hist(data,bins=5,color='blue',edgecolor='black')
plt.title("Histogram")
plt.show()

# ===== Scatter plot =====
x=np.random.rand(50)
y=np.random.rand(50)
plt.scatter(x,y,c=x+y,cmap='viridis',s=50) # s is size of points
plt.colorbar(label='x+y')
plt.title("Scatter Plot")
plt.show()

# ===== subplots =====
fig, axes = plt.subplots(1, 2, figsize=(10,4))
axes[0].plot(x, y, 'r-'); axes[0].set_title("Line")
axes[1].bar(['A','B','C'], [5,7,3], color='orange'); axes[1].set_title("Bar")
plt.tight_layout()
plt.show()

# ===== Bar plot =====
categories = ['A', 'B', 'C']
values = [5, 7, 3]
plt.bar(categories, values, color=['red', 'green', 'blue'])
plt.title("Bar Plot")
plt.xlabel("Categories")
plt.ylabel("Values")
plt.show()

