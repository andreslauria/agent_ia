import os

def get_files_info(working_directory, directory=None):
    
    if directory == None:
        directory = working_directory
        
    if not os.path.abspath(directory).startswith(os.path.abspath(working_directory)):
        return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
    
    if not os.path.isdir(os.path.abspath(directory)):
        return f'Error: "{directory}" is not a directory'
    
    
    try:
        dir_list = os.listdir(os.path.abspath(directory))
    except Exception as e:
        return f"Error: {e}"
    
    content = []
    
    for obj in dir_list:
        name = obj
        try:
            file_size = os.path.getsize(os.path.join(os.path.abspath(directory), obj))
        except Exception:
            file_size = -1
        
        try:
            is_dir = os.path.isdir(os.path.join(os.path.abspath(directory), obj))
        except Exception:
            is_dir = False
        
        content.append(f"- {name}: file_size={file_size} bytes, is_dir={is_dir}")
    
    
    return '\n'.join(content)