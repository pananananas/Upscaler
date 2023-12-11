import matplotlib.pyplot as plt
import numpy as np
# Adjusting the colormap to 'coolwarm' and removing the color scale

# Create sample data
x = np.arange(0, 5)
y = np.arange(0, 5)
x, y = np.meshgrid(x, y)
z = np.sin(x)**2 + np.cos(y)**2

# Setup interpolation grid
xnew = np.linspace(0, 4, 100)
ynew = np.linspace(0, 4, 100)
xnew, ynew = np.meshgrid(xnew, ynew)

# Nearest neighbor interpolation
z_nearest = griddata((x.flatten(), y.flatten()), z.flatten(), (xnew, ynew), method='nearest')

# Bilinear interpolation
z_linear = griddata((x.flatten(), y.flatten()), z.flatten(), (xnew, ynew), method='linear')

# Bicubic interpolation - we can use 'cubic' for 2D interpolation in griddata
z_cubic = griddata((x.flatten(), y.flatten()), z.flatten(), (xnew, ynew), method='cubic')

# Plotting without the color scale and changing colormap to 'coolwarm'
fig, axs = plt.subplots(1, 3, figsize=(18, 6), sharey=True)

# Nearest Neighbor
axs[0].imshow(z_nearest, interpolation='nearest', extent=(0, 4, 0, 4), cmap='coolwarm')
axs[0].set_title('Nearest Neighbor')
axs[0].axis('off')  # Remove the axis

# Bilinear
axs[1].imshow(z_linear, interpolation='bilinear', extent=(0, 4, 0, 4), cmap='coolwarm')
axs[1].set_title('Bilinear')
axs[1].axis('off')  # Remove the axis

# Bicubic
axs[2].imshow(z_cubic, interpolation='bicubic', extent=(0, 4, 0, 4), cmap='coolwarm')
axs[2].set_title('Bicubic')
axs[2].axis('off')  # Remove the axis

plt.tight_layout()
plt.show()
