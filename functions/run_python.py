import os
import subprocess

def run_python_file(working_directory, file_path):
    working_path = os.path.abspath(working_directory)
    full_path = os.path.abspath(os.path.join(working_path, file_path))

    if not full_path.startswith(working_path):
        return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
    
    root_ext = os.path.splitext(file_path)
    if root_ext[1] != ".py":
        return f'Error: "{file_path}" is not a Python file.'
    
    if not os.path.exists(file_path):
        return f'Error: File "{file_path}" not found.'
    
    try:
        result = subprocess.run(
            ["python3", file_path],
            cwd=working_path,
            capture_output=True,
            text=True,
            timeout=30
        )

        output: list[str] = []

        if result.stdout:
            output.append(f"STDOUT:\n{result.stdout.strip()}")
        if result.stderr:
            output.append(f"STDERR:\n{result.stderr.strip()}")

        if result.returncode != 0:
            output.append(f"Process exited with code {result.returncode}")

        return "\n".join(output) if output else "No output produced."
    except Exception as e:
        return f"Error: executing Python file: {e}"