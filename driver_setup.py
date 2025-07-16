from selenium import webdriver
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.edge.options import Options
from selenium.webdriver.common.by import By

def start_edge():
    options = Options()
    options.add_argument("--start-maximized")
    service = EdgeService(executable_path=r"C:\Users\HP\Downloads\Web Drivres\Edgedriver\msedgedriver.exe")

    return webdriver.Edge(service=service, options=options)