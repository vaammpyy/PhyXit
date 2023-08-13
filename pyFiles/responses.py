import discord
import os
from simulate import *
from papers import *
from prof import *

help = open('../helpDesk/main.txt', mode='r').read()
sim_h = open('../helpDesk/sim_h.txt', mode='r').read()
arxiv_h = open('../helpDesk/arxiv_h.txt', mode='r').read()
prof_h = open('../helpDesk/prof_h.txt', mode='r').read()
data_vec = 0


def vec(arr):
    global data_vec
    try:
        data_vec = [float(x) for x in arr]
    except:
        return ["\n>>> "+sim_h, 't']


def handle_response(message) -> str:
    p_message = ' '.join(message).lower().split()
    if p_message[0] == 'hello':
        return ['Hey there! \n>>> \n2 \n3 \n4 \n5', 't']
    if p_message[0] == 'img':

        return [['movie.mp4', '38891d63301e957da6fc19b732a09caf.jpg'], 'm']

    if p_message[0] == 'sim':
        try:
            os.remove('movie.mp4')
        except:
            pass
        vec(p_message[2:])
        if p_message[1] == 'projectile':
            projectile_motion(*data_vec)
        elif p_message[1] == 'pendulum':
            single_pendulum_motion(*data_vec)

        elif p_message[1] == 'spring':
            spring_block_motion(*data_vec)

        elif p_message[1] == 'rand_walk':
            random_walker_motion(*data_vec)
        else:
            return ["\n>>> "+sim_h, 't']
        return [['movie.mp4'], 'm']

    if p_message[0] == 'arxiv':
        try:
            os.remove('papers.log')
            os.remove('paper.pdf')
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

            return [[f"Details of paper: **{p_message[2]}**\n>>> "+lines, "paper.pdf"], 'm']

        return ["\n>>> "+arxiv_h, 't']

    if p_message[0] == 'profs' or p_message[0] == 'prof':
        try:
            os.remove('prof.log')
            os.remove('prof.jpg')
        except:
            pass

        if p_message[1] == 'name':
            name = ' '.join(p_message[2:])
            knowProf(name)

            paper = open('prof.log', mode='r')
            lines = paper.read()

            return [["prof.jpg", f"\n>>> {lines}"], 'm']
        return ["\n>>> "+prof_h, 't']

    return ["\n>>> "+help, 't']