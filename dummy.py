json_data = '{"user":"haha","ph":"123"}'
import json
dict_data = json.loads(json_data)
dict_data.pop("user")
back_data = json.dumps(dict_data)
print(back_data)