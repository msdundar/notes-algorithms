# python3

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

def search(name):
  search_queue = deque() # create a queue
  search_queue += graph[name] # add all your neighbours (alice, bob and claire) to the queue.
  searched = []

  while search_queue: # While the queue isn't empty
    person = search_queue.popleft() # dequeue the first person from queue.
    if not person in searched:
      if person_is_seller(person):
        print(person + " is a mango seller!")
        return True
      else:
        search_queue += graph[person] # Add all of this person's friends to the search queue.
        searched.append(person)
  return False

# This function checks whether the person's name ends with the letter m. If it does, they're a mango seller.
def person_is_seller(name):
  return name[-1] == 'm'

search("you")