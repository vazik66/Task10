from PIL import Image
import numpy as np


def get_avg_brightness(img_data, mosaic_size, x, y):
    return np.average(img_data[x : x + mosaic_size, y : y + mosaic_size])


def save_image(data, file_name, path):
    Image.fromarray(data).save(f'{file_name}.{path.split(".")[-1]}')


def create_mosaic(img_data, img_size, mosaic_size, grayscale_step):
    for x in range(0, img_size[0], mosaic_size):
        for y in range(0, img_size[1], mosaic_size):
            avg_brightness = get_avg_brightness(img_data, mosaic_size, x, y)
            img_data[x : x + mosaic_size, y : y + mosaic_size] = avg_brightness - avg_brightness % grayscale_step
            

def main():
    path = 'test_image.jpg'
    output_name = 'result_2'
    mosaic_size = 10
    grayscale_step = 50

    img_data = np.array(Image.open(path))
    img_size = img_data.shape

    create_mosaic(img_data, img_size, mosaic_size, grayscale_step)
    save_image(img_data, output_name, path)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        quit()
