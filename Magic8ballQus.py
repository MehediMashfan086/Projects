import sys
import random

responses = ["It is certain", "You may rely on it", "As I see it,Yes",
             "Outlook looks good", "Most Likely", "It is deciely so", "Without a doubt", "Yes Definetly"]

questions = True

while questions:
    qus = input("Please ask the magic 8 ball a question: ")
    if qus == "":
        sys.exit()
    else:
        print(responses[random.randint(0, 7)])