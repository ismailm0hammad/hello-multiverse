code = '"hello" + "world"'
result = eval(code)
print(result) # Output: "hello world"

code = '["a", "b", "c"][1]'
result = eval(code)
print(result) # Output: "b"

import types

code_string = "a = 6+5"
my_namespace = types.SimpleNamespace()
exec(code_string, my_namespace.__dict__)
print(my_namespace.a) # 11