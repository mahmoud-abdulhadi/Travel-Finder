from tkinter import * 

from tkinter import ttk 

import TravelAdvisor

from Graph import Graph

from tkinter import messagebox


countries = [airport.country for airport in TravelAdvisor.get_airports()]

def get_cities(country):

	cities = [airport.city for airport in TravelAdvisor.get_airports() if (airport.country == country)]
	cleaned_cities = set(cities)

	list_cities = sorted(list(cleaned_cities))
	return list_cities

def get_airports(city,country):

	airports = sorted([airport.code+ "-"+airport.name for airport in TravelAdvisor.get_airports() if ((airport.city == city) and (airport.country == country))])

	return airports

class TravelApp : 

	def __init__(self,master):

		self.world = Graph.load()

		master.geometry('640x480+50+50')

		master.title('Intelli Traveller')

		master.configure(background = '#4588B0')
		#master.resizable(False,False)

		self.header_frame = ttk.Frame(master)
		self.header_frame.pack(anchor='w')

		self.logo2 = PhotoImage('airplane-logo.gif')

		ttk.Label(self.header_frame,image = self.logo2).grid(row=0,column=3,rowspan=4)
		
		self.style = ttk.Style()

		self.style.configure('TLabel',font = ('Georgia',10),background = '#4588B0',foreground = 'white')
		self.style.configure('TFrame',background = '#4588B0')

		self.style.configure('Header.TLabel',font = ('Helvetica',16,'bold'),foreground = 'white')


		self.logo = PhotoImage(file = 'travel_logo.gif').subsample(2,2)

		ttk.Label(self.header_frame , image = self.logo).grid(row = 0 , column =0,rowspan = 2,padx = 5,pady=5)
		#ttk.Label(self.header_frame,text=' ').grid(row = 0,column =1)
		ttk.Label(self.header_frame, text = 'Travel Assistant',style ='Header.TLabel').grid(row = 0 , column =1,padx=15,pady=5,sticky = 'e')
		ttk.Label(self.header_frame ,wraplength =200, text = 'Choose Origin and Destination and let the \'Dijkstra\' works.').grid(row=1,column=1,sticky = 'e')

		self.middle_frame = ttk.Frame(master)

		self.middle_frame.pack(anchor = 'w')

		ttk.Label(self.middle_frame , text = 'Origin Country:').grid(row = 0,column=0,sticky = 'sw',padx=5)
		ttk.Label(self.middle_frame , text = 'Origin City:').grid(row=0,column = 1,sticky='sw',padx=5)
		ttk.Label(self.middle_frame,text = 'Origin Airport:').grid(row = 0,column = 2,sticky='sw',padx=5)


		self.origin_country = ttk.Combobox(self.middle_frame)

		self.origin_country.grid(row = 1,column = 0,padx=10,pady=10)

		self.origin_city = ttk.Combobox(self.middle_frame)

		self.origin_city.grid(row = 1 , column = 1,padx=10,pady=10)



		self.origin_airport = ttk.Combobox(self.middle_frame)


		self.origin_airport.grid(row = 1,column = 2,padx=10,pady=10)

		ttk.Label(self.middle_frame,text = 'Destination Country:').grid(row = 3,column = 0,padx=5,sticky='sw')


		ttk.Label(self.middle_frame,text = 'Destination City:').grid(row = 3 , column = 1,padx=5,sticky='sw')
		ttk.Label(self.middle_frame,text = 'Destination Airport:').grid(row = 3,column = 2,padx=5,sticky='sw')

		self.dest_country = ttk.Combobox(self.middle_frame)

		self.dest_country.grid(row = 4 , column = 0,padx=10,pady=10)

		self.dest_city = ttk.Combobox(self.middle_frame)

		self.dest_city.grid(row = 4 , column = 1,padx=10,pady=10)
		self.dest_airport = ttk.Combobox(self.middle_frame)
		self.dest_airport.grid(row = 4 , column = 2,padx=10,pady=10)


		self.contents_frame = ttk.Frame(master)

		
		

		
		self.contents_frame.pack(anchor = 'w')

		
		#-----------------------------middle frame ----
		

	
		#--------------content------frame-----


		self.path_frame = ttk.Frame(self.contents_frame)
		ttk.Label(self.path_frame,text = 'Path:').grid(row =0,column=0,sticky = 'sw',padx=5)
		self.path_frame.grid(row = 1 , column = 0,padx = 10)

		self.path  = ttk.Treeview(self.path_frame)

		self.path.grid(sticky = 'nswe',padx=10,pady =15)

		self.path['columns'] = ('airport','country','city')

		self.path.heading('#0',text = 'IATA Code',anchor='w')

		self.path.column("#0", anchor="w")

		self.path.heading('airport', text = 'Airport')

		self.path.column('airport',anchor = 'center' , width = 200)

		self.path.heading('country',text = 'Country')

		self.path.column('country',anchor = 'center',width = 200)

		self.path.heading('city',text = 'City')

		self.path.column('city',anchor = 'center',width = 200)

		

		#----------------footer - frame
		self.footer_frame = ttk.Frame(master)
		self.footer_frame.pack(anchor = 'w')

		self.cost_frame = ttk.Frame(self.footer_frame)

		self.cost_frame.pack(side= LEFT ,anchor = 'w')
		ttk.Label(self.cost_frame,text = 'Cost: ').grid(row = 0 , column  = 0,sticky = 'w',padx=10,pady=10)


		self.cost_var = StringVar()
		self.cost = ttk.Entry(self.cost_frame,width = 20 , state = 'readonly',textvariable = self.cost_var)

		self.cost.grid(row  = 0 , column = 1,sticky = 'w',padx=10,pady=10)


		self.btn_frame = ttk.Frame(self.footer_frame)

		self.btn_frame.pack(side= LEFT , anchor  = 'e')

		ttk.Button(self.btn_frame , text = 'Get Me Fast' ,command = self.compute).grid(row = 0 , column = 0,sticky  ='e',padx=15,pady=15) 


		
		ttk.Button(self.btn_frame,text = 'Clear',command = self.clear).grid(row = 0,column  = 1,sticky = 'e',padx=15,pady=15)

		#process middle frame
		self.fill_contries()
		self.origin_country_var = StringVar()

		self.origin_country.config(width = 25,textvariable = self.origin_country_var,state = 'readonly' )

		#self.origin_country.bind('<Button-1>',lambda e:self.fill_cities)
		self.dest_country_var = StringVar()

		self.dest_country.config(width = 25,textvariable = self.dest_country_var,state = 'readonly')
		#self.dest_country.bind('<<ComboboxSelected>>',lambda e:self.fill_cities)

		self.origin_country.bind('<<ComboboxSelected>>', lambda _: 
			self.origin_city.config(values = get_cities(self.origin_country_var.get())))
		

		self.dest_country.bind('<<ComboboxSelected>>',lambda _:
			self.dest_city.config(values = get_cities(self.dest_country_var.get())))

		self.origin_city_var = StringVar()

		self.origin_city.config(state = 'readonly' ,textvariable = self.origin_city_var,width=25)

		self.origin_city.bind('<<ComboboxSelected>>',lambda _:
			self.origin_airport.config(values = get_airports(self.origin_city_var.get(),self.origin_country_var.get())))


		self.dest_city_var = StringVar()

		self.dest_city.config(width = 25,textvariable = self.dest_city_var,state = 'readonly')

		self.dest_city.bind('<<ComboboxSelected>>',lambda _:
			self.dest_airport.config(values = get_airports(self.dest_city_var.get(),self.dest_country_var.get())))

		self.origin_airport_var = StringVar()
		self.origin_airport.config(textvariable = self.origin_airport_var ,state = 'readonly',width = 30)

		self.dest_airport.config(width = 30,state = 'readonly')
		
		self.origin_airport.bind('<<ComboboxSelected>>', lambda _:print(self.origin_airport_var.get()[:self.origin_airport_var.get().index('-')]))

		self.dest_airport_var = StringVar()
		self.dest_airport.config(textvariable = self.dest_airport_var ,state = 'readonly',width = 30)

		self.dest_airport.config(width = 30,state = 'readonly')
		
		self.cost_var = StringVar()

		self.cost.config(textvariable = self.cost_var)

		
		
	def fill_contries(self):

		cleaned_countries = set(countries)

		countries_list = sorted(list(cleaned_countries))

		self.origin_country.config(values = countries_list)

		self.dest_country.config(values = countries_list)
		

	def compute(self):
		self.clear()
		origin_code = self.origin_airport_var.get()[:self.origin_airport_var.get().find('-')]

		destination_code = self.dest_airport_var.get()[:self.dest_airport_var.get().find('-')]

		origin = TravelAdvisor.AIRPORTS[origin_code]

		destination = TravelAdvisor.AIRPORTS[destination_code]
		
		try :
			price,path = self.world.dijkstra(origin,destination)

			self.cost_var.set('$%s'%(price))
			if price > 1000 : 
				self.cost.config(foreground = 'red')
			else : 
				self.cost.config(foreground = 'green')
			print(price)

			for i,airport in enumerate(path) : 
				self.path.insert('','end',text = airport.code,values =(airport.name,airport.country,airport.city))
		except :
			messagebox.showinfo(title = 'Sorry for Unconvenience' , message = 'No Road found or the inputs are invalid')
		print(path)


	def clear(self):
		self.cost_var.set('$')
		for i in self.path.get_children():
			self.path.delete(i)
			




if __name__ == '__main__':

	


	#print(get_cities('Syria'))

	#get_airports('Aleppo')

	root = Tk()

	TravelApp(root)

	root.mainloop()