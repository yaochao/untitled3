#!/usr/bin/env python3
# -*- coding:utf-8 -*- 
# Created by yaochao at 2018/4/9


import multiprocessing as mp, os

cores = 4


def process(line):
    '''
    处理读取出来的每一行
    :param line:
    :return:
    '''
    print(line)


def process_wrapper(chunkStart, chunkSize):
    with open("input.txt") as f:
        f.seek(chunkStart)
        lines = f.read(chunkSize).splitlines()
        for line in lines:
            process(line)


def chunkify(fname, size=1024 * 1024):
    fileEnd = os.path.getsize(fname)
    with open(fname, 'r') as f:
        chunkEnd = f.tell()
    while True:
        chunkStart = chunkEnd
        f.seek(size, 1)
        f.readline()
        chunkEnd = f.tell()
        yield chunkStart, chunkEnd - chunkStart
        if chunkEnd > fileEnd:
            break


# init objects
pool = mp.Pool(cores)
jobs = []

# create jobs
for chunkStart, chunkSize in chunkify("input.txt"):
    jobs.append(pool.apply_async(process_wrapper, (chunkStart, chunkSize)))

# wait for all jobs to finish
for job in jobs:
    job.get()

# clean up
pool.close()
