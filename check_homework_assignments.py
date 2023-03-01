from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException  
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import sys, poplib
from email import parser

max_classes = 10
max_assignments = 20

def cr():
    path = "https://trinitybham.classreach.com/Login"
    driver = webdriver.Chrome(executable_path='')
    driver.get(path)
    assert "LogIn" in driver.title

    user = driver.find_element(By.NAME, "UserName")
    pwd = driver.find_element(By.NAME, "Password")

    user.send_keys("user")
    pwd.send_keys("password")

    driver.find_element(By.ID, "ClassReachLoginButton").click()
    driver.find_element(By.XPATH, "//*[@id=\"RoleSelectContainer\"]/div[1]/form/input[4]").click()
    driver.find_element(By.XPATH, "//*[@id=\"StandardSidebar\"]/div/div/div[2]/div/ul/li[10]/ul/li[3]/a").click()
    
    classes = {}
    for i in range(3, max_classes-1):
        tmp_path = f"/html/body/div[2]/div[6]/div/div/div[2]/div/ul/li[10]/ul/li[3]/ul/li[{i}]/a"
        tmp = driver.find_element(By.XPATH, tmp_path).text.split("\n")
        ext = driver.find_element(By.XPATH, tmp_path).get_attribute("href")
        classes[tmp[0]] = [tmp_path]
        
    assignments = {}
    for c in classes:
        print(c + ":")
        driver.find_element(By.XPATH, classes[c][0]).click()
        driver.find_element(By.XPATH, "/html/body/div[2]/div[7]/div[1]/div[2]/a[4]").click()

        assignments[c] = []
        for i in range(1, max_assignments):
            try:
                row = driver.find_element(By.XPATH, f"/html/body/div[2]/div[7]/div[2]/div/div/div[2]/div/div[2]/a[{i}]")
                name = row.find_element(By.XPATH, f"/div[1]/div").text
                start_date = row.find_element(By.XPATH, f"/div[3]").text
                due_date = row.find_element(By.XPATH, f"/div[4]").text
                assignments[c].append(f"Name: {name}; Created {start_date}; Due {due_date}")
            except NoSuchElementException:
                break

        if len(assignments[c]) == 0:
            assignments[c].append(f"No assignments found.")

        for a in assignments[c]:
            print(a)

        driver.back()
        driver.back()
        driver.find_element(By.XPATH, "//*[@id=\"StandardSidebar\"]/div/div/div[2]/div/ul/li[10]/ul/li[3]/a").click()

    driver.close()
    
def gm():
    stream = poplib.POP3_SSL('pop.gmail.com')
    stream.user('email')
    stream.pass_('password')
    #Get messages from server:
    print(stream.stat())

    messages = []
    for i in range(1, stream.stat()[0]):
        if messages[i][1][2].decode("utf-8"):
            pass

    messages = [stream.retr(i) for i in range(1, stream.stat()[0])]
    print(messages[0][1])
    # Concat message pieces:
    messages = [b"\n".join(mssg[1]) for mssg in messages]
    #Parse message intom an email object:
    messages = [parser.Parser().parsestr(mssg) for mssg in messages]
    
    for message in messages:
        print(message['subject'])
    stream.quit()

def main():
    if sys.argv[1] == "cr":
        cr()
    elif sys.argv[1] == "gm":
        gm()
    else:
        print("Error: Invalid argument")

if __name__ == "__main__":
    main()