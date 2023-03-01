from selenium import webdriver
import random


driver = webdriver.Chrome()

driver.get("https://forms.office.com/Pages/ResponsePage.aspx?id=hVh-eMTdU0Wnv6udzkyo6ty483wRWiJKnstcshYYwQZUQU8xUENFQTY4UTJBNjM4TFBSOEg0QTJLTS4u")

# section 1

# first question
def first_question():
    random_number = random.randint(1, 20)

    if random_number <= 8:
        under_18 = driver.find_element_by_xpath("/html/body/div/div/div[2]/div/div[1]/div/div/div[1]/div[2]/div[2]/div[2]/div/div[3]/div/div[1]/div/label/input")
        under_18.click()
    if random_number > 8 and random_number <= 14:
        option_2 = driver.find_element_by_xpath("/html/body/div/div/div[2]/div/div[1]/div/div/div[1]/div[2]/div[2]/div[2]/div/div[3]/div/div[2]/div/label/input")
        option_2.click()
    if random_number > 14 and random_number <= 18:
        option_3 = driver.find_element_by_xpath("/html/body/div/div/div[2]/div/div[1]/div/div/div[1]/div[2]/div[2]/div[2]/div/div[3]/div/div[3]/div/label/input")
        option_3.click()
    if random_number == 19:
        option_4 = driver.find_element_by_xpath("/html/body/div/div/div[2]/div/div[1]/div/div/div[1]/div[2]/div[2]/div[2]/div/div[3]/div/div[4]/div/label/input")
        option_4.click()
    if random_number == 20:
        option_5 = driver.find_element_by_xpath("/html/body/div/div/div[2]/div/div[1]/div/div/div[1]/div[2]/div[2]/div[2]/div/div[3]/div/div[5]/div/label/input")
        option_5.click()

# secind question

def secind_question():

    random_number = random.randint(1, 25)

    if random_number <= 12:
        woman = driver.find_element_by_xpath("/html/body/div/div/div[2]/div/div[1]/div/div/div[1]/div[2]/div[2]/div[3]/div/div[3]/div/div[1]/div/label/input")
        woman.click()
    if random_number > 12 and random_number <= 24:
        man = driver.find_element_by_xpath("/html/body/div/div/div[2]/div/div[1]/div/div/div[1]/div[2]/div[2]/div[3]/div/div[3]/div/div[2]/div/label/input")
        man.click()
    if random_number == 25:
        non_binary = driver.find_element_by_xpath("/html/body/div/div/div[2]/div/div[1]/div/div/div[1]/div[2]/div[2]/div[3]/div/div[3]/div/div[3]/div/label/input")
        non_binary.click()

# third question

def third_question():

    random_number = random.randint(1, 100)

    if random_number <= 65:
        yes = driver.find_element_by_xpath("/html/body/div/div/div[2]/div/div[1]/div/div/div[1]/div[2]/div[2]/div[4]/div/div[3]/div/div[1]/div/label/input")
        yes.click()
    if random_number > 65 and random_number <= 95:
        no = driver.find_element_by_xpath("/html/body/div/div/div[2]/div/div[1]/div/div/div[1]/div[2]/div[2]/div[4]/div/div[3]/div/div[2]/div/label/input")
        no.click()
    if random_number > 95:
        maybe = driver.find_element_by_xpath("/html/body/div/div/div[2]/div/div[1]/div/div/div[1]/div[2]/div[2]/div[4]/div/div[3]/div/div[3]/div/label/input")
        maybe.click()

# forth question

