import tkinter as tk

LARGE_FONT = ("Verdana", 12)


class Simu(tk.Tk):
	
	def __init__(self, *args,**kwargs):
		tk.Tk.__init__(self, *args,**kwargs)
		container = tk.Frame(self)
		container.pack(side ="top",fill="both",expand=True)

		container.grid_rowconfigure(0, weight=1)
		container.grid_columnconfigure(0, weight=1)
		self.frame = {}

		frame = StartPage(container,self)
		frame2 = StartPage2(container,self)
		
		self.frame[StartPage] = frame
		self.frame[StartPage2] = frame2
		frame.grid(row=0, column=0, sticky="nsew")
		frame2.grid(row=28, column=28, sticky="nsew")
		self.show_frame(StartPage)
		self.show_frame2(StartPage2)

	def show_frame(self, cont):
		frame = self.frame[cont]
		frame.tkraise()

	def show_frame2(self, cont):
		frame2 = self.frame[cont]
		frame2.tkraise()

class StartPage(tk.Frame):

	def __init__(self, parent, controller):
		tk.Frame.__init__(self,parent)
		label = tk.Label(self, text="Start Page", font= LARGE_FONT)
		label.pack(pady=10,padx=10)

class StartPage2(tk.Frame):

	def __init__(self, parent, controller):
		tk.Frame.__init__(self,parent)
		label = tk.Label(self, text="Start Page", font= LARGE_FONT)
		label.pack(pady=10,padx=10)

app = Simu()
app.mainloop()
