import pygame, sys, os
from pygame import *

import tkinter as tk
from tkinter import filedialog

from colors import *
from nodes import Node
from edges import Edge

class Maker:
    def __init__(self, width: int, height: int):
        #window size
        self.width = width
        self.height = height

        #dark mode
        self.dark_mode = False

        #fps and clock
        self.FPS = 60
        self.clock = pygame.time.Clock()
        
        #pygame initialization
        pygame.init()

        #create window
        self.window = pygame.display.set_mode((800, 700), RESIZABLE)
        pygame.display.set_caption("Map maker")

        #mouse variables
        self.mouse_x, self.mouse_y = pygame.mouse.get_pos()
        self.mouse_click = False

        #moving variables
        self.move_velocity = 5
        self.move_x = 0
        self.move_y = 0

        #nodes
        self.nodes = []
        self.clicked_idx = None
        self.name_input = False

        #edges
        self.edges = []
        self.create_new_edge = False
        self.node1 = None
        self.node2 = None

        #for tkinter
        root = tk.Tk()
        root.withdraw()

    def open_file(self):
        file_path = filedialog.askopenfilename()
        if type(file_path) != str:
            return
        
        self.nodes = []
        self.edges = []
        
        with open(file_path, "r") as file:
            n_of_nodes = int(file.readline())
            for _ in range(n_of_nodes):
                node_data = file.readline().split(";")
                name = node_data[0]
                x = int(node_data[1])
                y = int(node_data[2])
                w = int(node_data[3])
                h = int(node_data[4])
                self.nodes.append(Node(x, y, name, w, h))
            n_of_edges = int(file.readline())
            for _ in range(n_of_edges):
                edge_data = file.readline().split(";")
                idx1 = int(edge_data[0])
                idx2 = int(edge_data[1])
                node1 = self.nodes[idx1]
                node2 = self.nodes[idx2]
                self.edges.append(Edge(node1, node2))

    def save_to_file(self):
        file_path = filedialog.asksaveasfilename()
        if type(file_path) != str:
            return
        
        str_to_save = f"{len(self.nodes)}\n"
        for node in self.nodes:
            str_to_save += f"{node.name};{int(node.x)};{int(node.y)};{int(node.width)};{int(node.height)}\n"
        str_to_save += f"{len(self.edges)}\n"
        for edge in self.edges:
            str_to_save += f"{self.nodes.index(edge.node1)};{self.nodes.index(edge.node2)}\n"
        
        with open(file_path, "w") as file:
            file.write(str_to_save)

    def search_for_clicked_node(self):
        for i in range(len(self.nodes)):
            node = self.nodes[i]
            if node.x < self.mouse_x and node.y < self.mouse_y and node.x+node.width > self.mouse_x and node.y+node.height > self.mouse_y:
                return i
        return None
    
    def remove_node(self, node: Node):
        to_remove = []
        for edge in self.edges:
            if edge.contains_node(node):
                to_remove.append(edge)
        for edge in to_remove:
            self.edges.remove(edge)
        self.nodes.remove(node)

    def draw_all(self):
        if self.dark_mode:
            self.window.fill(black)
        else:
            self.window.fill(white)
        for edge in self.edges:
            edge.draw(self.window)
        for node in self.nodes:
            node.draw(self.window)

    def run(self):
        while True:
            #update size variables values
            self.width, self.height = self.window.get_size()

            #mouse position
            self.mouse_x, self.mouse_y = pygame.mouse.get_pos()

            #moving map by WSAD
            for node in self.nodes:
                node.x += self.move_x
                node.y += self.move_y

            #moving nodes by mouse
            if self.mouse_click and self.clicked_idx is not None:
                node = self.nodes[self.clicked_idx]
                node.x = self.mouse_x - node.width/2
                node.y = self.mouse_y - node.height/2

            #update view
            self.draw_all()

            #handle events
            for event in pygame.event.get():
                #quit
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit(0)
                #keys
                elif event.type == pygame.KEYDOWN:
                    if self.name_input:
                        #enter
                        if event.key == pygame.K_RETURN:    
                            self.name_input = False
                        elif event.key == pygame.K_BACKSPACE:
                            self.nodes[self.clicked_idx].name = self.nodes[self.clicked_idx].name[:-1:]
                        else:
                            self.nodes[self.clicked_idx].name += pygame.key.name(event.key)
                        continue
                    if event.key == pygame.K_n:
                        self.nodes.append(Node(self.mouse_x, self.mouse_y))
                    elif event.key == pygame.K_m:
                        self.create_new_edge = True
                    elif event.key == pygame.K_x:
                        self.clicked_idx = self.search_for_clicked_node()
                        if self.clicked_idx is not None:
                            self.remove_node(self.nodes[self.clicked_idx])
                    elif event.key == pygame.K_c:
                        self.open_file()
                    elif event.key == pygame.K_v:
                        self.save_to_file()
                    elif event.key == pygame.K_1:
                        self.dark_mode = False
                    elif event.key == pygame.K_2:
                        self.dark_mode = True

                    #moving
                    elif event.key == pygame.K_w:
                        self.move_y = 1 * self.move_velocity
                    elif event.key == pygame.K_s:
                        self.move_y = -1 * self.move_velocity
                    elif event.key == pygame.K_a:
                        self.move_x = 1 * self.move_velocity
                    elif event.key == pygame.K_d:
                        self.move_x = -1 * self.move_velocity

                elif event.type == pygame.KEYUP:
                    #moving
                    if event.key == pygame.K_w:
                        self.move_y = 0
                    elif event.key == pygame.K_s:
                        self.move_y = 0
                    elif event.key == pygame.K_a:
                        self.move_x = 0
                    elif event.key == pygame.K_d:
                        self.move_x = 0
                    
                #mouse down
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    self.clicked_idx = self.search_for_clicked_node()
                    #left
                    if event.button == 1:
                        self.mouse_click = True
                        if self.clicked_idx is not None:
                            #create new edge
                            if self.create_new_edge:
                                if self.node1 is None:
                                    self.node1 = self.nodes[self.clicked_idx]
                                else:
                                    self.node2 = self.nodes[self.clicked_idx]
                                    already_exists = False
                                    for edge in self.edges:
                                        if edge.contains_node(self.node1) and edge.contains_node(self.node2):
                                            already_exists = True
                                            break

                                    if self.node1 is not self.node2 and not already_exists:
                                        self.edges.append(Edge(self.node1, self.node2))

                                    self.create_new_edge = False
                                    self.node1 = None
                                    self.node2 = None
                        else:
                            self.create_new_edge = False
                    #right
                    elif event.button == 3:
                        if self.clicked_idx is not None and not self.name_input:
                            self.nodes[self.clicked_idx].name = ""
                            self.name_input = True

                #mouse up
                elif event.type == pygame.MOUSEBUTTONUP:
                    self.mouse_click = False
                    if not self.name_input:
                        self.clicked_idx = None



            #display refresh
            pygame.display.update()
            self.clock.tick(self.FPS)


