# Create a dictionary with some key-value pairs
d={"name":"Alice","age":25,"city":"new yourk"}
d["gender"]="fenale"
d.update({"country":"USA"})
print(d.get("age"))
print(d.pop("city"))
print(d.popitem())
print(d.keys())
print(d.values())
print(d.items())
print(d.setdefault("email","alice@example.com"))
d.clear()
print(d)
#
d={'a':10,'b':70,'c':30}
print(len(d))
