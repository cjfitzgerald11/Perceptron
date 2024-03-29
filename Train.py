from Perceptron import Perceptron
from Node import Node

class Train:
    def __init__(self, trainImages, trainAsnwers, learningRate):
        self.learningRate = learningRate
        self.trainImages = trainImages
        self.trainAsnwers = trainAsnwers

    """Backpropagation training method. Trains the perceptron against each image
    in the file."""
    def train(self,perceptron):
        for i in range(len(self.trainImages)):
            perceptron.trainWeights(self.trainImages[i],self.trainAsnwers[i])
        return perceptron
