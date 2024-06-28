import cv2 as cv
import os

prototxt_path = 'C:/Users/Admin/Documents/AIO---262-Trinh-Xd/Module1/Week4/model/MobileNetSSD_deploy.prototxt.txt'
weights_path = 'C:/Users/Admin/Documents/AIO---262-Trinh-Xd/Module1/Week4/model/MobileNetSSD_deploy.caffemodel'

if not os.path.exists(prototxt_path):
    raise FileNotFoundError(f"Prototxt file {prototxt_path} not found")

if not os.path.exists(weights_path):
    raise FileNotFoundError(f"Weights file {weights_path} not found")

net = cv.dnn.readNetFromCaffe(prototxt_path, weights_path)
image_path = 'path_to_your_image.jpg'
image = cv.imread(image_path)

if image is None:
    raise ValueError(f"Image {image_path} not found or could not be read")

# Preprocess the image
blob = cv.dnn.blobFromImage(image, 0.007843, (300, 300), 127.5)

# Set the blob as input to the network
net.setInput(blob)

# Perform a forward pass
output = net.forward()
for layer_name, layer_params in net.getLayerNames().items():
    print(f"Layer name: {layer_name}, params: {layer_params}")
