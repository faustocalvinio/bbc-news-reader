# imports
from xml.dom.expatbuilder import ElementInfo
from xml.etree.ElementTree import Element
from selenium import webdriver;
from easygui import enterbox,choicebox;
from time import sleep;
import pyttsx3;
# defining function
def newsReader():
    engine=pyttsx3.init();
    newVoiceRate = 90;
    engine.setProperty('rate',newVoiceRate);
    # url=enterbox("Enter an URL from BBC news");
    # url="https://www.bbc.com/news/uk-60279585";
    url="https://www.bbc.com"
    #print(url);
    nav=webdriver.Chrome("../../../../../Downloads/chromedriver_win32/chromedriver.exe");
    # nav.manage().window().maximize();
    nav.get(url);
    nav.maximize_window();
    sleep(1.5);  
    nav.find_element_by_class_name('fc-button-label').click()
    sleep(1.5);
    nav.find_element_by_id('bbccookies-continue-button').click();
    # heading=nav.find_element_by_id('main-heading').text;    
    # engine.say(heading);
    # engine.runAndWait();
    categoriesEnd=[]
    categories=nav.find_elements_by_class_name('module__title__link');
    for cat in categories:
        categoriesEnd.append(cat.text)       
        
    category=choicebox("pick a category","Pick category",categoriesEnd)
    print(category)
    sleep(3)
    sleep(50); 
    
# calling function
newsReader();