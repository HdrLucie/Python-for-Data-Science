Nothing = None
Garlic = float("NaN")
Zero = 0
Empty = ""
Fake = False

def NULL_not_found(object: any) -> int:
    if type(object) is float:
        print("Cheese: nan", type(object))
        return 0
    elif object is Nothing:
        print("Nothing: None ", type(object))
        return 0
    elif object is Zero:
        print("Zero: 0 ", type(object))
        return 0
    elif object is Empty:
        print("Empty: ", type(object))
        return 0
    elif object is Fake:
        print("Fake: False ", type(object))
        return 0
    else:
        print("Type not Found")
        return 1
