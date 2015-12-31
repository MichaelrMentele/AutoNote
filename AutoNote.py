#AutoNote.py
'''
Description: This is a desktop notetaking application designed to work similar 
to sticky notes but auto append notes to 'collections' (other documents) based 
on how they are tagged. Make your notes and use this to stick them in the 
appropriate bins. All automatically.
Inputs: ASCII characters as text editor. 
		Disseminate command, which intializes distribution waterfall
Outputs: None
Author: Michael
'''
import sys
import Tkinter
import noteAppender
import noteParser


class AutoNote_tk(Tkinter.Tk):
	'''This class contains a text editor GUI'''


	def __init__(self, parent):
		Tkinter.Tk.__init__(self,parent)
		self.parent = parent
		self.initialize()


	def initialize(self):
		'''Loads up the AutoNote GUI'''
		self.grid()

		#text entries to the editor
		self.entryVariable = Tkinter.StringVar()
		self.entry = Tkinter.Entry(self, textvariable=self.entryVariable)
		self.entry.grid(column=0, row=0, sticky='EW')
		self.entry.bind("<Return>", self.OnPressEnter)
		self.entryVariable.set(u"Enter text here.")

		#Display Button
		button = Tkinter.Button(self, text=u"Append Note!",
								command=self.OnButtonClick)
		button.grid(column=1, row=0)

		#Display label
		self.labelVariable = Tkinter.StringVar()
		label = Tkinter.Label(self, textvariable=self.labelVariable,
							  anchor="w", fg="white", bg="blue")
		label.grid(column=0, row=1, columnspan=2, stick='EW')
		self.labelVariable.set(u"Hello")

		#Determine behavior of GUI
		self.grid_columnconfigure(0, weight=1)
		self.resizable(True, False)
		self.update()
		self.geometry(self.geometry())
		self.entry.focus_set()
		self.entry.selection_range(0, Tkinter.END)


	def OnButtonClick(self):
		parsedNote = noteParser.parseText(self.entryVariable.get())
		noteAppender.append(parsedNote[0], parsedNote[1])

		self.labelVariable.set("Note Appended!")
		self.entry.focus_set()
		self.entry.selection_range(0,Tkinter.END)

	
	def OnPressEnter(self, event):
		raise Exception('Not implemented!')
		self.labelVariable.set("You clicked the enter)")
		self.entry.focus_set()
		self.entry.selection_range(0,Tkinter.END)



if __name__ == "__main__":
	app = AutoNote_tk(None)
	app.title('AutoNote')
	app.mainloop()

