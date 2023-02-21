class JOINT:
    def __init__(self, name, position, parent, child, axis, face):
        self.name = name
        self.position = position
        self.parent = parent
        self.child = child
        self.axis = axis
        self.face = face
        pass
    
    def __str__(self):
        return "Name: " + self.name + ", Position: " + str(self.position) + ", Parent: " + str(self.parent) + ", Child: " + str(self.child) + ", Axis: " + str(self.axis) + ", Face: " + str(self.face)