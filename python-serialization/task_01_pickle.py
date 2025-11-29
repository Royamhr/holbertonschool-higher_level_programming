import pickle


class CustomObject:

    def __init__(self, name, age, is_student):
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        print("Name: {}".format(self.name))
        print("Age: {}".format(self.age))
        print("Is Student: {}".format(self.is_student))

    def serialize(self, filename):
        with open(filename, 'wb') as f:
            result = pickle.dumps(self)
            f.write(result)

    @classmethod
    def deserialize(cls, filename):
        try:
            with open(filename, 'rb') as f:
                result = pickle.load(f)
                return result
        except Exception:
            return None
