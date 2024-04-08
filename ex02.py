ft_list = ["Hello", "tata!"]
ft_tuple = ("Hello", "toto!")
ft_set = {"Hello", "tutu!"}
ft_dict = {"Hello" : "titi!"}



def all_thing_is_obj(object: any) -> int:
    keys = {
        "tuple" : "Tuple",
        "list" : "List",
        "set" : "Set",
        "dict" : "Dictionary",
    }   
    object_key = type(object).__name__
    object_type = type(object)
    
    if object_key in keys:
        print(f"{keys[object_key]} : {object_type}")
    elif object_key == "str":
        print(f"{object} is in the kitchen : {object_type}")
    else:
        print("Type hasn't been found")
    return 42

all_thing_is_obj(ft_list)
all_thing_is_obj(ft_tuple)
all_thing_is_obj(ft_set)
all_thing_is_obj(ft_dict)
all_thing_is_obj("Brian")
print(all_thing_is_obj(10))
