from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import tkinter
from tkinter import Label
options = Options()
options.headless = True
driver = webdriver.Chrome(options=options)
driver.get("http://selfcare.denbroadband.in/Customer/Default.aspx")
username=driver.find_element_by_id("txtUserName")
password=driver.find_element_by_id("txtPassword")
username.send_keys("addemailhere") #Email
password.send_keys("addpasswordhere") #Password
login=driver.find_element_by_xpath('//*[@type="submit"]')
login.click()
session=driver.find_element_by_id("AccountPlanDetails")
session.click()
data=driver.find_element_by_id("ContentPlaceHolder1_tbAdditonal_tpPlan_gdPlan_lblRemain_0")
expirydate=driver.find_element_by_id("ContentPlaceHolder1_tbAdditonal_tpPlan_gdPlan_lblExpiryDate_0")
data1=data.text.strip('/-')
data_int=int(data1)
ed=expirydate.text
top = tkinter.Tk()
top.title("Test Window")
top.geometry('200x200')
lbl = Label(top, text="Den Broadband")
lbl.grid(column=0, row=0)
lbl = Label(top, text="Data Left : ")
lbl.grid(column=0, row=1)
lbl = Label(top, text=data1+"MB")
lbl.grid(column=1, row=1)
lbl = Label(top, text="Expired On :")
lbl.grid(column=0, row=2)
lbl = Label(top, text=ed)
lbl.grid(column=1, row=2)
top.mainloop()
