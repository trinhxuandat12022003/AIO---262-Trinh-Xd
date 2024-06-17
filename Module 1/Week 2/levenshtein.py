def levenshtein_distance(source, target):
    # Bước 1: Khởi tạo ma trận D
    m = len(source)
    n = len(target)
    D = [[0] * (n + 1) for _ in range(m + 1)]

    # Bước 2: Hoàn thiện hàng đầu tiên và cột đầu tiên
    for i in range(m + 1):
        D[i][0] = i  # chi phí delete
    for j in range(n + 1):
        D[0][j] = j  # chi phí insert

    # Bước 3: Tính toán các giá trị với các ô còn lại trong ma trận
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if source[i - 1] == target[j - 1]:
                cost = 0  # nếu ký tự giống nhau
            else:
                cost = 1  # nếu ký tự khác nhau

            D[i][j] = min(
                D[i - 1][j] + 1,     # delete
                D[i][j - 1] + 1,     # insert
                D[i - 1][j - 1] + cost  # substitute
            )

    # Bước 4: Giá trị tại ô D[m][n] là khoảng cách Levenshtein
    return D[m][n]


# Ví dụ
source = "yu"
target = "you"
distance = levenshtein_distance(source, target)
print(f"Khoảng cách Levenshtein giữa '{source}' và '{target}' là {distance}")
print(levenshtein_distance(" hola ", " hello "))
