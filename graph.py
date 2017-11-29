import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation

class TimelineGif:

    # TODO: Add more colors
    colors = ['gold', 'yellowgreen', 'lightcoral', 'lightskyblue', 'limegreen', 'red', 'navy', 'blue', 'magenta', 'crimson']

    def __init__(self, timeline):
        self.timeline = timeline
        self.labels = list(timeline[0].keys())

        self.fig, self.ax = plt.subplots()

    def _update(self, frame):
        self.ax.clear()        
        self.ax.axis('equal')
        data = [self.timeline[frame][label] for label in self.labels]
        self.ax.pie(data, labels=self.labels, colors=self.colors, autopct='%1.1f%%', startangle=90)
        title = 'Generation ' + str(frame+1)
        self.ax.set_title(title)

    def generate(self, name):
        gif = FuncAnimation(self.fig, self._update, frames=np.arange(0, len(self.timeline)), interval=200)
        gif.save(name, writer='imagemagick')
