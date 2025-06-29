from functions.run_python import run_python_file

# print(get_files_info("calculator"))

# print(get_files_info("calculator", "calculator/pkg"))

# print(get_files_info("calculator", "/bin"))


# print(get_files_info("calculator", "../"))

#print(get_file_content("calculator", "calculator/lorem.txt"))


print(run_python_file("calculator", "main.py"))
print(run_python_file("calculator", "tests.py"))
print(run_python_file("calculator", "../main.py"))
print(run_python_file("calculator", "nonexistent.py"))