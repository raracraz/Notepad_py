#https://www.youtube.com/watch?v=bxwM7YE3Rkg

from tkinter import *
def main():
    root = Tk()
    gui = Window(root)
    gui.root.mainloop()
    return None

class Window:
    def __init__(self, root):
        self.root = root
        self.root.geometry('700x500')
        self.root.title('TK Notepad')

        #Create textspace
        self.textspace = Text(self.root)
        self.textspace.grid(row=0, column=0)

        #Create open and save buttons
        Button(self.root, text = 'Save', command = self.savefile).grid(row=0, column=1)
        Button(self.root, text = 'Open', command = self.openfile).grid(row=0, column=2)

        pass

    def savefile(self):
        savegui = Tk()
        savegui.geometry('560x50')
        filecontents = self.textspace.get(0.0, END)

        def writefile():
            with open(file_name.get()+'.txt', 'w+') as file:
                file.write(filecontents)
                file.close()
                savegui.destroy()
            return None


        Label(savegui, text = 'File Name').grid(row=0, column=0)
        file_name = Entry(savegui, width=40)
        file_name.grid(row=0, column=1)

        Button(savegui, text = 'Save', command = writefile).grid(row=0, column=2)


        return None

    def openfile(self):
        opengui = Tk()
        opengui.geometry('560x50')

        def opennew():
            try:
                with open(file_name.get(), 'r') as file:
                    self.textspace.delete(0.0, END)
                    self.textspace.insert(0.0, file.read())
                    file.close()
                    opengui.destroy()
            except FileNotFoundError:
                file_name.delete(0.0, END)
                file_name.insert(0.0, 'File not found, try another one...')
            return None 

        Label(opengui, text = 'File Name').grid(row=0, column=0)
        file_name = Entry(opengui, width=40)
        file_name.grid(row=0, column=1)

        Button(opengui, text = 'Open', command = opennew).grid(row=0, column=2)

        return None

    pass
main()