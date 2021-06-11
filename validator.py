# CS170 Project 02 / Part 02

# Otniel Thehumury   862029595
# Matthew Walsh      862088280

from classifier import Classifier
import numpy as np

class Validator:
    def __init__(self, cls):
        self.classifier = cls

    # Returns classifier accuracy.
    def Validate(self, subset):

        # Ensure that given the subset is valid.
        for feat in subset:
            if (0 > feat) or (feat > self.classifier.num_features):
                print("ERROR: Subset does not match features.")
                return 0

        # K-fold vars.
        num_correct = 0

        # Perform k-fold cross validation.
        for leave_out in range(self.classifier.num_points):

            # Reset each fold.
            row_index = 0

            for row in self.classifier.normalized:
                
                if row_index == leave_out:
                    # print(row_index)
                    continue

                row_index += 1

        return 0