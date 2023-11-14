import tkinter as tk
from tkinter import Text, END
import tkinter.messagebox as mbox
from PIL import ImageTk, Image
import time
import psutil
import socket
import mysql.connector

# Connect to MySQL database
db_connection = mysql.connector.connect(
    host="Draunzer",
    user="root",
    password="12345",
    database="network_usage"
)

# Create a cursor object to execute SQL commands
db_cursor = db_connection.cursor()

# Create a table if it doesn't exist
db_cursor.execute('''
    CREATE TABLE IF NOT EXISTS network_usage (
        id INT AUTO_INCREMENT PRIMARY KEY,
        usage_value FLOAT,
        timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
''')

# Commit the changes
db_connection.commit()

# Function to insert network usage data into the database
def insert_network_usage(difference):
    db_cursor.execute("INSERT INTO network_usage (usage_value) VALUES (%s)", (difference,))
    db_connection.commit()

# Function to update the label and insert data into the database
def update_label():
    global old_value

    new_value = psutil.net_io_counters().bytes_sent + psutil.net_io_counters().bytes_recv
    difference = new_value - old_value

    # Insert data into the database
    insert_network_usage(difference)

    # Display data in the GUI
    path_text.delete("1.0", "end")
    path_text.insert(END, "Usage: {:.3f} bytes/sec".format(difference))

    # Update the connection status label
    IPaddress = socket.gethostbyname(socket.gethostname())
    if IPaddress == "127.0.0.1":
        l2.configure(text="No internet, your localhost is\n" + IPaddress)
    else:
        l2.configure(text="Connected, with the IP address\n" + IPaddress)

    # Check if max limit is exceeded
    if difference > 10000000000000:
        mbox.showinfo("Exceed Status", "Max Limit Usage Exceeded.")

    old_value = new_value

# Function to stop the network usage tracking and close the window
def stop_tracking():
    window.destroy()

# Function to start the network usage tracking
def start_tracking():
    window1.withdraw()  # Use withdraw to hide the window without destroying it
    global window
    window = tk.Tk()
    window.title("Network Usage Tracker")
    window.geometry("1000x700")
    window.iconify()

    # top label
    top1 = tk.Label(window, text="NETWORK USAGE\nTRACKER", font=("Arial", 50, 'underline'), fg="magenta")
    top1.place(x=190, y=10)

    top1 = tk.Label(window, text="MAX LIMIT  :  100 MB/sec", font=("Arial", 50), fg="green")
    top1.place(x=130, y=180)

    # text area
    global path_text
    path_text = Text(window, height=1, width=24, font=("Arial", 50), bg="white", fg="blue", borderwidth=2, relief="solid")
    path_text.place(x=50, y=300)

    # connection status label
    top1 = tk.Label(window, text="Connection Status :", font=("Arial", 50), fg="green")
    top1.place(x=200, y=450)

    # label for displaying connection status
    global l2
    l2 = tk.Label(window, fg='blue', font=("Arial", 30))
    l2.place(x=200, y=530)

    # global variable to store the previous network usage value
    global old_value
    old_value = 0

    # Function to update the label and insert data into the database
    def update_label_after_delay():
        update_label()
        window.after(1000, update_label_after_delay)

    # Function to stop the network usage tracking and close the window
    def stop_tracking():
        window.destroy()

    # stop button created
    stop_button = tk.Button(window, text="STOP", command=stop_tracking, font=("Arial", 25), bg="red", fg="blue",
                            borderwidth=3, relief="raised")
    stop_button.place(x=730, y=590)

    window.protocol("WM_DELETE_WINDOW", stop_tracking)
    window.after(1000, update_label_after_delay)
    window.mainloop()

# Main Window & Configuration
window1 = tk.Tk()
window1.title("Network Usage Tracker")
window1.geometry('1000x700')

# top label
start1 = tk.Label(text="NETWORK USAGE\nTRACKER", font=("Arial", 55, "underline"), fg="magenta")
start1.place(x=150, y=10)

# start button created
startb = tk.Button(window1, text="START", command=start_tracking, font=("Arial", 25), bg="orange", fg="blue",
                   borderwidth=3, relief="raised")
startb.place(x=130, y=590)

# exit button created
exitb = tk.Button(window1, text="EXIT", command=window1.destroy, font=("Arial", 25), bg="red", fg="blue",
                  borderwidth=3, relief="raised")
exitb.place(x=730, y=590)

# image on the main window
path = "Images/front.png"
img1 = ImageTk.PhotoImage(Image.open(path))
panel = tk.Label(window1, image=img1)
panel.place(x=320, y=200)

window1.protocol("WM_DELETE_WINDOW", window1.destroy)
window1.mainloop()
