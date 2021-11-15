contacts = {
    "number":4,
    "students":
    [
        {"name":"John Doe", "email":"john@test.com"},
        {"name":"Jane Doh", "email":"jane@test.com"},
        {"name":"JR Dow", "email":"jr@test.com"}
    ]
}

for student in contacts["students"]:
    print(student["email"])