name = ["Anna", "Eli", "Pariece", "Brendan", "Amy", "Shane", "Oscar"]
favorite_animal = ["horse", "cat", "spider", "giraffe", "ticks", "dolphins", "llamas"]

def make_dict(arr1, arr2):
    new_dict = {}
    if len(arr1) > len(arr2):
        new_dict = dict(zip(arr1, arr2))
    elif len(arr2) > len(arr1):
        new_dict = dict(zip(arr2, arr1))
    else:
        new_dict = dict(zip(arr1, arr2))
    print new_dict
make_dict(name,favorite_animal)
