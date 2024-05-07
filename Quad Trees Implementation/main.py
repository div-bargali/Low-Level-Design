import Helper.constants
from quadtree import QuadTree
from Cab import Cab
from Location import Location

def main():
    qTree = QuadTree.get_instance(width=100, height=100)

    cab1 = Cab(30, 40)
    cab2 = Cab(-20, 70)
    cab3 = Cab(80, -90)
    cab4 = Cab(-60, -50)
    qTree.add_driver(cab1)
    qTree.add_driver(cab2)
    qTree.add_driver(cab3)
    qTree.add_driver(cab4)

    target = Location(10, -20)
    nearest_cabs = qTree.get_nearest_cabs(target)

    print("Nearest cabs to target location:")
    for cab in nearest_cabs:
        print(f"({cab.x}, {cab.y})")

if __name__ == "__main__":
    main()