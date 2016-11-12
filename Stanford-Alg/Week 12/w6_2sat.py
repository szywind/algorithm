#!/usr/bin/python
#-*- coding: utf-8 -*-

# for coursera algo course 02.
# https://class.coursera.org/algo2-003/quiz/attempt?quiz_id=97
#
# by dmitriy khodakov (dmitryhd@gmail.com) - 08.08.2014

"""
In this assignment you will implement one or more algorithms for the 2SAT problem.
Used Papadmitriou 2sat. see http://e-maxx.ru/algo/2_sat
"""

import sys
sys.path.append('../')

def run_tests(cases, solve_function, load_function):
    # format: file_with case, answer
    for case in cases:
        res = solve_function(*load_function(case[0]))
        assert res == case[1], 'test case {} gone wrong, get {}'.format(case[0], cc)
    print('\n---------------\nall %i tests passed.' % len(cases))


def load_file(filename):
    edges = []
    with open(filename) as fd:
        n = int(fd.readline())
        for line in fd.readlines():
            sline = line.split()
            edges.append([-1*int(sline[0]), int(sline[1])])
            edges.append([-1*int(sline[1]), int(sline[0])])
    return n, edges


def solve_2sat(n, edges):
    VISITED = 1
    graph = {}
    trans_graph = {}
    for edge in edges:
        if not edge[0] in graph.keys():
            graph[edge[0]] = [[],False]
        if not edge[1] in graph.keys():
            graph[edge[1]] = [[],False]
        if not edge[1] in trans_graph.keys():
            trans_graph[edge[1]] = [[],False]
        if not edge[0] in trans_graph.keys():
            trans_graph[edge[0]] = [[],False]
        graph[edge[0]][0].append(edge[1])
        trans_graph[edge[1]][0].append(edge[0])

    def dfs(graph, start):
        #print('dfs------------')
        S = [start]
        order = []
        component = set()
        while S:
            v = S.pop()
            if graph[v][VISITED] == False:
                graph[v][VISITED] = True
                order.append(v)
                component.add(v)
                #print('going on v={}, edges={}'.format(v,graph[v][0]))
                for w in graph[v][0]:
                    S.append(w)
        #print('component:')
        return order, component

    def find_connected_components(graph, trans_graph):
        strong_conn_components = []
        all_visited = False
        vertex_order = []
        for vertex in graph.keys():
            if graph[vertex][VISITED] == False:
                order, component = dfs(graph, vertex)
                vertex_order += order
        for vertex in reversed(vertex_order):
            if trans_graph[vertex][VISITED] == False:
                order, component = dfs(trans_graph, vertex)
                strong_conn_components.append(component)
        #print('scc: {}'.format(strong_conn_components))
        return strong_conn_components

    strong_conn_components = find_connected_components(graph, trans_graph)

    strong_conn_components.sort(key=len, reverse=True)

    comp = {}
    for v in graph.keys():
        comp[v] = 9000000 + v
    for scc_ind in range(len(strong_conn_components)):
        for v in strong_conn_components[scc_ind]:
            comp[v] = scc_ind
    for v in graph.keys():
        if comp[v] == comp[-v]:
            #print('broke on', v)
            return False
    return True # exists

def test():
    cases = [ ['case01.txt', True],
              ['case02.txt', False],
              ['case03.txt', True],
            ]
    for case in cases:
        n, edges = load_data(case[0])
        cc = solve_2sat(n, edges)
        assert cc == case[1], 'test case {} gone wrong, get {}'.format(case[0], cc)

def main():
    if len(sys.argv) == 1:
        cases = [
              ['case03.txt', True],
              ['case02.txt', False],
              ['case03.txt', True],
            ]
        run_tests(cases, solve_2sat, load_file)
    else:
        files = [
            # '2sat1.txt',
            #      '2sat2.txt',
                 '2sat3.txt',
                 '2sat4.txt',
                 '2sat5.txt',
                 '2sat6.txt'
                ]
        for f in files:
            n, edges = load_file(f)
            cc = solve_2sat(n, edges)
            print(cc)

if __name__ == '__main__':
    main()
