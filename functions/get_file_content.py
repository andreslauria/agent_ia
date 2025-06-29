import os


def get_file_content(working_directory, file_path):
    MAX_CHARS = 10000
    
    if not os.path.abspath(file_path).startswith(os.path.abspath(working_directory)):
        return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
    
    if not os.path.isfile(os.path.abspath(file_path)):
        return f'Error: File not found or is not a regular file: "{file_path}"'
    try:
        with open(file_path, "r") as f:
            file_content_string = f.read(MAX_CHARS)
            
            next_char = f.read(1)
            if next_char:
                file_content_string += '[...File "{file_path}" truncated at 10000 characters]'
        
    except Exception as e:
        return f'Error: {e}'
        
    return file_content_string