def forth_question():

    countries = ['england', 'russia', 'france', 'finland', 'germany', 'america', 'greece', 'austria', 'italy', 'bulgaria', 'romania', 'canada', 'south africa', 'japan', 'malta']

    random_number = random.randint(1, 100)
    
    if random_number <= 70:
        england = driver.find_element_by_xpath("/html/body/div/div/div[2]/div/div[1]/div/div/div[1]/div[2]/div[2]/div[5]/div/div[3]/div/div/input")
        england.send_keys("England")
    if random_number > 70 and random_number <= 75:
        america = driver.find_element_by_xpath("/html/body/div/div/div[2]/div/div[1]/div/div/div[1]/div[2]/div[2]/div[5]/div/div[3]/div/div/input")
        america.send_keys("America")
    if random_number > 75 and random_number <+ 100:
        random_country_select = random.choice(countries)
        random_country = driver.find_element_by_xpath("/html/body/div/div/div[2]/div/div[1]/div/div/div[1]/div[2]/div[2]/div[5]/div/div[3]/div/div/input")
        random_country.send_keys(random_country_select)
        
    #button press
    next_button = driver.find_element_by_xpath("/html/body/div/div/div[2]/div/div[1]/div/div/div[1]/div[2]/div[3]/div[1]/button")
    next_button.click()

# section 2

def fith_question():
    star_1 = driver.find_element_by_xpath("/html/body/div/div/div[2]/div/div[1]/div/div/div[1]/div[2]/div[2]/div[2]/div/div[3]/div/div/div[1]/span")
    star_2 = driver.find_element_by_xpath("/html/body/div/div/div[2]/div/div[1]/div/div/div[1]/div[2]/div[2]/div[2]/div/div[3]/div/div/div[2]/span")
    star_3 = driver.find_element_by_xpath("/html/body/div/div/div[2]/div/div[1]/div/div/div[1]/div[2]/div[2]/div[2]/div/div[3]/div/div/div[3]/span")
    star_4 = driver.find_element_by_xpath("/html/body/div/div/div[2]/div/div[1]/div/div/div[1]/div[2]/div[2]/div[2]/div/div[3]/div/div/div[4]/span")
    star_5 = driver.find_element_by_xpath("/html/body/div/div/div[2]/div/div[1]/div/div/div[1]/div[2]/div[2]/div[2]/div/div[3]/div/div/div[5]/span")
    star_6 = driver.find_element_by_xpath("/html/body/div/div/div[2]/div/div[1]/div/div/div[1]/div[2]/div[2]/div[2]/div/div[3]/div/div/div[6]/span")
    star_7 = driver.find_element_by_xpath("/html/body/div/div/div[2]/div/div[1]/div/div/div[1]/div[2]/div[2]/div[2]/div/div[3]/div/div/div[7]/span")
    star_8 = driver.find_element_by_xpath("/html/body/div/div/div[2]/div/div[1]/div/div/div[1]/div[2]/div[2]/div[2]/div/div[3]/div/div/div[8]/span")
    star_9 = driver.find_element_by_xpath("/html/body/div/div/div[2]/div/div[1]/div/div/div[1]/div[2]/div[2]/div[2]/div/div[3]/div/div/div[9]/span")
    star_10 = driver.find_element_by_xpath("/html/body/div/div/div[2]/div/div[1]/div/div/div[1]/div[2]/div[2]/div[2]/div/div[3]/div/div/div[10]/span")

    random_number = random.randint(1, 100)

    if random_number <= 5:
        star_1.click()
    if random_number > 5 and random_number <= 10:
        star_2.click()
    if random_number > 10 and random_number <= 15:
        star_3.click()
    if random_number > 15 and random_number <= 20:
        star_4.click()
    if random_number > 20 and random_number <= 35:
        star_5.click()
    if random_number > 35 and random_number <= 45:
        star_6.click()
    if random_number > 45 and random_number <= 50:
        star_7.click()
    if random_number > 50 and random_number <= 65:
        star_8.click()
    if random_number > 65 and random_number <= 85:
        star_9.click()
    if random_number > 85:
        star_10.click()

def sixth_question():
    random_number = random.randint(1, 100)

    if random_number <= 45:
        yes = driver.find_element_by_xpath("/html/body/div/div/div[2]/div/div[1]/div/div/div[1]/div[2]/div[2]/div[3]/div/div[3]/div/div[1]/div/label/input")
        yes.click()
    if random_number > 45 and random_number <= 90:
        no = driver.find_element_by_xpath("/html/body/div/div/div[2]/div/div[1]/div/div/div[1]/div[2]/div[2]/div[3]/div/div[3]/div/div[2]/div/label/input")
        no.click()
    if random_number > 90:
        maybe = driver.find_element_by_xpath("/html/body/div/div/div[2]/div/div[1]/div/div/div[1]/div[2]/div[2]/div[3]/div/div[3]/div/div[3]/div/label/input")
        maybe.click()

