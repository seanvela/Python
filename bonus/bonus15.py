import json

with open('questions.json', 'r') as file:
    content = file.read()

# converted to 'list' class instead of 'str' class
# data cannont be munipulated as 'str' class
data = json.loads(content)


for question in data:
    print(question["question_text"])
    for index, alternative in enumerate(question["alternatives"]):
        print(index + 1, " - ", alternative)
    
    user_choice = int(input("Enter your answer: "))
    question["user_choice"] = user_choice


# holds users score
score = 0

for index, question in enumerate(data):
    if question["user_choice"] == question["correct_answer"]:
        score = score + 1
        result = "Correct Answer"
    else:
        result = 'Wrong Answer'

    message = f"{result}! {index + 1} - Your answer: {question['user_choice']}, Correct answer is : {question['correct_answer']}"

    print(message)

print('Total score is: ', score, '/', len(data))