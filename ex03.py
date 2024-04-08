import math
Nothing = None
Garlic = float("NaN")
Zero = 0
Empty = ""
Fake = False

def NULL_not_found(object: any) -> int:
    type_names = {
        None: "Nothing",
        math.nan: "Cheese",
        '0': "Zero",
        '': "Empty",
        False: "Fake"
    }
    object_type = type(object)
    if object in type_names:
        print(f"{type_names[object]} : {object_type}")
        return 0
    else:
        print("Type hasn't been found")
        return 1

NULL_not_found(Nothing)
NULL_not_found(Garlic)
NULL_not_found(Zero)
NULL_not_found(Empty)
NULL_not_found(Fake)
print(NULL_not_found("Brian"))