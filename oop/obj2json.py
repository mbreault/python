import json

## serialize an object to json
class JsonSerializable(object):
    def toJson(self):
        return json.dumps(self.__dict__)

class Example(JsonSerializable):
    def __init__(self, fname):
        self.fname = fname

x = Example('/foo/bar')
print(x.toJson())