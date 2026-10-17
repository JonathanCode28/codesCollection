import pickle

names = ["elton john", "eminem", "drake", "eminem"] #list
color = ("blue", "yellow", "skyblue", "blue") #tuple
my_dict = {
    "key": "value",
    "name": "h.potter",
    "level": 4,
    "power": "survive",
    "xp": 100,
}
print(my_dict["key"])
my_dict["level"] = 5
print(my_dict["level"])

my_dict.update(level=10, xp=0, name="albus", power="smart")
my_dict_pickle = pickle.dumps(my_dict)
my_dict_unpickle = pickle.loads(my_dict_pickle)
print(my_dict_unpickle)
print(my_dict_pickle)
print(my_dict)