from PIL import Image
import numpy as np
import doctest


def get_avg_brightness(img_data, mosaic_size, x, y):
    """Calculates average brightnes of pixels from x to x+mosaic_size and from y to y+mosaic_size

    Args:
        img_data (ndarray): array with data from image
        mosaic_size (integer): mosaic size
        x (integer): width iterator
        y (integer): height iterator

    Returns:
        float: average brightness

    >>> get_avg_brightness(np.array(Image.open('images/test_image.jpg')), 10, 0, 0)
    144.99
    """
    return np.average(img_data[x : x + mosaic_size, y : y + mosaic_size])


def save_image(data, file_name, path):
    """Creates image from array with given name

    Args:
        data (ndarray): array with data from image
        file_name (string): name of new file
        path (string): path to input image
    """
    Image.fromarray(data).save(f'{file_name}.{path.split(".")[-1]}')


def create_mosaic(img_data, img_size, mosaic_size, grayscale_step):
    """Creates mosaic

    Args:
        img_data (ndarray): array with data from image
        img_size (tuple): image size (width, height)
        mosaic_size (integer): mosaic size
        grayscale_step (integer): grayscale step
    """
    for x in range(0, img_size[0], mosaic_size):
        for y in range(0, img_size[1], mosaic_size):
            avg_brightness = get_avg_brightness(img_data, mosaic_size, x, y)
            img_data[x : x + mosaic_size, y : y + mosaic_size] = (
                avg_brightness - avg_brightness % grayscale_step
            )


def main():
    path = input("Enter image path: ")
    output_name = input("Enter name of output file: ")
    mosaic_size = int(input("Enter mosaic size: "))
    grayscale_step = int(input("Enter grayscale step: "))

    img_data = np.array(Image.open(path))
    img_size = img_data.shape

    create_mosaic(img_data, img_size, mosaic_size, grayscale_step)
    save_image(img_data, output_name, path)


if __name__ == "__main__":
    doctest.testmod()
    try:
        main()
    except KeyboardInterrupt:
        quit()
