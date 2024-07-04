# Open the file and read its contents using the implicity method, and passing in the absolute file path
with open('/Users/reliablespine/learn_python/file_handling.py/DOB.txt', 'r', encoding='utf-8') as file: #the word file here is a temporary variable and could be anything, x,y,z etc
    data = file.readlines()

# Split the data into two sections
first_section = data[:5]
second_section = data[5:]

# Print the sections
print("First Section:")
for line in first_section:
    print(line.strip())

print("\nSecond Section:")
for line in second_section:
    print(line.strip())

#/Users/reliablespine/learn_python/file_handling.py, select the file, right click and copy the path for absolute path
#