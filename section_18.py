def input_validator(message):
    question_mark = ["what", "which", "who", "how", "when", "where"]
    capitalize_message = message.capitalize()
    for word in question_mark:
        if message.startswith(word):
            return "{}?".format(capitalize_message)
    return "{}.".format(capitalize_message)


result = []
while True:
    message = input("What is on your mind")
    if message == "\end":
        break
    else:
        result_input = input_validator(message)
        result.append(result_input)
all_input = " ".join(result)
print(all_input)
