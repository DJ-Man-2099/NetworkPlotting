from PyQt5.QtWidgets import *

from matplotlib.backends.backend_qt5agg import FigureCanvas

from matplotlib.figure import Figure

import numpy as np

import  random 

import math


class MplWidget (QWidget):
    frame_size = [0]

    def __init__(self,  parent=None):

        QWidget . __init__(self,  parent)

        self . canvas = FigureCanvas(Figure())

        vertical_layout = QVBoxLayout()
        vertical_layout . addWidget(self . canvas)

        self . canvas . Plot = self . canvas . figure . add_subplot(111)
        self . setLayout(vertical_layout)

    def update_graph(self):

        
        Labels = np.array([1,2,4,8,16,32,64,128,256]) #The X-Axis Labels
        xticks = np.array([0,1,2,3,4,5,6,7,8]) #The X-Axis Values
        x = np.arange(9) #The Continous input
        t = 2**x
        B = 10*(10**6)
        
        T = (51.2/2)*10**(-6)
        A = (1-1/t)**(t-1)
        
        self.canvas.Plot.clear()
        
        #For Loop, for all frame_sizes
        for f in self.frame_size:
            F = f*8
            P = F/B
            y = P/(P+(2*T/A))#The Continous Output
            self  . canvas . Plot . plot(x,  y)
            self.canvas.Plot.set_xticks(xticks)
            self.canvas.Plot.set_xticklabels(Labels)
            self.canvas.Plot.set_yticks([0.0,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1.0])
        self  . canvas . Plot . legend(
            (self.frame_size), loc='upper right')
        self . canvas . Plot . set_title('Efficiency')
        self . canvas . Plot . set_xlabel('No. of Ready Channels')
        self . canvas . Plot . set_ylabel('Efficiency')
        self  . canvas . draw()

    
