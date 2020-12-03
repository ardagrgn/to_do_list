from collections import deque
graph = {}
graph["you"] = ["alice","bob","claire"]
graph["bob"]= ["anuj","peggy"]
graph["alice"]=["peggy"]
graph["claire"]=["thom","jonny"]
graph["anuj"]= []
graph["peggy"]= []
graph["thom"]= []
graph["jonny"]= []

search_queue = deque()

search_queue += graph["you"]
searched = []

def last_word(name):
    return name[-1] == "y"


def search(name):
    search_queue = deque()
    search_queue += graph["you"]
    searched = []

    while search_queue :
        person = search_queue.popleft()

        if not person in searched:
            if last_word(person):
                print(f"{person} adlı bu arkadaşın son harfi 'y'dir.")
                return True
            else:
                search_queue += graph[person]
                searched.append(person)
    return False

search("you")





