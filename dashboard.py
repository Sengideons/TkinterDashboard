from tkinter import *
from PIL import ImageTk, Image, ImageDraw
from datetime import *
import time


class Dashboard2:
    def __init__(self, window):
        self.window = window
        self.window.title("System Management Dashboard")
        self.window.geometry("1366x768")
        self.window.resizable(0, 0)
        self.window.state('zoomed')
        self.window.config(background='#eff5f6')
        # Window Icon Photo
        icon = PhotoImage(file='images\\pic-icon.png')
        self.window.iconphoto(True, icon)

        # ==============================================================================
        # ================== HEADER ====================================================
        # ==============================================================================
        self.header = Frame(self.window, bg='#009df4')
        self.header.place(x=300, y=0, width=1070, height=60)

        self.logout_text = Button(self.header, text="Logout", bg='#32cf8e', font=("", 13, "bold"), bd=0, fg='white',
                                  cursor='hand2', activebackground='#32cf8e')
        self.logout_text.place(x=950, y=15)

        # ==============================================================================
        # ================== SIDEBAR ===================================================
        # ==============================================================================
        self.sidebar = Frame(self.window, bg='#ffffff')
        self.sidebar.place(x=0, y=0, width=300, height=750)

        # =============================================================================
        # ============= BODY ==========================================================
        # =============================================================================
        self.heading = Label(self.window, text='Dashboard', font=("", 15, "bold"), fg='#0064d3', bg='#eff5f6')
        self.heading.place(x=325, y=70)

        # body frame 1
        self.bodyFrame1 = Frame(self.window, bg='#ffffff')
        self.bodyFrame1.place(x=328, y=110, width=1040, height=350)

        # body frame 2
        self.bodyFrame2 = Frame(self.window, bg='#009aa5')
        self.bodyFrame2.place(x=328, y=495, width=310, height=220)

        # body frame 3
        self.bodyFrame3 = Frame(self.window, bg='#e21f26')
        self.bodyFrame3.place(x=680, y=495, width=310, height=220)

        # body frame 4
        self.bodyFrame4 = Frame(self.window, bg='#ffcb1f')
        self.bodyFrame4.place(x=1030, y=495, width=310, height=220)

        # ==============================================================================
        # ================== SIDEBAR ===================================================
        # ==============================================================================

        # logo
        self.logoImage = ImageTk.PhotoImage(file='images/hyy.png')
        self.logo = Label(self.sidebar, image=self.logoImage, bg='#ffffff')
        self.logo.place(x=70, y=80)

        # Name of brand/person
        self.brandName = Label(self.sidebar, text='Sen Gideons', bg='#ffffff', font=("", 15, "bold"))
        self.brandName.place(x=80, y=200)

        # Dashboard
        self.dashboardImage = ImageTk.PhotoImage(file='images/dashboard-icon.png')
        self.dashboard = Label(self.sidebar, image=self.dashboardImage, bg='#ffffff')
        self.dashboard.place(x=35, y=289)

        self.dashboard_text = Button(self.sidebar, text="Dashboard", bg='#ffffff', font=("", 13, "bold"), bd=0,
                                     cursor='hand2', activebackground='#ffffff')
        self.dashboard_text.place(x=80, y=287)

        # Manage
        self.manageImage = ImageTk.PhotoImage(file='images/manage-icon.png')
        self.manage = Label(self.sidebar, image=self.manageImage, bg='#ffffff')
        self.manage.place(x=35, y=340)

        self.manage_text = Button(self.sidebar, text="Manage", bg='#ffffff', font=("", 13, "bold"), bd=0,
                                  cursor='hand2', activebackground='#ffffff')
        self.manage_text.place(x=80, y=345)

        # Settings
        self.settingsImage = ImageTk.PhotoImage(file='images/settings-icon.png')
        self.settings = Label(self.sidebar, image=self.settingsImage, bg='#ffffff')
        self.settings.place(x=35, y=402)

        self.settings_text = Button(self.sidebar, text="Settings", bg='#ffffff', font=("", 13, "bold"), bd=0,
                                    cursor='hand2', activebackground='#ffffff')
        self.settings_text.place(x=80, y=402)

        # Exit
        self.ExitImage = ImageTk.PhotoImage(file='images/exit-icon.png')
        self.Exit = Label(self.sidebar, image=self.ExitImage, bg='#ffffff')
        self.Exit.place(x=25, y=452)

        self.Exit_text = Button(self.sidebar, text="Exit", bg='#ffffff', font=("", 13, "bold"), bd=0,
                                cursor='hand2', activebackground='#ffffff')
        self.Exit_text.place(x=85, y=462)

        # =============================================================================
        # ============= BODY ==========================================================
        # =============================================================================

        # Body Frame 1
        self.pieChart_image = ImageTk.PhotoImage(file='images/pie-graph1.png')
        self.pieChart = Label(self.bodyFrame1, image=self.pieChart_image, bg='#ffffff')
        self.pieChart.place(x=690, y=70)

        # Graph
        self.graph_image = ImageTk.PhotoImage(file='images/graph.png')
        self.graph = Label(self.bodyFrame1, image=self.graph_image, bg='#ffffff')
        self.graph.place(x=40, y=70)

        # Body Frame 2
        self.total_people = Label(self.bodyFrame2, text='230', bg='#009aa5', font=("", 25, "bold"))
        self.total_people.place(x=120, y=100)

        self.totalPeopleImage = ImageTk.PhotoImage(file='images/left-icon.png')
        self.totalPeople = Label(self.bodyFrame2, image=self.totalPeopleImage, bg='#009aa5')
        self.totalPeople.place(x=220, y=0)

        self.totalPeople_label = Label(self.bodyFrame2, text="Total People", bg='#009aa5', font=("", 12, "bold"),
                                       fg='white')
        self.totalPeople_label.place(x=5, y=5)

        # Body Frame 3
        self.people_left = Label(self.bodyFrame3, text='50', bg='#e21f26', font=("", 25, "bold"))
        self.people_left.place(x=120, y=100)

        # left icon
        self.LeftImage = ImageTk.PhotoImage(file='images/left-icon.png')
        self.Left = Label(self.bodyFrame3, image=self.LeftImage, bg='#e21f26')
        self.Left.place(x=220, y=0)

        self.peopleLeft_label = Label(self.bodyFrame3, text="Left", bg='#e21f26', font=("", 12, "bold"),
                                      fg='white')
        self.peopleLeft_label.place(x=5, y=5)

        # Body Frame 4
        self.total_earnings = Label(self.bodyFrame4, text='$40,000.00', bg='#ffcb1f', font=("", 25, "bold"))
        self.total_earnings.place(x=80, y=100)

        self.earnings_label = Label(self.bodyFrame4, text="Total Earnings", bg='#ffcb1f', font=("", 12, "bold"),
                                    fg='white')
        self.earnings_label.place(x=5, y=5)
        # Frame 4 icon
        self.earningsIcon_image = ImageTk.PhotoImage(file='images/earn3.png')
        self.earningsIcon = Label(self.bodyFrame4, image=self.earningsIcon_image, bg='#ffcb1f')
        self.earningsIcon.place(x=220, y=0)




        # date and Time
        self.clock_image = ImageTk.PhotoImage(file="images/time.png")
        self.date_time_image = Label(self.sidebar, image=self.clock_image, bg="white")
        self.date_time_image.place(x=88, y=20)

        self.date_time = Label(self.window)
        self.date_time.place(x=115, y=15)
        self.show_time()

    def show_time(self):
        self.time = time.strftime("%H:%M:%S")
        self.date = time.strftime('%Y/%m/%d')
        set_text = f"  {self.time} \n {self.date}"
        self.date_time.configure(text=set_text, font=("", 13, "bold"), bd=0, bg="white", fg="black")
        self.date_time.after(100, self.show_time)


def wind():
    window = Tk()
    Dashboard2(window)
    window.mainloop()


if __name__ == '__main__':
    wind()
