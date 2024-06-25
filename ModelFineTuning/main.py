import json

import ollama
import time

chat = []


def make_request(prompt):
    start_time = time.time()
    chat.append({"role": "user", "content": prompt})
    v = ollama.chat(
        model="myDbAdmin",
        messages=chat,
        format="json",
        stream=False
    )
    print(v["message"])
    chat.append({"role": "assistant", "content": v["message"]["content"]})

    end_time = time.time()
    response_time = end_time - start_time

    print(f"Response time for '{prompt}': {response_time:.4f} seconds")


#time these functions to see the time it takes to respond to each prompt with the ollama model
make_request("create a db model for a college")
make_request("add current grade to student table")
make_request("add last name also to student table")
make_request("just keep name in student table")
make_request("create a databse for a travel agency employees")
