from functions.get_file_content import get_file_content

# print(get_files_info("calculator"))

# print(get_files_info("calculator", "calculator/pkg"))

# print(get_files_info("calculator", "/bin"))


# print(get_files_info("calculator", "../"))

#print(get_file_content("calculator", "calculator/lorem.txt"))


print(get_file_content("calculator", "calculator/main.py"))

print(get_file_content("calculator", "calculator/pkg/calculator.py"))
print(get_file_content("calculator", "/bin/cat"))