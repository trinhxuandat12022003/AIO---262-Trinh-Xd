'''
Problem 1: Xây dựng hàm tính disparity map của hai ảnh stereo đầu vào (ảnh bên trái (L) và
ảnh bên phải (R)) theo phương thức pixel-wise matching. Các bước tính toán trong phương
pháp này có thể được miêu tả qua các bước dưới đây:
1. Đọc ảnh chụp bên trái (left) và ảnh chụp bên phải (right) dưới dạng ảnh grayscale (ảnh
mức xám) đồng thời ép kiểu ảnh về np.float32.
2. Khởi tạo hai biến height, width có giá trị bằng chiều cao, chiều rộng của ảnh trái.
3. Khởi tạo một ma trận không - zero matrix (depth) với kích thước bằng height, width.
4. Với mỗi pixel tại vị trí (h, w) (duyệt từ trái qua phải, trên xuống dưới) thực hiện các bước
sau:
(a) Tính cost (L1 hoặc L2) giữa các cặp pixel left[h, w] và right[h, w - d] (trong đó
d ∈ [0, disparity_range]). Nếu (w - d) < 0 thì gán giá trị cost = max_cost (max_cost
= 255 nếu dùng L1 hoặc 255^2 nếu dùng L2).
(b) Với danh sách cost tính được, chọn giá trị d (doptimal) mà ở đó cho giá trị cost là nhỏ
nhất.
(c) Gán depth[h, w] = doptimal x scale. Trong đó, scale = 255 / disparity_range
(Ở Problem 01, các bạn gán mặc định giá trị scale = 16).
'''

import cv2
import numpy as np


def distance(x, y):
    return abs(x - y)


def l1_distance(x, y):
    return abs(x - y)


def l2_distance(x, y):
    return (x - y) ** 2


def pixel_wise_matching(left_img, right_img, disparity_range, save_result=True):
    # Read left, right images then convert to grayscale
    left = cv2.imread(left_img, 0)
    right = cv2.imread(right_img, 0)

    left = left.astype(np.float32)
    right = right.astype(np.float32)

    height, width = left.shape[:2]

    # Create blank disparity map
    depth = np.zeros((height, width), np.uint8)
    scale = 16
    max_value = 255

    for y in range(height):
        for x in range(width):
            # Find j where cost has minimum value
            disparity = 0
            cost_min = max_value

            for j in range(disparity_range):
                cost = max_value if (
                    x - j) < 0 else distance(int(left[y, x]), int(right[y, x - j]))

                if cost < cost_min:
                    cost_min = cost
                    disparity = j

            # Let depth at (y,x) = j (disparity)
            # Multiply by a scale factor for visualization purpose
            depth[y, x] = disparity * scale

    if save_result == True:
        print("Saving result...")
        # Save results
        cv2.imwrite(f'pixel_wise_l1.png', depth)
        cv2.imwrite(f'pixel_wise_l1_color.png',
                    cv2.applyColorMap(depth, cv2.COLORMAP_JET))

    print("Done")

    return depth


def pixel_wise_matching_l1(left_img, right_img, disparity_range, save_result=True):
    # Read left, right images then convert to grayscale
    left  = cv2.imread(left_img, 0)
    right = cv2.imread(right_img, 0)

    left  = left.astype(np.float32)
    right = right.astype(np.float32)

    height, width = left.shape[:2]

    # Create blank disparity map
    depth = np.zeros((height, width), np.uint8)
    scale = 16
    max_value = 255

    for y in range(height):
        for x in range(width):
            # Find j where cost has minimum value
            disparity = 0
            cost_min  = max_value

            for j in range(disparity_range):
                cost = max_value if (x - j) < 0 \
                                else l1_distance(int(left[y, x]), int(right[y, x - j]))

                if cost < cost_min:
                    cost_min  = cost
                    disparity = j

            # Let depth at (y, x) = j (disparity)
            # Multiply by a scale factor for visualization purpose
            depth[y, x] = disparity * scale

    if save_result == True:
        print('Saving result...')
        # Save results
        cv2.imwrite(f'pixel_wise_l1.png', depth)
        cv2.imwrite(f'pixel_wise_l1_color.png', cv2.applyColorMap(depth, cv2.COLORMAP_JET))

    print('Done.')

    return depth, cv2.applyColorMap(depth, cv2.COLORMAP_JET)


def pixel_wise_matching_l2(left_img, right_img, disparity_range, save_result=True):
    # Read left, right images then convert to grayscale
    left  = cv2.imread(left_img, 0)
    right = cv2.imread(right_img, 0)

    left  = left.astype(np.float32)
    right = right.astype(np.float32)

    height, width = left.shape[:2]

    # Create blank disparity map
    depth = np.zeros((height, width), np.uint8)
    scale = 16
    max_value = 255 ** 2

    for y in range(height):
        for x in range(width):
            # Find j where cost has minimum value
            disparity = 0
            cost_min  = max_value

            for j in range(disparity_range):
                cost = max_value if (x - j) < 0 else l2_distance(int(left[y, x]), int(right[y, x - j]))

                if cost < cost_min:
                    cost_min  = cost
                    disparity = j

            # Let depth at (y, x) = j (disparity)
            # Multiply by a scale factor for visualization purpose
            depth[y, x] = disparity * scale

    if save_result == True:
        print('Saving result...')
        # Save results
        cv2.imwrite(f'pixel_wise_l2.png', depth)
        cv2.imwrite(f'pixel_wise_l2_color.png', cv2.applyColorMap(depth, cv2.COLORMAP_JET))

    print('Done.')

    return depth

left_img_path = 'C:\\Users\\Admin\\Documents\\AIO---262-Trinh-Xd\\Module 2 project\\left.png'
right_img_path = 'C:\\Users\\Admin\\Documents\\AIO---262-Trinh-Xd\\Module 2 project\\left.png'
disparity_range = 64

depth = pixel_wise_matching_l2(
    left_img_path,
    right_img_path,
    disparity_range,
    save_result=True
)
cv2.imshow('color_map',cv2.applyColorMap(depth, cv2.COLORMAP_JET))

cv2.waitKey(0)