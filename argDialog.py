from tkinter import *
import tkSimpleDialog

class ArgDialog(tkSimpleDialog.Dialog):

	def body(self, master):
		"""Body of the dialog with entries for all arguments"""
		for i, arg in enumerate(self.args):
			Label(master, text=arg).grid(row=i)

		self.entries = [None]*len(self.args)

		for i in range(len(self.args)):
			self.entries[i] = Entry(master)
		print(self.entries)

		for i, entry in enumerate(self.entries):
			entry.grid(row=i, column=1)

		return self.entries[0] # initial focus


	def apply(self):
		first = int(self.entries[0].get())
		print(first)