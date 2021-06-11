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

        # Make copy of the dataset for feature selection.
        # temp_normalized = self.classifier.normalized.copy()
        to_delete = []

        # Trim down to given subset.

        for col in range(self.classifier.num_features + 1)[1:]:
            if col not in subset:
                to_delete.append(col)
        
        # print(to_delete)
        # temp_normalized = np.delete(temp_normalized, to_delete, axis = 1)

        # print(temp_normalized)

        # K-fold vars.
        fold_list = []
        folded = []
        num_correct = 0

        print("\n--------------------------------------")
        print("\nPerforming k-fold cross validation.\n")

        # Perform k-fold cross validation.
        for leave_out in range(self.classifier.num_points):

            # Prepare temporary datasets for k-folding.
            fold_list = self.classifier.normalized.copy()
            folded = self.classifier.normalized[leave_out]
            print(fold_list)
            del fold_list[leave_out]
            print(fold_list)
            fold_list = np.delete(fold_list, to_delete, axis = 1)
            print(fold_list)

            # Create classifier for folded data.
            temp_c = Classifier()
            temp_c.Train(fold_list)
            result = temp_c.Test(folded)

            # Increment if classification accurate.
            if result == folded[0]:
                num_correct += 1

        return num_correct / self.classifier.num_points
