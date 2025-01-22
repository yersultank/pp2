#data types
#text type: str
#numeric types: int, float, complex
#sequence types: list, tuple, range
#mapping type: duct
#set types: set, frozenset
#boolean type: bool
#binary types: bytes, bytearray, memoryview
#none type: NoneType
x=5
print(type(x))

x="hello world"
print(type(x))

x=20.5
print(type(x))

x=1j
print(type(x))

x=[1,2,3,4,5,6,7]
print(type(x))

x=("apple","orange","kiwi")
print(type(x))

x=frozenset({"apple","orange","kiwi"})
print(type(x))

x=True
print(type(x))

x=b"hi"
print(type(x))

x=bytearray(5)
print(type(x))

x=memoryview(bytes(5))
print(type(x))

x=None
print(type(x))

# we can specify the data types:
print("************")

x = str("Hello World")
print(type(x))

x = int(20)
print(type(x))

x = float(20.5)
print(type(x))

x = complex(1j)
print(type(x))

x = list(("apple", "banana", "cherry"))
print(type(x))

x = tuple(("apple", "banana", "cherry"))
print(type(x))

x = range(6)
print(type(x))

x = dict(name="John", age=36)
print(type(x))

x = set(("apple", "banana", "cherry"))
print(type(x))

x = frozenset(("apple", "banana", "cherry"))
print(type(x))

x = bool(5)
print(type(x))

x = bytes(5)
print(type(x))

x = bytearray(5)
print(type(x))

x = memoryview(bytes(5))
print(type(x))

x = {"name" : "John", "age" : 36}
print(type(x))