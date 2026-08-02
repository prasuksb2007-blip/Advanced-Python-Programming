class singleton:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            print("Creating the object...")
            cls._instance=super().__new__(cls)
        return cls._instance
#Creating objects
obj1=singleton()
obj2=singleton()
print(obj1)
print(obj2)
print(obj1 is obj2)