def color_to_grayscale(image):
    """
    Convert an RGB image to grayscale using luminance weights.
    """
    # Write code here
    n = len(image)
    m = len(image[0])
    res = [[0 for i in range(0, m)] for i in range(0, n)]

    for i in range(0, n):
        for j in range(0, m):
            res[i][j] = 0.299 * image[i][j][0] + 0.587 * image[i][j][1] + 0.114 * image[i][j][2]

    return res