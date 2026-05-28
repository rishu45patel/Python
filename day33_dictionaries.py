
info={"name":"ritesh","age":24,"eligible":True}
print(info)



info={"name":"ritesh","age":24,"eligible":True}
print(info["name"])
print(info.get("name"))

print(info.keys())
for key in info.keys():
    print(info[key])



print(info.values())
for key in info.keys():
    print(f"the value corresponding to the key{key} is {info[key]}")

print("\n")

info={"name":"ritesh","age":24,"eligible":True}
print(info.items())
for key, value in info.items():
    print(f"the value corresponding to the key{key} is {value}")





































