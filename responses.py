import discord
import os
from simulate import *
from papers import *

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
        return [['movie.mp4', '38891d63301e957da6fc19b732a09caf.jpg'], 'm']
        # except:
        #     continue
    if p_message[0] == 'sim':
        try:
            os.remove('movie.mp4')
        except:
            pass
        if p_message[1] == 'projectile':
            v = float(p_message[2])
            theta = float(p_message[3])
            h = float(p_message[4])
            dt = float(p_message[5])
            t = float(p_message[6])
            projectile_motion(v, theta, h, dt, t)

            
            return [['movie.mp4', "\n>>> "+help], 'm']
    if p_message[0] == 'arxiv':
        try:
            os.remove('papers.log')
        except:
            pass
        if p_message[1] == 'top':
            query = ' '.join(p_message[2:])
            getList(query)
            paper = open('papers.log', mode='r')
            lines = paper.read()
            return [f"Top 10 papers related to **{query}**\n>>> "+lines, 't']
        if p_message[1] == 'fetch':
            fetchPaper(p_message[2])
            paper = open('papers.log', mode='r')
            lines = paper.read()
            return [f"Details of paper: **{p_message[2]}**\n>>> "+lines, 't']


    return ["\n>>> "+help, 't']
