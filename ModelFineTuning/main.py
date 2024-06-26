import time

import ollama

chat = []


def make_request(prompt):
    start_time = time.time()
    chat.append({"role": "user", "content": prompt})
    v = ollama.chat(model="myDbAdmin", messages=chat, format="json", stream=False)
    print(v["message"])
    chat.append({"role": "assistant", "content": v["message"]["content"]})

    end_time = time.time()
    response_time = end_time - start_time

    print(f"Response time for '{prompt}': {response_time:.4f} seconds")


# import json
# s = json.loads('{"database":{\n"name":"college_db",\n"tables":[\n  {\n    "name":"students",\n    "columns":[\n      {"name":"student_id","type":"int","constraints":["primary key","auto increment"]},\n      {"name":"first_name","type":"varchar(100)","constraints":["not null"]},\n      {"name":"last_name","type":"varchar(100)","constraints":["not null"]},\n      {"name":"email","type":"varchar(255)","constraints":["unique"]}\n    ],\n    "foreign_keys":[]\n  },\n  {\n    "name":"courses",\n    "columns":[\n      {"name":"course_id","type":"int","constraints":["primary key","auto increment"]},\n      {"name":"course_name","type":"varchar(100)","constraints":["not null"]},\n      {"name":"department","type":"varchar(50)","constraints":["not null"]}\n    ],\n    "foreign_keys":[]\n  },\n  {\n    "name":"enrollments",\n    "columns":[\n      {"name":"enrollment_id","type":"int","constraints":["primary key","auto increment"]},\n      {"name":"student_id","type":"int","constraints":["not null"]},\n      {"name":"course_id","type":"int","constraints":["not null"]},\n      {"name":"enrollment_date","type":"date","constraints":["not null"]}\n    ],\n    "foreign_keys":[\n      {"student_id":"students.student_id"},\n      {"course_id":"courses.course_id"}\n    ]\n  }\n]}}')
# print(json.dumps(s))

# time these functions to see the time it takes to respond to each prompt with the ollama model
make_request("create a db model for a college")
make_request("add current grade to student table")
make_request("add last name also to student table")
make_request("just keep name in student table")
make_request("create a databse for a travel agency employees")
