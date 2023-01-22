# Acquaintance
import random

# ky-ky

name = input("Enter your name: ")

def rt_read_file():

    content = ''
    with open("words.txt", "r") as file:
        content = file.read()
    return content

def write_file(name, point):

    with open("history.txt", "a") as file:
        file.write(f"{name}:{point}")
        file.write(f"\n")

def words_for_test(string):

    clean_str = string.split("\n")
    answers = []
    for i in clean_str:
        answers.append(''.join(random.sample(i, len(i))))

    return answers

def start_play(dic_words):

    answers = rt_read_file().split("\n")
    point = 0
    for count, i in enumerate(dic_words):
        print(f"Write true word: {i}")
        answer = input()
        if answer == answers[count]:
            point += 10
    write_file(name, point)

def get_status_history(name):

    content = ''
    count_pley = 0
    max_result = 0
    temp = 0
    with open("history.txt", "r") as file:
        content = file.read().split("\n")

    for i in content:
        if i.split(":").count(name):
            count_pley += 1
            temp = i.split(":")
            if int(temp[1]) >= max_result:
                max_result = int(temp[1])

    print(count_pley)
    print(max_result)

start_play(words_for_test(rt_read_file()))
get_status_history(name)
