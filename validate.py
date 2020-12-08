
import os, json
import pandas as pd
import sys
import jsonschema
from jsonschema import validate

#просмотр схемы
# print(schema)
# print("Pretty-printed schema:")
# print(json.dumps(schema, indent=4))

#просмотр данных
# print(data)
# print("Pretty-printed input data:")
# print(json.dumps(data, indent=4))


#ищем файлы в папке заканчивающиеся на json и делаем список
path_to_json = 'C:\\Users\\SS\\PycharmProjects\\test\\event'
json_files = [pos_json for pos_json in os.listdir(path_to_json) if pos_json.endswith('.json')]
print(json_files[1])

#ищем файлы в папке заканчивающиеся на schema и делаем список
path_to_json = 'C:\\Users\\SS\\PycharmProjects\\test\\schema'
schema_files = [pos_json for pos_json in os.listdir(path_to_json) if pos_json.endswith('.schema')]
print(schema_files[1])

#цикл должен проходиться по каждому файлу из списка и делать валидацию, сохраняя лог
for i in range(len(json_files)):
    #обращаемся к файлу json
    shemaPath = open('C:\\Users\\SS\\PycharmProjects\\test\\schema\\' + schema_files[1]  + '',)
    schema = json.load(shemaPath)
    #обращаемся к файлу schema
    eventPath = open('C:\\Users\\SS\\PycharmProjects\\test\\event\\' + json_files[i] + '',)
    data = json.load(eventPath)
    #валидируем данные
    for idx, item in enumerate(data):
        try:
            validate(item, schema)
            sys.stdout.write("Record #{}: OK\n".format(idx))
        except jsonschema.exceptions.ValidationError as ve:
            sys.stderr.write("Record #{}: ERROR\n".format(idx))
            sys.stderr.write(str(ve) + "\n")
        old_stdout = sys.stdout

        log_file = open(f"message.log", "w")

        sys.stdout = log_file

        print
        "this will be written to message.log"

        sys.stdout = old_stdout

        log_file.close()





