
from tkinter import Tk, messagebox


class MyApplication(Tk):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.title("My Application")





if __name__ == "__main__":
    app = MyApplication()
    app.mainloop()
