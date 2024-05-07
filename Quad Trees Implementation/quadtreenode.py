from Helper.constants import *
from Cab import Cab

class QuadTreeNode:
    def __init__(self, x, y, width, height):
        self.x = x # x-cord of the center
        self.y = y # y-cord of the center
        self.width = width # this is half width
        self.height = height # this is half height
        self.cabs = []
        self.children = [None, None, None, None]
        self.type = QuadTreeNodeType.EMPTY_LEAF

    def add_driver(self, cab):
        if not self.in_bounds(cab):
            print(f"The location ({cab.x}, {cab.y}) is out of bounds.")
            return False # cab is out of bounds

        if self.type == QuadTreeNodeType.EMPTY_LEAF:
            if len(self.cabs) < 1:
                print(f"Inserting cab ({cab.x}, {cab.y}) at quad tree with center ({self.x}, {self.y}) and half lengths ({self.width}, {self.height})")
                self.cabs.append(cab)
                self.type = QuadTreeNodeType.FULL_LEAF
                return True
        
        elif self.type == QuadTreeNodeType.FULL_LEAF:
            self.type = QuadTreeNodeType.DIVIDED
            self.create_children()

            # move existing_cab to appropriate child node
            for existing_cab in self.cabs:
                for child in self.children:
                    if child.in_bounds(existing_cab):
                        child.add_driver(existing_cab)
                        self.cabs.remove(existing_cab)
                        break

            # insert the new cab in correct child node
            for child in self.children:
                if child.add_driver(cab):
                    return True
            return False      
        
        else: # for DIVIDED 
            # check where the cab belongs
            if cab.x < self.x and cab.y > self.y:
                print("Recursively inserting cab in NW quad")
                self.children[0].add_driver(cab)
            elif cab.x >= self.x and cab.y >= self.y:
                print("Recursively inserting cab in NE quad")
                self.children[1].add_driver(cab)
            elif cab.x < self.x and cab.y < self.y:
                print("Recursively inserting cab in SW quad")
                self.children[2].add_driver(cab)
            else:
                print("Recursively inserting cab in SE quad")
                self.children[3].add_driver(cab)


    def create_children(self):
        print(f"Divding the quad with center ({self.x}, {self.y}) and half lengths ({self.width}, {self.height})")
        sub_width = self.width / 2
        sub_height = self.height / 2
        # NW
        self.children[0] = QuadTreeNode(self.x - sub_width, self.y + sub_height, sub_width, sub_height)
        # NE 
        self.children[1] = QuadTreeNode(self.x + sub_width, self.y + sub_height, sub_width, sub_height)
        # SW 
        self.children[2] = QuadTreeNode(self.x - sub_width, self.y - sub_height, sub_width, sub_height)
        # SE 
        self.children[3] = QuadTreeNode(self.x + sub_width, self.y - sub_height, sub_width, sub_height)

    def in_bounds(self, cab):
        return (cab.x >= self.x - self.width and cab.x <= self.x + self.width \
        and cab.y >= self.y - self.height and cab.y <= self.y + self.height)

    def get_nearest_cabs(self, loc, cabs=None):
        if cabs is None:
            cabs = []
        
        if len(cabs) >= NO_OF_CABS:
            return cabs

        if self.type == QuadTreeNodeType.FULL_LEAF:
            print(f"Found nearby cab at loc ({self.cabs[0].x}, {self.cabs[0].y}) in quadrant ({self.x}, {self.y})")
            cabs.extend(self.cabs)
        
        if self.type == QuadTreeNodeType.DIVIDED:
            print("*"*20)
            print(f"Searching for cabs in children of quadrant at center ({self.x}, {self.y})")
            children_sorted = sorted(self.children, key=lambda child: ((child.x - loc.x)**2 + (child.y - loc.y)**2))

            # Recursively search child nodes
            for child in children_sorted:
                if len(cabs) >= NO_OF_CABS:
                    return cabs
                child.get_nearest_cabs(loc, cabs)

        return cabs
        

