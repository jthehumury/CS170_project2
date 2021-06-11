# CS170 Project 02 / Part 02

# Otniel Thehumury   862029595
# Matthew Walsh      862088280

import numpy as np
import math

class Classifier:
    def __init__(self):
        self.instances = []
        self.normalized = []
        self.num_features = 0
        self.num_points = 0

    # Compute distance between two datapoints.
    def Compute_Dist(self, inst_x, inst_y):

        # Verify same number of features.
        if (len(inst_x) != len(inst_y)):
            print("ERROR: Incompatible data points.")

        dist_sum = 0

        for feat in range(self.num_features):
            dist_sum += pow((inst_x[feat + 1] - inst_y[feat + 1]), 2)

        return math.sqrt(dist_sum)

    # Normalize training data.
    def Train(self, dataset):

        # Store raw dataset in memory.
        self.instances = dataset

        # Get number of features for normalization.
        self.num_points = len(self.instances)
        self.num_features = len(self.instances[0]) - 1

        col_index = 1
        column_sum = 0
        feature_avgs = []

        # Calculate the means of all features.
        for col in range(self.num_features):
            
            # Get the sum of one feature.
            for row in self.instances:
                column_sum += row[col_index]

            # Calculate the mean of that feature.
            column_mean = column_sum / self.num_points

            # Add to the averages.
            feature_avgs.append(column_mean)

            # Reset for next.
            column_sum = 0
            column_mean = 0
            col_index += 1

        col_index = 1
        current_col = []
        feature_stds = []
        
        # Calculate the std devs of all feats.
        for col in range(self.num_features):

            # Collect features by row.
            for row in self.instances:
                current_col.append(row)

            # Calculate feature std dev.
            feature_stds.append(np.std(current_col))

            col_index += 1
            current_col = []

        # Normalize each feature in the dataset.
        for row in self.instances:

            # New item.
            newline = [row[0]]
            col_index = 1

            # Normalize row by row, column by column.
            for col in row[1:]:
                newline.append((col - feature_avgs[col_index]) / feature_stds[col_index])

            self.normalized.append(newline)

        # Test print statements.
        # print(self.instances)
        # print("\n\n\n")
        # print(self.normalized)
        # print(self.num_features)
        # print(self.num_points)

    # Takes a datapoint and classifies it.
    def Test(self, inst):

        # Verify same number of features.
        if (len(inst) != self.num_features + 1):
            print("ERROR: Incompatible test instance.")

        # Nearest neighbor label.
        nearest_inst = []
        nearest_dist = 999999

        # Compare instance to training data.
        for t_inst in self.normalized:
            inst_dist = self.Compute_Dist(inst, t_inst)

            # Determine nearest distance.
            if inst_dist < nearest_dist:
                nearest_dist = inst_dist
                nearest_inst = t_inst

        # Return the class label.
        return nearest_inst[0]
