from PIL import Image
import numpy as np
import math


def count_distance1(px1, px2):
    distance = math.sqrt(((px1[0] - px2[0]) ** 2) + ((px1[1] - px2[1]) ** 2) + ((px1[2] - px2[2]) ** 2))
    return distance


def count_distance2(px1, px2):
    distance = max(int(px1[0]) - int(px2[0]), int(px1[1]) - int(px2[1]), int(px1[2]) - int(px2[2]))
    return distance


def contour1(img, width, height):
    contours = Image.new("RGB", (width, height), "white")
    carray = np.array(contours)
    for i in range(1, width - 1):
        for j in range(1, height - 1):
            if (count_distance1(img[i][j], img[i + 1][j]) > 20 or count_distance1(img[i][j], img[i][
                j + 1]) > 20 or count_distance1(img[i][j], img[i - 1][j]) > 20 or count_distance1(img[i][j], img[i][
                j - 1]) > 20 or count_distance1(img[i][j], img[i + 1][j + 1]) > 20 or count_distance1(img[i][j],
                                                                                                      img[i - 1][
                                                                                                          j - 1]) > 20 or count_distance1(
                    img[i][j], img[i + 1][j - 1]) > 20 or count_distance1(img[i - 1][j + 1], img[i][j]) > 20):
                carray[i][j] = [105, 105, 105]
    return carray


def contour2(img, width, height):
    contours = Image.new("RGB", (width, height), "white")
    carray = np.array(contours)
    for i in range(1, width - 1):
        for j in range(1, height - 1):
            if (count_distance2(img[i][j], img[i + 1][j]) > 20 or count_distance2(img[i][j], img[i][
                j + 1]) > 20 or count_distance2(img[i][j], img[i - 1][j]) > 20 or count_distance2(img[i][j], img[i][
                j - 1]) > 20 or count_distance2(img[i][j], img[i + 1][j + 1]) > 20 or count_distance2(img[i][j],
                                                                                                      img[i - 1][
                                                                                                          j - 1]) > 20 or count_distance2(
                    img[i][j], img[i + 1][j - 1]) > 20 or count_distance2(img[i - 1][j + 1], img[i][j]) > 20):
                carray[i][j] = [105, 105, 105]
    return carray


img = Image.open('apple.png')
array = np.array(img)
print(array[0][0])
contoured = contour1(array, img.size[0], img.size[1])
Image.fromarray(contoured).show()

contoured = contour2(array, img.size[0], img.size[1])
Image.fromarray(contoured).show()

img = Image.open('tree.png')
array = np.array(img)
print(array[0][0])
contoured = contour1(array, img.size[0], img.size[1])
Image.fromarray(contoured).show()

contoured = contour2(array, img.size[0], img.size[1])
Image.fromarray(contoured).show()
