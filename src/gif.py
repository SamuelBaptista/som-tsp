from genericpath import exists
import glob
import os

from PIL import Image

def get_frames(source="./diagrams/*.png"):
    frames = []
    imgs = glob.glob(source)

    for i in imgs:
        new_frame = Image.open(i)
        frames.append(new_frame)

    final_frames = frames[1:len(frames)]

    return final_frames

def create_gif(frames, name):

    if not os.path.exists('./gifs'):
        os.makedirs('./gifs')

    frames[0].save(
        f'./gifs/{name}.gif',
        format='GIF',
        append_images=frames[1:],
        save_all=True,
        duration=300,
        loop=0
    )


def remove_images(filename, path='./diagrams'):
    files = os.listdir(path)
    
    for file in files:
        if file == f'route_{filename}.png':
            continue
        os.remove(os.path.join(path, file))



if __name__ == '__main__':
    frames = get_frames()
    create_gif(frames, 'teste')
    remove_images()