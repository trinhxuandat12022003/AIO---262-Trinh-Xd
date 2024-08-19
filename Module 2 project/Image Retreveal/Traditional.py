import os
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt

#GET DATA
ROOT = 'data'
CLASS_NAME = sorted(list(os.listdir(f'C:\\Users\\Admin\\Documents\\AIO---262-Trinh-Xd\\Module 2 project\\Image Retreveal\\{ROOT}\\train')))

def read_image_from_path(path, size):
    im = Image.open(path).convert('RGB').resize(size)
    return np.array(im)

def folder_to_images(folder, size):
    list_dir = [folder + '/' + name for name in os.listdir(folder)]
    images_np = np.zeros(shape=(len(list_dir), *size, 3))
    images_path = []
    for i, path in enumerate(list_dir):
        images_np[i] = read_image_from_path(path, size)
        images_path.append(path)
    images_path = np.array(images_path)
    return images_np, images_path

def plot_results(querquery_pathy, ls_path_score, reverse):
    fig = plt.figure(figsize=(15, 9))
    fig.add_subplot(2, 3, 1)
    plt.imshow(read_image_from_path(querquery_pathy, size=(448,448)))
    plt.title(f"Query Image: {os.path.basename(querquery_pathy)}", fontsize=16)
    plt.axis("off")
    for i, path in enumerate(sorted(ls_path_score, key=lambda x : x[1], reverse=reverse)[:5], 2):
        fig.add_subplot(2, 3, i)
        plt.imshow(read_image_from_path(path[0], size=(448,448)))
        plt.title(f"Top {i-1}: {os.path.basename(path[0])}", fontsize=16)
        plt.axis("off")
    plt.show()

# Absolute Difference

def absolute_difference(query, data):
    axis_batch_size = tuple(range(1,len(data.shape)))
    return np.sum(np.abs(data - query), axis=axis_batch_size)

def get_l1_score(root_img_path, query_path, size):
    query = read_image_from_path(query_path, size)
    ls_path_score = []
    for folder in os.listdir(root_img_path):
        if folder in CLASS_NAME:
            path = root_img_path + folder
            images_np, images_path = folder_to_images(path, size) # mang numpy nhieu anh, paths
            rates = absolute_difference(query, images_np)
            ls_path_score.extend(list(zip(images_path, rates)))
    return query, ls_path_score

root_img_path = f"C:\\Users\\Admin\Documents\\AIO---262-Trinh-Xd\\Module 2 project\\Image Retreveal\\{ROOT}\\train\\"
query_path = f"C:\\Users\\Admin\\Documents\\AIO---262-Trinh-Xd\\Module 2 project\\Image Retreveal\\{ROOT}\\test\\African_crocodile\\n01697457_18534.JPEG"
size = (448, 448)
query, ls_path_score = get_l1_score(root_img_path, query_path, size)
# plot_results(query_path, ls_path_score, reverse=False)

# Mean Square Difference

def mean_square_difference(query, data):
    axis_batch_size = tuple(range(1,len(data.shape)))
    return np.mean((data - query)**2, axis=axis_batch_size)

def get_l2_score(root_img_path, query_path, size):
    query = read_image_from_path(query_path, size)
    ls_path_score = []
    for folder in os.listdir(root_img_path):
        if folder in CLASS_NAME:
            path = root_img_path + folder
            images_np, images_path = folder_to_images(path, size) # mang numpy nhieu anh, paths
            rates = mean_square_difference(query, images_np)
            ls_path_score.extend(list(zip(images_path, rates)))
    return query, ls_path_score

root_img_path = f"C:\\Users\\Admin\Documents\\AIO---262-Trinh-Xd\\Module 2 project\\Image Retreveal\\{ROOT}\\train\\"
query_path = f"C:\\Users\\Admin\\Documents\\AIO---262-Trinh-Xd\\Module 2 project\\Image Retreveal\\{ROOT}\\test\\Orange_easy\\0_100.jpg"
size = (448, 448)
query, ls_path_score = get_l2_score(root_img_path, query_path, size)
#plot_results(query_path, ls_path_score, reverse=False)

# Cosine Similarity
def cosine_similarity(query, data):
    axis_batch_size = tuple(range(1,len(data.shape)))
    # Ứng dụng norm
    query_norm = np.sqrt(np.sum(query**2))
    data_norm = np.sqrt(np.sum(data**2, axis=axis_batch_size))
    return np.sum(data * query, axis=axis_batch_size) / (query_norm*data_norm + np.finfo(float).eps)

def get_cosine_similarity_score(root_img_path, query_path, size):
    query = read_image_from_path(query_path, size)
    ls_path_score = []
    for folder in os.listdir(root_img_path):
        if folder in CLASS_NAME:
            path = root_img_path + folder
            images_np, images_path = folder_to_images(path, size) # mang numpy nhieu anh, paths
            rates = cosine_similarity(query, images_np)
            ls_path_score.extend(list(zip(images_path, rates)))
    return query, ls_path_score

root_img_path = f"C:\\Users\\Admin\Documents\\AIO---262-Trinh-Xd\\Module 2 project\\Image Retreveal\\{ROOT}\\train\\"
query_path = f"C:\\Users\\Admin\\Documents\\AIO---262-Trinh-Xd\\Module 2 project\\Image Retreveal\\{ROOT}\\test\\Orange_easy\\0_100.jpg"
size = (448, 448)
query, ls_path_score = get_cosine_similarity_score(root_img_path, query_path, size)
# plot_results(query_path, ls_path_score, reverse=False)

#Correlation Coefficient
def correlation_coefficient(query, data):
    axis_batch_size = tuple(range(1,len(data.shape)))
    query_mean = query - np.mean(query)
    data_mean = data - np.mean(data, axis=axis_batch_size, keepdims=True)
    query_norm = np.sqrt(np.sum(query_mean**2))
    data_norm = np.sqrt(np.sum(data_mean**2, axis=axis_batch_size))

    return np.sum(data_mean * query_mean, axis=axis_batch_size) / (query_norm*data_norm + np.finfo(float).eps)

def get_correlation_coefficient_score(root_img_path, query_path, size):
    query = read_image_from_path(query_path, size)
    ls_path_score = []
    for folder in os.listdir(root_img_path):
        if folder in CLASS_NAME:
            path = root_img_path + folder
            images_np, images_path = folder_to_images(path, size) # mang numpy nhieu anh, paths
            rates = correlation_coefficient(query, images_np)
            ls_path_score.extend(list(zip(images_path, rates)))
    return query, ls_path_score

root_img_path = f"C:\\Users\\Admin\Documents\\AIO---262-Trinh-Xd\\Module 2 project\\Image Retreveal\\{ROOT}\\train\\"
query_path = f"C:\\Users\\Admin\\Documents\\AIO---262-Trinh-Xd\\Module 2 project\\Image Retreveal\\{ROOT}\\test\\Orange_easy\\0_100.jpg"
size = (448, 448)
query, ls_path_score = get_cosine_similarity_score(root_img_path, query_path, size)
plot_results(query_path, ls_path_score, reverse=True)