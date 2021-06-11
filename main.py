# CS170 Project 02 / Part 02

# Otniel Thehumury   862029595
# Matthew Walsh      862088280

from classifier import Classifier
from validator import Validator
import random

class Problem:
    def __init__(self):
        self.depth = 1
        self.is_best = False

    # Prints features in correct format.
    def print_features(self, features):
        if not features:
            return "{}"
        result = "{"
        for i in range(len(features)):
            result += str(features[i])
            if i < len(features) - 1:
                result += ","
            else:
                result += "}"
        return result

    # Forward selection.
    def forward_selection(self, num_features):

        # Starting with no features.
        max_fitness = ([], round(random.uniform(0,100),2))

        print("Using no features and \"random\" evaluation, I get an accuracy of " + str(max_fitness[1]) + "%\n")
        
        while True:

            # Resets to True each outter loop.
            self.is_best = True

            # Greedy choice from previous evaluation.
            base = max_fitness[0]

            # For every feature.
            for i in range(1, num_features + 1):
                if i in base:
                    continue
                base.append(i)

                # TODO: Integrate validator.

                # Create random accuracy for feature(s).
                fitness = (list(base), round(random.uniform(0,100),2))
                print("Using feature(s) " + self.print_features(fitness[0]) + " accuracy is " +str(fitness[1]) + "%")
                
                # Tracks most accurate feature(s).
                if fitness[1] > max_fitness[1]:
                    self.is_best = False
                    max_fitness = fitness
                base.pop()

            print("")

            # If local max:
            if self.is_best:
                print("(Warning, accuracy has decreased!)")
                break

            # If max depth is reached:
            if self.depth == num_features:
                break
            self.depth +=1
            print("Feature set " + self.print_features(max_fitness[0]) + " was best, accuracy is " + str(max_fitness[1]) + "%\n")
        print("Finished search!!! The best feature subset is " + self.print_features(max_fitness[0]) + ", which has an accuracy of " + str(max_fitness[1]) + "%\n")

    # Backward elimination.
    def backward_elimination(self, num_features):

        # Convert num_features so it works on Matt's machine.
        num_features = int(num_features)

        # Starting with all features:
        max_fitness = ([i for i in range(1, num_features + 1)], round(random.uniform(0,100),2))

        print("Using features " + self.print_features(max_fitness[0]) + ", I get an accuracy of " + str(max_fitness[1]) + "%\n")
        
        while True:

            # Resets to True each outter loop.
            self.is_best = True

            # Greedy choice from previous evaluation.
            base = max_fitness[0]

            # For every feature:
            for i in range(1, num_features + 1):
                if i not in base:
                    continue
                base.remove(i)

                # Create random accuracy for feature(s).
                fitness = (list(base), round(random.uniform(0,100),2))
                print("Using feature(s) " + self.print_features(fitness[0]) + " accuracy is " +str(fitness[1]) + "%")

                # Tracks most accurate feature(s).
                if fitness[1] > max_fitness[1]:
                    self.is_best = False
                    max_fitness = fitness
                base.append(i)
            print("")

            # If local max:
            if self.is_best:
                print("(Warning, accuracy has decreased!)")
                break

            # If max depth is reached:
            if self.depth == num_features:
                break
            self.depth +=1
            print("Feature set " + self.print_features(max_fitness[0]) + " was best, accuracy is " + str(max_fitness[1]) + "%\n")
        print("Finished search!!! The best feature subset is " + self.print_features(max_fitness[0]) + ", which has an accuracy of " + str(max_fitness[1]) + "%\n")

# Read in the dataset.
def read_dataset():

    # Prompt user with dataset options.
    print("--------------------------------------")
    print("\nWhich dataset would you like to use?\n")
    print("1) Small Dataset #80")
    print("2) Large Dataset #80")
    print("---------------------")
    print("3) Small Dataset #98")
    print("4) Large Dataset #98")
    print("---------------------")
    print("5) Small Dataset #107")
    print("6) Large Dataset #107")

    # Read user input and convert to an integer.
    data_choice = input("\nEnter dataset choice: ")
    data_choice = int(data_choice)

    if data_choice == 1:
        filename = 'cs_170_small80.txt'

    elif data_choice == 2:
        filename = 'cs_170_large107.txt'

    elif data_choice == 3:
        filename = 'cs_170_small98.txt'

    elif data_choice == 4:
        filename = 'cs_170_large98.txt'

    elif data_choice == 5:
        filename = 'cs_170_small107.txt'

    else:
        filename = 'cs_170_large107.txt'

    # Dataset to return.
    dataset = []

    # Read each line as new datapoint.
    with open(filename) as file:
        for line in file:

            # New item.
            newline = []

            # Following items are features.
            for word in line.split():

                # Split value by 'e'.
                split_val = word.split("e", 1)
                val = float(split_val[0])

                # Get exponent value.
                exp = float(split_val[1][1:4])
                if (split_val[1][0] == '-'):
                    exp = exp * (-1)

                # Calculate val with exp.
                calc = val * pow(10, exp)
                newline.append(calc)

            # Add line to instances as onject.
            dataset.append(newline)

    return dataset

# GUI Functions:
def intro():

    print("\n--------------------------------------")
    print("CS170 Project 02 / Part 02\n")
    print("Otniel Thehumury 862029595")
    print("Matthew Walsh    862088280")
    print("--------------------------------------")

    # Collect the number of features from the user.
    # num_features = input("Please enter total number of features: ")

    # print("\nType the number of the algorithm you want to run.")
    # print("\n1) Forward Selection")
    # print("\n2) Backward Elimination")
    # print("\n3) NN Classifier")

    # choice = input("\nHere: ")
    # choice = int(choice)

    # Project 2, Part 2:
    choice = 3

    print("")
    p = Problem()

    if choice == 1:
        print("Chosen Forward Elimination")
        # p.forward_selection(num_features)

    elif choice == 2:
        print("Chosen Backward Elimination")
        # p.backward_elimination(num_features)

    elif choice == 3:
        print("Nearest Neighbor Classifier:\n")

        training_data = read_dataset()

        print("Please select a feature subset.\n")
        print("For example, type: 1 3 5 7 9")
        print("Enter zero or blank for all features.\n")
        sub_input = input("Enter your choice here: ")

        # Separate input into int list.
        subset = []
        for feat in sub_input.split():
            subset.append(int(feat))

        # Zero indicates all features.
        if sub_input == "":
            subset = [0]

        # Train the classifier.
        c = Classifier()
        c.Train(training_data)
        # c.Test([2.0, 2.1530859, 4.4095784, 3.6216757, 3.8451064, 2.9807186, 2.0171732, 0.5397355, 3.3933456, 2.2950856, 3.0431002])
        
        # Implement validator.
        v = Validator(c)
        print(v.Validate(subset))

    else:
        print("Incorrect choice - closing program.")

intro()
