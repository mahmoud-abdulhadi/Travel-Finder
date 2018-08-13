from Graph import Graph 
import TravelAdvisor
import pprint

world = Graph.load()


valencia = TravelAdvisor.AIRPORTS['VLC']

#pprint.pprint(world.neighbours(valencia))

portland = TravelAdvisor.AIRPORTS['PDX']

bristol = TravelAdvisor.AIRPORTS['BRS']

portland = TravelAdvisor.AIRPORTS['PDX']
distance,path = world.dijkstra(valencia , portland)
#print(path)
for index,airport in enumerate(path):
	print('%s| %s'%(index,airport))

print('$ %s'%(distance))

