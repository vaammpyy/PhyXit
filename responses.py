import discord
from simulate import *
f = open('main.txt', mode='r')
help = f.read()


def handle_response(message) -> str:
    p_message = ' '.join(message).lower().split()
    if p_message[0] == 'hello':
        return ['Hey there! \n>>> \n2 \n3 \n4 \n5', 't']
    if p_message[0] == 'img':
        # while(True):
        # try:
        # media = ['vid.mp4', '38891d63301e957da6fc19b732a09caf.jpg']
        return [['vid.mp4', '38891d63301e957da6fc19b732a09caf.jpg'], 'm']
        # except:
        #     continue
    if p_message[0] == 'sim':
        if p_message[1] == 'projectile':
            v = float(p_message[2])
            theta = float(p_message[3])
            h = float(p_message[4])
            dt = float(p_message[5])
            t = float(p_message[6])
            projectile_motion(v, theta, h, dt, t)

            while (True):
                try:
                    return [['movie.mp4'], 'm']
                except:
                    continue

    return ["\n>>> "+help, 't']
