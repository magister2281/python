import os

def log_reading(func):
    def wrapper(*args):
      result = func(*args)
      for file in result:
          if file[-4::] == ".log":
              file = open(file, 'r')
              print(file.read())
      return result
    return wrapper


@log_reading
def get_files(dir):
    file_list = os.listdir(dir)
    return file_list


result = get_files(r'D:\dec\venv')
print(result)

