import random

class Problem:
    def __init__(self):
        self.depth = 1
        self.is_best = False

    #Prints features in correct format
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

    # Forward selection
    def forward_selection(self, num_features):

        # Starting with no features
        max_fitness = ([], round(random.uniform(0,100),2))

        print("Using no features and \"randon\" evaluation, I get an accuracy of " + str(max_fitness[1]) + "%\n")
        
        while True:

            # Resets to True each outter loop
            self.is_best = True

            # Greedy choice from previous evaluation
            base = max_fitness[0]

            # For every feature
            for i in range(1, num_features + 1):
                if i in base:
                    continue
                base.append(i)

                # Create random accuracy for feature(s)
                fitness = (list(base), round(random.uniform(0,100),2))
                print("Using feature(s) " + self.print_features(fitness[0]) + " accuracy is " +str(fitness[1]) + "%")
                
                # Tracks most accurate feature(s)
                if fitness[1] > max_fitness[1]:
                    self.is_best = False
                    max_fitness = fitness
                base.pop()
            print("")

            # if local max
            if self.is_best:
                print("(Warning, accuracy has decreased!)")
                break

            # if max depth is reached
            if self.depth == num_features:
                break
            self.depth +=1
            print("Feature set " + self.print_features(max_fitness[0]) + " was best, accuracy is " + str(max_fitness[1]) + "%\n")
        print("Finished search!!! The best feature subset is " + self.print_features(max_fitness[0]) + ", which has an accuracy of " + str(max_fitness[1]) + "%\n")

    # Backward elimination
    def backward_elimination(self, num_features):

        # Starting with all features
        max_fitness = ([i for i in range(1, num_features + 1)], round(random.uniform(0,100),2))

        print("Using features " + self.print_features(max_fitness[0]) + ", I get an accuracy of " + str(max_fitness[1]) + "%\n")
        
        while True:

            # Resets to True each outter loop
            self.is_best = True

            # Greedy choice from previous evaluation
            base = max_fitness[0]

            # For every feature
            for i in range(1, num_features + 1):
                if i not in base:
                    continue
                base.remove(i)

                # Create random accuracy for feature(s)
                fitness = (list(base), round(random.uniform(0,100),2))
                print("Using feature(s) " + self.print_features(fitness[0]) + " accuracy is " +str(fitness[1]) + "%")

                # Tracks most accurate feature(s)
                if fitness[1] > max_fitness[1]:
                    self.is_best = False
                    max_fitness = fitness
                base.append(i)
            print("")

            # if local max
            if self.is_best:
                print("(Warning, accuracy has decreased!)")
                break

            # if max depth is reached
            if self.depth == num_features:
                break
            self.depth +=1
            print("Feature set " + self.print_features(max_fitness[0]) + " was best, accuracy is " + str(max_fitness[1]) + "%\n")
        print("Finished search!!! The best feature subset is " + self.print_features(max_fitness[0]) + ", which has an accuracy of " + str(max_fitness[1]) + "%\n")

# GUI Functions
def intro():
    num_features = input("Please enter total number of features: ")

    print("\nType the number of the algorithm you want to run.")

    print("\n1) Forward Selection")

    print("\n2) Backward Elimination")

    choice = input("\nHere: ")
    print("")
    p = Problem()
    if choice == 1:
        p.forward_selection(num_features)
    else:
        p.backward_elimination(num_features)

intro()