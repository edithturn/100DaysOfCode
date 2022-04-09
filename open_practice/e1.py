from pytest_httpx import to_response


list_of_words = ["hello", "yes", "goodbye", "last"]
to_print = ""

for i in range(len(list_of_words)):
    to_print += list_of_words[i]
    if i != len(list_of_words) - 1:
        to_print += ","

print(list_of_words[0]+"."+list_of_words[1]+"."+list_of_words[2]+"."+list_of_words[3])