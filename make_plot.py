import matplotlib.pyplot as plt
import matplotlib.patches as patches
import matplotlib.collections as mpl
from further_includes import *
from includes import*
from cspace import *


class Plot:
    def __init__(self,x_start,x_goal):
        self.xI,self.xG=x_start,x_goal
        self.env=ENV
        self.obstacle_prop=self.env.obstacle_props
    
    def animation(self, nodelist, path, animation=False):
        self.plot_environmentv2()
        self.plot_visited(nodelist, animation)
        self.plot_path(path)
    
    
    def plot_environmentv2(self):

        FIG, AX = plt.subplots(nrows=1, ncols=1, sharex=True, sharey=True, figsize=(9, 9))
        plt.ylim(0, self.env.width)
        plt.xlim(0, self.env.height)
        plt.scatter(self.env.start[0], self.env.start[1], s=500, c=COLORS[0], marker='v')
        plt.scatter(self.env.end[0], self.env.end[1], s=800, c=COLORS[1], marker='v')
        plt.plot(self.env.start[0],self.env.start[1],'bo',)
        plt.plot()
    
        OBSTACLES = [plt.Circle(j[0], j[1]) for i, j in enumerate(self.env.obstacle_props)]
        OBS_PATCHES = mpl.collections.PatchCollection(OBSTACLES, facecolors='black')
        AX.add_collection(OBS_PATCHES)
        
    def animation_v2(self, path_x, path_y, visited,V):
        self.plot_environmentv2()
        

        for node in V:
            plt.plot(node.x, node.y, marker='.', color='lightgrey', markersize=3)

        count = 0
        for node in visited:
            count += 1
            plt.plot([node.x, node.parent.x], [node.y, node.parent.y], '-g')
            plt.gcf().canvas.mpl_connect(
                'key_release_event',
                lambda event: [exit(0) if event.key == 'escape' else None])
            if count % 10 == 0:
                plt.pause(0.001)

        plt.plot(path_x, path_y, linewidth=2, color='red')
        plt.pause(0.01)
        plt.show()

        
    
    def plot_visited(self,nodelist):
        #
        count=0
        for node in nodelist:
            #
            count+=1
            if node.parent:
                #
                plt.plot([node.parent.x, node.x], [node.parent.y, node.y], "-g")
                plt.gcf().canvas.mpl_connect('key_release_event',lambda event:[exit(0) if event.key == 'escape' else None])
                if count %10==0:
                    #
                    plt.pause(0.01)
        else:
            #
            for node in nodelist:
                #
                if node.parent:
                    #
                    plt.plot([node.parent.x, node.x], [node.parent.y, node.y], "-g")
                    
   
    def plot_path(path):
        if len(path)!=0:
            plt.plot([x[0] for x in path], [x[1] for x in path], '-r', linewidth=2)
            plt.pause(0.01)
            print(path)
        plt.show()





#p=Plot([5,10],[10,10])
#p.plot_environmentv2()
#plt.show()
