# ERROR AND EXCEPTION
x = -5
# using the raise
if x < 0:
    raise Exception('X should be positive')

# using the assert
assert (x >= 0), 'X should be positive'

# using try catch else finally
try:
    a = 5/0
except Exception as e:
    print(f"the error is [ {e} ]")

# its always better to write the name of the exception
try:
    a = 9+"hi"
except TypeError as e:
    print(e)

# its always better to write the name of the exception
try:
    a = 9+89
except TypeError as e:
    print(e)
else:
    print("everything is fine --- NO ERRORS---")
finally:
    print("cleaning up..............")


# creating our own exception
class valuestoohigherror(Exception):
    
    def __init__(self,message,value):
        self.message=message
        self.value=value

def val(x):
    if x > 50:
        raise valuestoohigherror("high values =",x)

try:
    val(78)
except valuestoohigherror as e:
    print(e.message,e.value)
