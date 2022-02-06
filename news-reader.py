# imports
from turtle import width
from selenium import webdriver;
from easygui import enterbox;
from time import sleep;
import pyttsx3;
# defining function
def newsReader():
    engine=pyttsx3.init();
    newVoiceRate = 90;
    engine.setProperty('rate',newVoiceRate);
    url=enterbox("Enter an URL from BBC news");
    # url="https://www.bbc.com/news/uk-60279585";
    #print(url);
    nav=webdriver.Chrome("../../../chromedriver.exe");
    # nav.manage().window().maximize();
    nav.get(url);
    nav.maximize_window();
    sleep(3);  
    nav.find_element_by_class_name('fc-button-label').click()
    sleep(3);
    heading=nav.find_element_by_id('main-heading').text;    
    engine.say(heading);
    engine.runAndWait();
    sleep(50); 
    
# calling function
newsReader();