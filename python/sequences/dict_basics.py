student = {
    "name": "Samriddhi",
    "age": 20,
    "course": "BCA"
}
print("Dictionary:", student)
print("Name:", student["name"])
print("Age:", student.get("age")) 
# Update
student["age"] = 21
student["year"] = "3rd"
print("After update:", student) 
# Delete
del student["year"]
print("After delete:", student) 
# Loop through dictionary
for key, value in student.items():
    print(key, "->", value)
print("All keys:", list(student.keys()))
print("All values:", list(student.values()))