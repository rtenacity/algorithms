from collections import deque
graph = {}
graph["you"] = ["alice", "bob", "claire"]
graph["bob"] = ["anuj", "peggy"]
graph["alice"] = ["peggy"]
graph["claire"] = ["thom", "jonny"]
graph["anuj"] = []
graph["peggy"] = []
graph["thom"] = []
graph["jonny"] = []

## SHORTER VERSION FROM WHAT IS IN THE BOOK ##

def person_is_seller(name):
    return name[-1] == 'm'

search_queue = deque()
search_queue += graph["you"]

while search_queue:
    person = search_queue.popleft()
    if person_is_seller(person):
        print(person, "is a mango seller")
    else:
        search_queue += graph[person]
