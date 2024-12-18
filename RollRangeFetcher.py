from tkinter import Tk, Label, Entry, Button
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import os

# C:\Users\Ronit Ahuja\OneDrive\Desktop\RollRangeFetcher
# https://www.osmania.ac.in/res07/becbcsaug24.jsp

def take_ss(num, desktop_path, site_link, driver):
    try:
        driver.get(site_link)
        driver.maximize_window()
        driver.find_element("name", "htno").send_keys(num)
        driver.find_element("name", "Submit").click()

        screenshot_path = os.path.join(desktop_path, f"{num}.png")
        driver.save_screenshot(screenshot_path)
    except Exception as e:
        exit(0)

def on_submit(root):
    start_number = int(entry_start.get())
    end_number = int(entry_end.get())
    desktop_path = entry_path.get()
    site_link = entry_link.get()

    sevice=Service("C:\\webdrivers\\chromedriver.exe")
    driver = webdriver.Chrome(service=sevice)
    for i in range(start_number, end_number + 1):
        take_ss(i, desktop_path, site_link,driver)
    root.destroy()
    driver.quit()

# Tkinter GUI
root = Tk()
root.title("RollRangeFetcher")
root.geometry("400x200")  

label_path = Label(root, text="Folder Path:")
label_path.grid(row=0, column=0)
entry_path = Entry(root,bd=1, relief="solid", width=50)
entry_path.grid(row=0, column=1)

label_link = Label(root, text="OU Site Link:")
label_link.grid(row=1, column=0)
entry_link = Entry(root,bd=1, relief="solid",width=50)
entry_link.grid(row=1, column=1)

label_start = Label(root, text="Start Number:")
label_start.grid(row=2, column=0)
entry_start = Entry(root,bd=1, relief="solid",width=50)
entry_start.grid(row=2, column=1)

label_end = Label(root, text="End Number:")
label_end.grid(row=3, column=0)
entry_end = Entry(root,bd=1, relief="solid",width=50)
entry_end.grid(row=3, column=1)

submit_button = Button(root, text="Submit",bd=1, relief="solid", command=lambda: on_submit(root))
submit_button.grid(row=4, column=0, columnspan=2)

root.mainloop()
