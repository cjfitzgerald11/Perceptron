class ImageReader:
    def __init__(self,imageFile):
        self.imageFolder = imageFile
        self.images = []
        self.answers = []

    def readImages(self):
        if len(self.images) > 0:
            continue
        else:
            #read images in
            print()

    def getImages(self):
        return self.images, self.answers