def seventh_question():

    random_number = random.randint(1, 100)

    if random_number <= 20:
        option_1 = driver.find_element_by_xpath("/html/body/div/div/div[2]/div/div[1]/div/div/div[1]/div[2]/div[2]/div[4]/div/div[3]/div/div[1]/div/label/input")
        option_1.click()
    if random_number > 20 and random_number <= 65:
        option_2 = driver.find_element_by_xpath("/html/body/div/div/div[2]/div/div[1]/div/div/div[1]/div[2]/div[2]/div[4]/div/div[3]/div/div[2]/div/label/input")
        option_2.click()
    if random_number > 65 and random_number <= 85:
        option_3 = driver.find_element_by_xpath("/html/body/div/div/div[2]/div/div[1]/div/div/div[1]/div[2]/div[2]/div[4]/div/div[3]/div/div[3]/div/label/input")
        option_3.click()
    if random_number > 85:
        option_4 = driver.find_element_by_xpath("/html/body/div/div/div[2]/div/div[1]/div/div/div[1]/div[2]/div[2]/div[4]/div/div[3]/div/div[4]/div/label/input")
        option_4.click()
def eighth_question():

    random_number = random.randint(1, 100)

    if random_number <= 45:
        yes = driver.find_element_by_xpath("/html/body/div/div/div[2]/div/div[1]/div/div/div[1]/div[2]/div[2]/div[5]/div/div[3]/div/div[1]/div/label/input")
        yes.click()
    if random_number > 45 and random_number < 90:
        no = driver.find_element_by_xpath("/html/body/div/div/div[2]/div/div[1]/div/div/div[1]/div[2]/div[2]/div[5]/div/div[3]/div/div[2]/div/label/input")
        no.click()
    if random_number > 90:
        maybe = driver.find_element_by_xpath("/html/body/div/div/div[2]/div/div[1]/div/div/div[1]/div[2]/div[2]/div[5]/div/div[3]/div/div[3]/div/label/input")
        maybe.click()

def ninth_question():

    random_number = random.randint(1, 100)

    if random_number <= 10:
        option_1 = driver.find_element_by_xpath("/html/body/div/div/div[2]/div/div[1]/div/div/div[1]/div[2]/div[2]/div[6]/div/div[3]/div/div[1]/div/label/input")
        option_1.click()
    if random_number > 10 and random_number <= 35:
        option_2 = driver.find_element_by_xpath("/html/body/div/div/div[2]/div/div[1]/div/div/div[1]/div[2]/div[2]/div[6]/div/div[3]/div/div[2]/div/label/input")
        option_2.click()
    if random_number > 35 and random_number <= 60:
        option_3 = driver.find_element_by_xpath("/html/body/div/div/div[2]/div/div[1]/div/div/div[1]/div[2]/div[2]/div[6]/div/div[3]/div/div[3]/div/label/input")
        option_3.click()
    if random_number > 60 and random_number <= 85:
        option_4 = driver.find_element_by_xpath("/html/body/div/div/div[2]/div/div[1]/div/div/div[1]/div[2]/div[2]/div[6]/div/div[3]/div/div[4]/div/label/input")
        option_4.click()
    if random_number > 85:
        option_5 = driver.find_element_by_xpath("/html/body/div/div/div[2]/div/div[1]/div/div/div[1]/div[2]/div[2]/div[6]/div/div[3]/div/div[5]/div/label/input")
        option_5.click()


if __name__ == "__main__":
    first_question()
    secind_question()
    third_question()
    forth_question()
    fith_question()
    sixth_question()
    seventh_question()
    eighth_question()
    ninth_question()