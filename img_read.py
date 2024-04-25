import cv2
print(cv2.__version__)

img=cv2.imread('data/kris.jpg',0)
cv2.imshow('Image', img)

# Wait for any key to be pressed indefinitely
cv2.waitKey(0)
# Close all OpenCV windows
cv2.destroyAllWindows()

#save new copys
cv2.imwrite('data/kris_copy.png',img)