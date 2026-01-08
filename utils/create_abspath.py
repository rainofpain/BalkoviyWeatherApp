import os

def create_abspath(path: str):
    try:
        path_elements_list = path.split('/')
        
        base_path = os.path.abspath(os.path.join(__file__, "..", ".."))
        
        for element in path_elements_list:
            base_path = os.path.join(base_path, element)
        
        return os.path.abspath(base_path)
    except Exception as error:
        print("\n", f"Помилка під час побудови абс. шляху: {error}", "\n")