'''
a Resize các ảnh đâu vào cùng kích thước
'''
import numpy as np
import cv2

bg1_image = cv2.imread(
    'Module 2\\Week 02\\Exercise04_Data\\GreenBackground.png', 1)
bg1_image = cv2.resize(bg1_image, (678, 381))

ob_image = cv2.imread('Module 2\\Week 02\\Exercise04_Data\\Object.png', 1)
ob_image = cv2.resize(ob_image, (678, 381))

bg2_image = cv2.imread(
    'Module 2\\Week 02\\Exercise04_Data\\NewBackground.jpg', 1)
bg2_image = cv2.resize(bg2_image, (678, 381))


'''
b Xây dựng hàm compute_difference()
'''


def compute_difference(bg_img, input_img):
    difference_three_channel = cv2.absdiff(bg_img, input_img)
    difference_single_channel = np.sum(difference_three_channel, axis=2) / 3.0
    difference_single_channel = difference_single_channel.astype('uint8')

    return difference_single_channel


difference_single_channel = compute_difference(bg1_image, ob_image)
cv2.imshow('Difference between pic', difference_single_channel)
cv2.waitKey(0)

'''
c Xây dựng hàm compute_binary_mask()
'''


def compute_binary_mask(difference_single_channel):
    difference_binary = np.where(difference_single_channel >= 15, 255, 0)
    difference_binary = np.stack((difference_binary,)*3, axis=-1)
    difference_binary = difference_binary.astype('uint8')
    return difference_binary


binary_mask = compute_binary_mask(difference_single_channel)
cv2.imshow('binary mask', binary_mask)
cv2.waitKey(0)

'''
d Xây dựng hàm replace_background()
'''


def replace_background(bg1_image, bg2_image, ob_image):
    difference_single_channel = compute_difference(bg1_image, ob_image)
    binary_mask = compute_binary_mask(difference_single_channel)
    output = np.where(binary_mask == 255, ob_image, bg2_image)
    return output


output = replace_background(bg1_image, bg2_image, ob_image)
cv2.imshow('Image after replacement', output)
cv2.waitKey(0)
