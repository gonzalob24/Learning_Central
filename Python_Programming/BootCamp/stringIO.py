import io

message = "This is just a normal string"

# Use stringIO method to set as file object
f = io.StringIO(message)
print(f.read())
