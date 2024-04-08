ft_list = ["Hello", "tata!"]
ft_tuple = ("Hello", "toto!")
ft_set = {"Hello", "tutu!"}
ft_dict = {"Hello" : "titi!"}

print(ft_list)
print(ft_tuple)
print(ft_set)
print(ft_dict)

ft_list[1] = "World"

country = "Germany"
ft_tuple = (ft_tuple[0], country)


ft_list = list(ft_set) 
ft_list.insert(1, "Wolfsburg!") 
ft_list.remove("tutu!")
ft_set = set(ft_list)


ft_dict["Hello"] = "42Wolfsburg"

print("\n")
print(ft_list)
print(ft_tuple)
print(ft_set)
print(ft_dict)

