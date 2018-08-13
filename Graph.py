import collections

import TravelAdvisor

from TravelAdvisor import Route

import functools

from Heap import Heap

import haversine

import pprint


class Graph(object):

	#Hash-table Implementation of undirected graph 

	def __init__(self):

		#Map each node to a set of nodes connected to IT 

		self._neighbours = collections.defaultdict(set)

	def connect(self,node1,node2):

		self._neighbours[node1].add(node2)
		self._neighbours[node2].add(node1)


	def neighbours(self,node):
		return self._neighbours[node]





	@classmethod
	def load(cls):
		''' Return a populated graph with real airports and routs ''' 

		world = cls()

		for flight in TravelAdvisor.get_flights():
			try : 
				origin = TravelAdvisor.AIRPORTS[flight.origin]

				destination = TravelAdvisor.AIRPORTS[flight.destination]

				world.connect(origin,destination)


			except : 
				continue 

		return world 

	@staticmethod
	@functools.lru_cache()
	def get_price(origin,destination, dollars_per_km = 0.1):

		#haversine distance , in kilometers
		point1 = origin.latitude , origin.longitude
		point2 = destination.latitude , destination.longitude

		distance = haversine.haversine(point1,point2)

		return distance 


	def dijkstra(self,origin,destination):

		#Use the dijkstra Algorithm to find the cheapest path 

		routes = Heap()

		for neighbour in self.neighbours(origin):

			price = self.get_price(origin,neighbour)

			routes.push(Route(price = price , path = [origin , neighbour]))

		visited = set()

		visited.add(origin)

		while routes : 

			#Find the nearest not-visited airport 
			price,path = routes.pop()

			airport = path[-1]

			if airport in visited : 
				continue 


			if airport is destination : 
				return price,path


			for neighbour in self.neighbours(airport):
				if neighbour not in visited : 
					#Total spent so far plus the price of gettig there 
					new_price = price + self.get_price(airport , neighbour)
					#app_price = new_price + exp
					new_path = path + [neighbour]

					routes.push(Route(new_price,new_path))
					#pprint.pprint(routes)


			visited.add(airport)

		return float('infinity')












