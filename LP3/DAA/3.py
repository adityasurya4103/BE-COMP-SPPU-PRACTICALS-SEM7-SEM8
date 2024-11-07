class ItemValue:
    """Item Value DataClass"""

    def __init__(self, wt_, val_, ind_):
        self.wt = wt_
        self.val = val_
        self.ind = ind_
        self.cost = val_ / wt_

    def __lt__(self, other):
        return self.cost < other.cost


def fractionalKnapSack(wt, val, capacity):
    """Function to get maximum value in Knapsack"""
    iVal = [ItemValue(wt[i], val[i], i) for i in range(len(wt))]

    # sorting items by value/weight ratio in descending order
    iVal.sort(key=lambda x: x.cost, reverse=True)

    totalValue = 0
    for i in iVal:
        curWt = i.wt
        curVal = i.val
        if capacity - curWt >= 0:
            capacity -= curWt
            totalValue += curVal
        else:
            fraction = capacity / curWt
            totalValue += curVal * fraction
            break
    return totalValue


if __name__ == "__main__":
    # Taking user input
    n = int(input("Enter the number of items: "))

    wt = []
    val = []
    
    for i in range(n):
        w = float(input(f"Enter weight of item {i + 1}: "))
        v = float(input(f"Enter value of item {i + 1}: "))
        wt.append(w)
        val.append(v)

    capacity = float(input("Enter the capacity of the knapsack: "))

    # Function call
    maxValue = fractionalKnapSack(wt, val, capacity)
    print("Maximum value in Knapsack =", maxValue)
