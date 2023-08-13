import discord
import os
from pyFiles.simulate import *
from pyFiles.papers import *
from pyFiles.prof import *
from pyFiles.wiki import *


Help = open('./helpDesk/main.txt', mode='r').read()
sim_h = open('./helpDesk/sim_h.txt', mode='r').read()
arxiv_h = open('./helpDesk/arxiv_h.txt', mode='r').read()
prof_h = open('./helpDesk/prof_h.txt', mode='r').read()
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

        return [['./tmp/movie.mp4', '38891d63301e957da6fc19b732a09caf.jpg'], 'm']

    '''
    The below area deals with the simulation call functions
    '''
    if p_message[0] == 'sim':
        try:
            os.remove('./tmp/movie.mp4')
        except:
            pass
        vec(p_message[2:])
        if p_message[1] == 'projectile':
            projectile_motion(*data_vec)
        elif p_message[1] == 'pendulum':
            single_pendulum_motion(*data_vec)

        elif p_message[1] == 'spring':
            spring_block_motion(*data_vec)

        elif p_message[1] == 'diffusion':
            random_walker_motion(*data_vec)

        elif p_message[1] == 'charged_int':
            charge_interaction_motion(*data_vec)
        else:
            return ["\n>>> "+sim_h, 't']
        return [['./tmp/movie.mp4'], 'm']

    '''
    The below area deals with the archive and wiki call functions
    '''

    if p_message[0] == 'arxiv':
        try:
            os.remove('./tmp/papers.log')
            os.remove('./tmp/paper.pdf')
        except:
            pass

        if p_message[1] == '-h':
            return ["\n>>> "+arxiv_h, 't']

        if p_message[1] == 'top':
            query = ' '.join(p_message[2:])
            getList(query)
            paper = open('./tmp/papers.log', mode='r')
            lines = paper.read()
            return [f"Top 10 papers related to **{query}**\n>>> "+lines, 't']

        if p_message[1] == 'fetch':
            fetchPaper(p_message[2])
            paper = open('./tmp/papers.log', mode='r')
            lines = paper.read()

            return [[f"Details of paper: **{p_message[2]}**\n>>> {lines}", "./tmp/paper.pdf"], 'm']
        if p_message[1] == 'wiki':
            query = ' '.join(p_message[2:])
            getSummary(query)
            paper = open('./tmp/papers.log', mode='r')
            lines = paper.read()
            return [[f"Summary of the Article on wikipedia:\n>>> {lines}"], 'm']
        return ["\n>>> "+arxiv_h, 't']

    '''
    The below area deals with the prof identification APIs
    '''
    if p_message[0] == 'profs' or p_message[0] == 'prof':
        try:
            os.remove('./tmp/prof.log')
            os.remove('./tmp/prof.jpg')
        except:
            pass

        if p_message[1] == 'name':
            name = ' '.join(p_message[2:])
            knowProf(name)

            paper = open('./tmp/prof.log', mode='r')
            lines = paper.read()

            return [["./tmp/prof.jpg", f"\n>>> {lines}"], 'm']
        return ["\n>>> "+prof_h, 't']

    return ["\n>>> "+Help, 't']
