# Import the wxPython library for creating GUI applications
import wx

# Define a new class 'MyFrame' that inherits from wx.Frame (a window)
class MyFrame(wx.Frame):
    def _init_(self):
        # Call the constructor of the parent class (wx.Frame)
        super()._init_(parent=None, title='Hello World')  # Set window title
        self.Show()  # Display the window

# Run this part only if the script is run directly (not imported)
if _name_ == '_main_':
    app = wx.App()       # Create the main application object
    frame = MyFrame()    # Create an instance of MyFrame (the window)
    app.MainLoop()   # Start the event loop so the window stays open