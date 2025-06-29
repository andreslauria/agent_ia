import os


def write_file(working_directory, file_path, content):
    
    if not os.path.abspath(file_path).startswith(os.path.abspath(working_directory)):
        return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'
    try:
        
        target_directory = os.path.dirname(file_path)
        os.makedirs(target_directory, exist_ok=True)
        
        with open(file_path, 'w') as file:
            file.write(content)     
    
    except Exception as e:
        return f'Error: {e}'
    
    return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'