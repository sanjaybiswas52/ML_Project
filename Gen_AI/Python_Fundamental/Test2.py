import gc

class Sample:
    def __init__(self, name):
        self.name = name
        print(f"Object {self.name} created.")

    def __del__(self):
        print(f"Object {self.name} destroyed.")

# Create a function to demonstrate garbage collection
def garbage_collection_demo():
    # Create two objects
    obj1 = Sample("Object1")
    obj2 = Sample("Object2")

    # Create a circular reference
    obj1.ref = obj2
    obj2.ref = obj1

    # Delete references to the objects
    print("\nDeleting objects...")
    del obj1
    del obj2

    # Manually run garbage collection
    print("\nRunning garbage collection...")
    collected = gc.collect()  # Returns the number of unreachable objects collected
    print(f"Garbage collector collected {collected} objects.")

# Call the function
garbage_collection_demo()

print("\nExiting program...")