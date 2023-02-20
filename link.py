class LINK:
    def __init__(self, name, center, position, x, y, z, faces, prevConnect):
        self.name = name
        self.center = center
        self.position = position
        self.x = x
        self.y = y
        self.z = z
        # 6 element array, with 1 meaning connected and 0 meaning free, in order of +x -x +y -y +z -z
        self.faces = faces
        # The link you are connecting to with the face of that link and the face of this link
        self.prevConnect = prevConnect
        pass

    def set_faces(self, faces):
        self.faces = faces
    
    def __str__(self):
        return "Name: " + self.name + ", Center: " + str(self.center) + ", Position " + str(self.position) + ", Length: " + str(self.x) + ", Width: " + str(self.y) + ", Height: " + str(self.z) + ", Connected To: " + str(self.prevConnect)