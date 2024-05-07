import math
import threading
from quadtreenode import QuadTreeNode

class QuadTree:
    _lock = threading.Lock() # access of _lock only to QuadTree class
    _instance = None

    def __init__(self, width, height, x=0, y=0):
        self.root = QuadTreeNode(x, y, width, height)

    # static method means it will not need a class instance 
    # and can be called from anywhere in the program
    @staticmethod
    def get_instance(width, height):
        if QuadTree._instance is None:
            with QuadTree._lock: # acquire thread lock
                if QuadTree._instance is None: # double check inside lock
                    QuadTree._instance = QuadTree(width, height)
        return QuadTree._instance.root

    def insert(self, cab):
        return self.root.add_driver(cab=cab)

    def find_nearest_driver(self, target):
        cabs = self.root.get_nearest_cabs(target)
        return cabs
