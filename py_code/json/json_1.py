# codeing = utf-8

import json

test = {"username":"测试", "age":16}

python_to_json = json.dumps(test, ensure_ascii=False, indent = 2)
print(python_to_json)

json_to_python = json.loads(python_to_json)
print(json_to_python)