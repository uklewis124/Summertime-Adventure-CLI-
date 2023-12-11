import pickle

time = "12:00"

students = {
    "Dan": {"Age": 50, "test": True},
    "Sam": {"Age": 35, "test": False}
}

dict2 = {
    "test":1,
    "test2":5
}



lister = ["fireball", "ice spear"]

array = [1,5,7]

new_save = {
    "students": students,
    "dict2": dict2,
    "time": time,
    "list": lister
}

with open('test_file.pkl', 'wb') as f:
    pickle.dump(new_save, f)
    pickle.dump(dict2, f)
    f.close()

with open('test_file.pkl', 'rb') as f:
    students_loaded = pickle.load(f)
    print(students_loaded["time"])
    time = students_loaded["time"]
    lister = students_loaded["list"]

print(new_save)


def update_dictionary(key, value, dict=new_save):
    dict[key] = value
def update_time(inp):
    time = inp

dict2.update({"test3": 10})
update_dictionary("dict2", dict2)

print(new_save)