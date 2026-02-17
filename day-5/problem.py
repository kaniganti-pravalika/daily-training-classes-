def expences_tracker(expences):
    total_expences=0
    for expence in expences:
        total_expences+=expence
    return total_expences
expences=[100,200,300,400]
total=expences_tracker(expences)
max_expence=max(expences)
min_expence=min(expences)
print("Total expences:",total)
print("Maximum expence:",max_expence)
print("Minimum expence:",min_expence)