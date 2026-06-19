text = "  Hello python world  "
 
print("Original:",text)
print("Length:", len(text))
print("Uppercase:", text.upper())
print("Lowercase:", text.lower())
print("Stripped:", text.strip())
print("Replace 'Python' with 'World'", text.replace("Python", "World"))
print("Title case:", text.strip().title())
print("Starts with 'Hello'?", text.strip().startswith("Hello"))
print("Ends with 'World'?", text.strip().endswith("World"))
print("Split into words:", text.strip().split())
print("Find index of 'Python':", text.find("python"))