import json

_queue = ['Gandalf','Aragorn','Legolas','Gimli']

with open('queue.json','w') as jfile:
  json.dump(_queue, jfile)