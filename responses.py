import discord
import os
from simulate import *
from papers import *

f = open('main.txt', mode='r')
help = f.read()
sim_h = open('sim_h.txt', mode='r').read()
arxiv_h = open('arxiv_h.txt', mode='r').read()


def handle_response(message) -> str:
    p_message = ' '.join(message).lower().split()
    if p_message[0] == 'hello':
        return ['Hey there! \n>>> \n2 \n3 \n4 \n5', 't']
    if p_message[0] == 'img':

        return [['movie.mp4', '38891d63301e957da6fc19b732a09caf.jpg'], 'm']

    if p_message[0] == 'sim':
        try:
            os.remove('movie.mp4')
            os.remove('op.txt')
        except:
            pass
        if p_message[1] == '-h':
            return ["\n>>> "+sim_h, 't']
        if p_message[1] == 'projectile':
            data_vec = [float(x) for x in p_message[2:]]
            projectile_motion(*data_vec)
            return [['movie.mp4', "op.txt"], 'm']
        if p_message[1] == 'pendulum':
            data_vec = [float(x) for x in p_message[2:]]
            # pendulum function(*data_vec)
            return [['movie.mp4', "op.txt"], 'm']
        return ["\n>>> "+sim_h, 't']

    if p_message[0] == 'arxiv':
        try:
            os.remove('papers.log')
        except:
            pass
        if p_message[1] == '-h':
            return ["\n>>> "+arxiv_h, 't']
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
        return ["\n>>> "+arxiv_h, 't']
    return ["\n>>> "+help, 't']
