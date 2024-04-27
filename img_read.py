import cv2

# Read the image
img = cv2.imread("data/kris.jpg",1)

# Construct Gaussian pyramid
G = img.copy()
gp = [G]
for i in range(6):
    G = cv2.pyrDown(G)
    gp.append(G)

# Upsample the last level of Gaussian pyramid
GE = cv2.pyrUp(gp[5])

# Subtract the upsampled image from the next level of Gaussian pyramid
L = cv2.subtract(gp[4], GE)

# Display the original image
cv2.imshow('Original Image', img)

# Display the upsampled image
cv2.imshow('Upsampled Image', GE)

# Display the Laplacian image
cv2.imshow('Laplacian Image', L)

cv2.waitKey(0) & 0xFF
cv2.destroyAllWindows()
