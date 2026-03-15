def image_histogram(image):
    """
    Compute the intensity histogram of a grayscale image.
    """
    arr = [0] * 256
    for row in image:
        for each in row:
            arr[each] += 1

    return arr
            