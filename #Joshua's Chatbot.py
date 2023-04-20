#Basic Chatbot (JTB)

#Imports and pre-requisits
from wit import Wit
import pyttsx3 as p
#For opening links
import webbrowser
#Connecting database
import mysql.connector
#For typewriter effect
import time
import sys


#Settings
server_token = "BBYGBXYNDZEYEANBNTULZZFJ7GHH2DT3"
client = Wit(access_token=server_token)

#Connect to database
connection = mysql.connector.connect(host = 'localhost', user='root', passwd='', database='kakashi_chatbot')
cur = connection.cursor()

#welcome message and starting the chatbot
print("""



                                                                    ░██╗░░░░░░░██╗███████╗██╗░░░░░░█████╗░░█████╗░███╗░░░███╗███████╗  ████████╗░█████╗░
                                                                    ░██║░░██╗░░██║██╔════╝██║░░░░░██╔══██╗██╔══██╗████╗░████║██╔════╝  ╚══██╔══╝██╔══██╗
                                                                    ░╚██╗████╗██╔╝█████╗░░██║░░░░░██║░░╚═╝██║░░██║██╔████╔██║█████╗░░  ░░░██║░░░██║░░██║
                                                                    ░░████╔═████║░██╔══╝░░██║░░░░░██║░░██╗██║░░██║██║╚██╔╝██║██╔══╝░░  ░░░██║░░░██║░░██║
                                                                    ░░╚██╔╝░╚██╔╝░███████╗███████╗╚█████╔╝╚█████╔╝██║░╚═╝░██║███████╗  ░░░██║░░░╚█████╔╝
                                                                    ░░░╚═╝░░░╚═╝░░╚══════╝╚══════╝░╚════╝░░╚════╝░╚═╝░░░░░╚═╝╚══════╝  ░░░╚═╝░░░░╚════╝░

                                        ██╗░░██╗░█████╗░██╗░░██╗░█████╗░░██████╗██╗░░██╗██╗  ███╗░░░███╗░█████╗░████████╗░█████╗░██████╗░░██████╗██╗
                                        ██║░██╔╝██╔══██╗██║░██╔╝██╔══██╗██╔════╝██║░░██║██║  ████╗░████║██╔══██╗╚══██╔══╝██╔══██╗██╔══██╗██╔════╝██║
                                        █████═╝░███████║█████═╝░███████║╚█████╗░███████║██║  ██╔████╔██║██║░░██║░░░██║░░░██║░░██║██████╔╝╚█████╗░██║
                                        ██╔═██╗░██╔══██║██╔═██╗░██╔══██║░╚═══██╗██╔══██║██║  ██║╚██╔╝██║██║░░██║░░░██║░░░██║░░██║██╔══██╗░╚═══██╗╚═╝
                                        ██║░╚██╗██║░░██║██║░╚██╗██║░░██║██████╔╝██║░░██║██║  ██║░╚═╝░██║╚█████╔╝░░░██║░░░╚█████╔╝██║░░██║██████╔╝██╗
                                        ╚═╝░░╚═╝╚═╝░░╚═╝╚═╝░░╚═╝╚═╝░░╚═╝╚═════╝░╚═╝░░╚═╝╚═╝  ╚═╝░░░░░╚═╝░╚════╝░░░░╚═╝░░░░╚════╝░╚═╝░░╚═╝╚═════╝░╚═╝                                                                                                                                                                     

                                                                                                                                                                                                                                                                                                                                      
    """)
print("If you would like to quit this chatbot at any time, please type EXIT")
print("Hey there, welcome to Kakashi Motors automated chatbot. Please try to be concise with your questions so I can do my best to help you!")
p.speak("Hey there, welcome to Kakashi Motors automated chatbot. Please try to be concise with your questions so I can do my best to help you!")   
print("---------------------------------------------------------------")

def main():
    
    #Message if you user would like more help or if they are finished using the chatbot
    def endmsg():
        write("Is there anything else I can help you with?, Please type yes or no \n")
        p.speak("Is there anything else I can help you with?, Please type yes or no")
        again = input().lower()
        if again == "yes":
            main()
        else:
            p.speak("I hope I helped you today, thank you for your vote of confidence with Kakashi Motors")
            print("I hope I helped you today, thank you for your vote of confidence with Kakashi Motors")
            write("Goodbye")
            p.speak("Goodbye")
            exit()
    #Recommendations for bikes and all of their info (defined as a function to use for other intents
    def recommendation():
      kakashimotorshomepage = r"C:\Users\Joshk\OneDrive\Desktop\Uni Year 3\Block 2 - Global Intelligence\Final Assignment\Assessment Task 2\Chatbot\Kakashi Homepage\Index.html"
      p.speak("Let's start with the first question. What type of bike are you looking for? Please choose 1 of 4 options below")  
      recommendcategory = input("Let's start with the first question. What type of bike are you looking for?\n1 - All-rounder (Can be used everday and for other purposes)\n2 - Cruiser (For long rides or trips)\n3 - Sport (Prioritises speed)\n4 - Off-road (Used for dirt trails or driving in terrain) \n").strip()
      #------------------------------------------------------------------ALL-ROUNDERS------------------------------------------------------------------
      if recommendcategory == "1":
          print("I see you are going for the All-rounder. We have 3 different models of all-rounder bikes from different companies. \n")
          p.speak("I see you are going for the All-rounder. We have 3 different models of all-rounder bikes from different companies")
          cur.execute("SELECT name FROM `motorcycles` WHERE category_id = '1'")
          allroundernames = cur.fetchall()
          for bikes in allroundernames:
              print("\n".join(bikes))
          p.speak("Please choose a bike from the list above and type it's exact name")
          print("\nPlease choose a bike from the list above and type it's exact name")
          allrounderoption = input("\n")
          #-------------------------------------------------------F 650 cs scarver--------------------------------------------------
          if allrounderoption == "F 650 cs scarver":
              p.speak("The F six fifty C S scarver. Great choice. Please find all the information for the bike below")
              print("The F 650 cs scarver. Great choice, Please find all the information for the bike below\n")
              cur.execute("SELECT brand FROM `motorcycles` WHERE name = 'F 650 cs scarver'")
              csscarver = cur.fetchall()
              for brand in csscarver:
                  display = "".join(brand)
              print("Brand -", display)
              cur.execute("SELECT year FROM `motorcycles` WHERE name = 'F 650 cs scarver'")
              csscarver = cur.fetchall()
              for year in csscarver:
                  display = "".join(year)
              print("Year -", display)
              cur.execute("SELECT price FROM `motorcycles` WHERE name = 'F 650 cs scarver'")
              csscarver = cur.fetchall()
              for price in csscarver:
                  display = "".join(price)
              print("Price -", "£" + display)
              cur.execute("SELECT power FROM `motorcycles` WHERE name = 'F 650 cs scarver'")
              csscarver = cur.fetchall()
              for power in csscarver:
                  display = "".join(power)
              print(display, "Horsepower")
              cur.execute("SELECT fuel_capacity FROM `motorcycles` WHERE name = 'F 650 cs scarver'")
              csscarver = cur.fetchall()
              for fuel in csscarver:
                  display = "".join(fuel)
              print("Fuel Capacity -", display + "Litres")
              cur.execute("SELECT description FROM `motorcycles` WHERE name = 'F 650 cs scarver'")
              csscarver = cur.fetchall()
              for description in csscarver:
                  display = "".join(description)
              print("Description -", display)
              write("If you would like to purchase this bike after reading all the information please let me know\n1 - Purchase\n2- No\n")
              response = input().strip()
              if response == "1":
                  webbrowser.open_new(r"C:\Users\Joshk\OneDrive\Desktop\Uni Year 3\Block 2 - Global Intelligence\Final Assignment\Assessment Task 2\Chatbot\Kakashi Homepage\Index.html")
                  endmsg()
              elif response == "2":
                  p.speak("Would you like to see more information on another bike?")
                  print("Would you like to see more information on another bike? \n1 - Yes\n2 - No")
                  answer = input("\n")
                  if answer == "1":
                      recommendation()
                  elif answer == "2":
                      endmsg()
          #-------------------------------------------------------350 S 2 mach II--------------------------------------------------
          elif allrounderoption == "350 S 2 mach II":
              p.speak("The three fifty S 2 mach 2. Very nice. Please find all the information for the bike below")
              print("The 350 S 2 mach II. Very nice, Please find all the information for the bike below\n")
              cur.execute("SELECT brand FROM `motorcycles` WHERE name = '350 S 2 mach II'")
              csscarver = cur.fetchall()
              for brand in csscarver:
                  display = "".join(brand)
              print("Brand -", display)
              cur.execute("SELECT year FROM `motorcycles` WHERE name = '350 S 2 mach II'")
              csscarver = cur.fetchall()
              for year in csscarver:
                  display = "".join(year)
              print("Year -", display)
              cur.execute("SELECT price FROM `motorcycles` WHERE name = '350 S 2 mach II'")
              csscarver = cur.fetchall()
              for price in csscarver:
                  display = "".join(price)
              print("Price -", "£" + display)
              cur.execute("SELECT power FROM `motorcycles` WHERE name = '350 S 2 mach II'")
              csscarver = cur.fetchall()
              for power in csscarver:
                  display = "".join(power)
              print(display, "Horsepower")
              cur.execute("SELECT fuel_capacity FROM `motorcycles` WHERE name = '350 S 2 mach II'")
              csscarver = cur.fetchall()
              for fuel in csscarver:
                  display = "".join(fuel)
              print("Fuel Capacity -", display + "Litres")
              cur.execute("SELECT description FROM `motorcycles` WHERE name = '350 S 2 mach II'")
              csscarver = cur.fetchall()
              for description in csscarver:
                  display = "".join(description)
              print("Description -", display)
              write("If you would like to purchase this bike after reading all the information please let me know\n1 - Purchase\n2- No\n")
              response = input().strip()
              if response == "1":
                  webbrowser.open_new(r"C:\Users\Joshk\OneDrive\Desktop\Uni Year 3\Block 2 - Global Intelligence\Final Assignment\Assessment Task 2\Chatbot\Kakashi Homepage\Index.html")
                  endmsg()
              elif response == "2":
                  p.speak("Would you like to see more information on another bike?")
                  print("Would you like to see more information on another bike? \n1 - Yes\n2 - No")
                  answer = input("\n")
                  if answer == "1":
                      recommendation()
                  elif answer == "2":
                      endmsg()
          #------------------------------------------------------------Road star-------------------------------------------------------
          elif allrounderoption == "Road star":
              p.speak("The Road star. lovely bike. Please find all the information for the bike below")
              print("The Road star. lovely bike, Please find all the information for the bike below\n")
              cur.execute("SELECT brand FROM `motorcycles` WHERE name = 'Road star'")
              csscarver = cur.fetchall()
              for brand in csscarver:
                  display = "".join(brand)
              print("Brand -", display)
              cur.execute("SELECT year FROM `motorcycles` WHERE name = 'Road star'")
              csscarver = cur.fetchall()
              for year in csscarver:
                  display = "".join(year)
              print("Year -", display)
              cur.execute("SELECT price FROM `motorcycles` WHERE name = 'Road star'")
              csscarver = cur.fetchall()
              for price in csscarver:
                  display = "".join(price)
              print("Price -", "£" + display)
              cur.execute("SELECT power FROM `motorcycles` WHERE name = 'Road star'")
              csscarver = cur.fetchall()
              for power in csscarver:
                  display = "".join(power)
              print(display, "Horsepower")
              cur.execute("SELECT fuel_capacity FROM `motorcycles` WHERE name = 'Road star'")
              csscarver = cur.fetchall()
              for fuel in csscarver:
                  display = "".join(fuel)
              print("Fuel Capacity -", display + "Litres")
              cur.execute("SELECT description FROM `motorcycles` WHERE name = 'Road star'")
              csscarver = cur.fetchall()
              for description in csscarver:
                  display = "".join(description)
              print("Description -", display)
              write("If you would like to purchase this bike after reading all the information please let me know\n1 - Purchase\n2- No\n")
              response = input().strip()
              if response == "1":
                  webbrowser.open_new(r"C:\Users\Joshk\OneDrive\Desktop\Uni Year 3\Block 2 - Global Intelligence\Final Assignment\Assessment Task 2\Chatbot\Kakashi Homepage\Index.html")
                  endmsg()
              elif response == "2":
                  p.speak("Would you like to see more information on another bike?")
                  print("Would you like to see more information on another bike? \n1 - Yes\n2 - No")
                  answer = input("\n")
                  if answer == "1":
                      recommendation()
                  elif answer == "2":
                      endmsg()

      #------------------------------------------------------------------CRUISERS------------------------------------------------------------------
      elif recommendcategory == "2":
          print("I see you are going for the Cruiser. We have 3 different models of cruiser bikes from different companies. \n")
          p.speak("I see you are going for the cruiser. We have 3 different models of cruiser bikes from different companies")
          cur.execute("SELECT name FROM `motorcycles` WHERE category_id = '2'")
          allroundernames = cur.fetchall()
          for bikes in allroundernames:
              print("\n".join(bikes))
          p.speak("Please choose a bike from the list above and type it's exact name")
          print("\nPlease choose a bike from the list above and type it's exact name")
          allrounderoption = input("\n")
          #----------------------------------------------------------------R 100--------------------------------------------------------
          if allrounderoption == "R 100":
              p.speak("The R One hundred. solid choice. Please find all the information for the bike below")
              print("The R 100. solid choice, Please find all the information for the bike below\n")
              cur.execute("SELECT brand FROM `motorcycles` WHERE name = 'R 100'")
              csscarver = cur.fetchall()
              for brand in csscarver:
                  display = "".join(brand)
              print("Brand -", display)
              cur.execute("SELECT year FROM `motorcycles` WHERE name = 'R 100'")
              csscarver = cur.fetchall()
              for year in csscarver:
                  display = "".join(year)
              print("Year -", display)
              cur.execute("SELECT price FROM `motorcycles` WHERE name = 'R 100'")
              csscarver = cur.fetchall()
              for price in csscarver:
                  display = "".join(price)
              print("Price -", "£" + display)
              cur.execute("SELECT power FROM `motorcycles` WHERE name = 'R 100'")
              csscarver = cur.fetchall()
              for power in csscarver:
                  display = "".join(power)
              print(display, "Horsepower")
              cur.execute("SELECT fuel_capacity FROM `motorcycles` WHERE name = 'R 100'")
              csscarver = cur.fetchall()
              for fuel in csscarver:
                  display = "".join(fuel)
              print("Fuel Capacity -", display + "Litres")
              cur.execute("SELECT description FROM `motorcycles` WHERE name = 'R 100'")
              csscarver = cur.fetchall()
              for description in csscarver:
                  display = "".join(description)
              print("Description -", display)
              write("If you would like to purchase this bike after reading all the information please let me know\n1 - Purchase\n2- No\n")
              response = input().strip()
              if response == "1":
                  webbrowser.open_new(r"C:\Users\Joshk\OneDrive\Desktop\Uni Year 3\Block 2 - Global Intelligence\Final Assignment\Assessment Task 2\Chatbot\Kakashi Homepage\Index.html")
                  endmsg()
              elif response == "2":
                  p.speak("Would you like to see more information on another bike?")
                  print("Would you like to see more information on another bike? \n1 - Yes\n2 - No")
                  answer = input("\n")
                  if answer == "1":
                      recommendation()
                  elif answer == "2":
                      endmsg()
          #-------------------------------------------------------900 Z 1 super 4---------------------------------------------------
          elif allrounderoption == "900 Z 1 super 4":
              p.speak("The nine hundred Z one super four. Bit of a tongue twister. Please find all the information for the bike below")
              print("The 900 Z 1 super 4. A bit of a tongue twister, Please find all the information for the bike below\n")
              cur.execute("SELECT brand FROM `motorcycles` WHERE name = '900 Z 1 super 4'")
              csscarver = cur.fetchall()
              for brand in csscarver:
                  display = "".join(brand)
              print("Brand -", display)
              cur.execute("SELECT year FROM `motorcycles` WHERE name = '900 Z 1 super 4'")
              csscarver = cur.fetchall()
              for year in csscarver:
                  display = "".join(year)
              print("Year -", display)
              cur.execute("SELECT price FROM `motorcycles` WHERE name = '900 Z 1 super 4'")
              csscarver = cur.fetchall()
              for price in csscarver:
                  display = "".join(price)
              print("Price -", "£" + display)
              cur.execute("SELECT power FROM `motorcycles` WHERE name = '900 Z 1 super 4'")
              csscarver = cur.fetchall()
              for power in csscarver:
                  display = "".join(power)
              print(display, "Horsepower")
              cur.execute("SELECT fuel_capacity FROM `motorcycles` WHERE name = '900 Z 1 super 4'")
              csscarver = cur.fetchall()
              for fuel in csscarver:
                  display = "".join(fuel)
              print("Fuel Capacity -", display + "Litres")
              cur.execute("SELECT description FROM `motorcycles` WHERE name = '900 Z 1 super 4'")
              csscarver = cur.fetchall()
              for description in csscarver:
                  display = "".join(description)
              print("Description -", display)             
              write("If you would like to purchase this bike after reading all the information please let me know\n1 - Purchase\n2- No\n")
              response = input().strip()
              if response == "1":
                  webbrowser.open_new(r"C:\Users\Joshk\OneDrive\Desktop\Uni Year 3\Block 2 - Global Intelligence\Final Assignment\Assessment Task 2\Chatbot\Kakashi Homepage\Index.html")
                  endmsg()
              elif response == "2":
                  p.speak("Would you like to see more information on another bike?")
                  print("Would you like to see more information on another bike? \n1 - Yes\n2 - No")
                  answer = input("\n")
                  if answer == "1":
                      recommendation()
                  elif answer == "2":
                      endmsg()
          #--------------------------------------------------------------Mt-07 tr---------------------------------------------------------
          elif allrounderoption == "Mt-07 tr":
              p.speak("The M T zero seven T R. Fast bike. Please find all the information for the bike below")
              print("The Mt-07 tr. fast bike, Please find all the information for the bike below\n")
              cur.execute("SELECT brand FROM `motorcycles` WHERE name = 'Mt-07 tr'")
              csscarver = cur.fetchall()
              for brand in csscarver:
                  display = "".join(brand)
              print("Brand -", display)
              cur.execute("SELECT year FROM `motorcycles` WHERE name = 'Mt-07 tr'")
              csscarver = cur.fetchall()
              for year in csscarver:
                  display = "".join(year)
              print("Year -", display)
              cur.execute("SELECT price FROM `motorcycles` WHERE name = 'Mt-07 tr'")
              csscarver = cur.fetchall()
              for price in csscarver:
                  display = "".join(price)
              print("Price -", "£" + display)
              cur.execute("SELECT power FROM `motorcycles` WHERE name = 'Mt-07 tr'")
              csscarver = cur.fetchall()
              for power in csscarver:
                  display = "".join(power)
              print(display, "Horsepower")
              cur.execute("SELECT fuel_capacity FROM `motorcycles` WHERE name = 'Mt-07 tr'")
              csscarver = cur.fetchall()
              for fuel in csscarver:
                  display = "".join(fuel)
              print("Fuel Capacity -", display + "Litres")
              cur.execute("SELECT description FROM `motorcycles` WHERE name = 'Mt-07 tr'")
              csscarver = cur.fetchall()
              for description in csscarver:
                  display = "".join(description)
              print("Description -", display)
              write("If you would like to purchase this bike after reading all the information please let me know\n1 - Purchase\n2- No\n")
              response = input().strip()
              if response == "1":
                  webbrowser.open_new(r"C:\Users\Joshk\OneDrive\Desktop\Uni Year 3\Block 2 - Global Intelligence\Final Assignment\Assessment Task 2\Chatbot\Kakashi Homepage\Index.html")
                  endmsg()
              elif response == "2":
                  p.speak("Would you like to see more information on another bike?")
                  print("Would you like to see more information on another bike? \n1 - Yes\n2 - No")
                  answer = input("\n")
                  if answer == "1":
                      recommendation()
                  elif answer == "2":
                      endmsg()

      #------------------------------------------------------------------SPORTS------------------------------------------------------------------
      elif recommendcategory == "3":
          print("I see you are going for the Sport. We have 4 different models of sports bikes from different companies. \n")
          p.speak("I see you are going for the sport. We have 4 different models of sports bikes from different companies")
          cur.execute("SELECT name FROM `motorcycles` WHERE category_id = '3'")
          allroundernames = cur.fetchall()
          for bikes in allroundernames:
              print("\n".join(bikes))
          p.speak("Please choose a bike from the list above and type it's exact name")
          print("\nPlease choose a bike from the list above and type it's exact name")
          allrounderoption = input("\n")
          #----------------------------------------------------------------S 1000 R--------------------------------------------------------
          if allrounderoption == "S 1000 R":
              p.speak("S one thousand R. lightning fast. Please find all the information for the bike below")
              print("The S 1000 R. lightning fast, Please find all the information for the bike below\n")
              cur.execute("SELECT brand FROM `motorcycles` WHERE name = 'S 1000 R'")
              csscarver = cur.fetchall()
              for brand in csscarver:
                  display = "".join(brand)
              print("Brand -", display)
              cur.execute("SELECT year FROM `motorcycles` WHERE name = 'S 1000 R'")
              csscarver = cur.fetchall()
              for year in csscarver:
                  display = "".join(year)
              print("Year -", display)
              cur.execute("SELECT price FROM `motorcycles` WHERE name = 'S 1000 R'")
              csscarver = cur.fetchall()
              for price in csscarver:
                  display = "".join(price)
              print("Price -", "£" + display)
              cur.execute("SELECT power FROM `motorcycles` WHERE name = 'S 1000 R'")
              csscarver = cur.fetchall()
              for power in csscarver:
                  display = "".join(power)
              print(display, "Horsepower")
              cur.execute("SELECT fuel_capacity FROM `motorcycles` WHERE name = 'S 1000 R'")
              csscarver = cur.fetchall()
              for fuel in csscarver:
                  display = "".join(fuel)
              print("Fuel Capacity -", display + "Litres")
              cur.execute("SELECT description FROM `motorcycles` WHERE name = 'S 1000 R'")
              csscarver = cur.fetchall()
              for description in csscarver:
                  display = "".join(description)
              print("Description -", display)
              write("If you would like to purchase this bike after reading all the information please let me know\n1 - Purchase\n2- No\n")
              response = input().strip()
              if response == "1":
                  webbrowser.open_new(r"C:\Users\Joshk\OneDrive\Desktop\Uni Year 3\Block 2 - Global Intelligence\Final Assignment\Assessment Task 2\Chatbot\Kakashi Homepage\Index.html")
                  endmsg()
              elif response == "2":
                  p.speak("Would you like to see more information on another bike?")
                  print("Would you like to see more information on another bike? \n1 - Yes\n2 - No")
                  answer = input("\n")
                  if answer == "1":
                      recommendation()
                  elif answer == "2":
                      endmsg()
              
          #-------------------------------------------------------Ninja rr---------------------------------------------------
          elif allrounderoption == "Ninja rr":
              p.speak("The Ninja R R. very sporty. Please find all the information for the bike below")
              print("The Ninja rr. very sporty, Please find all the information for the bike below\n")
              cur.execute("SELECT brand FROM `motorcycles` WHERE name = 'Ninja rr'")
              csscarver = cur.fetchall()
              for brand in csscarver:
                  display = "".join(brand)
              print("Brand -", display)
              cur.execute("SELECT year FROM `motorcycles` WHERE name = 'Ninja rr'")
              csscarver = cur.fetchall()
              for year in csscarver:
                  display = "".join(year)
              print("Year -", display)
              cur.execute("SELECT price FROM `motorcycles` WHERE name = 'Ninja rr'")
              csscarver = cur.fetchall()
              for price in csscarver:
                  display = "".join(price)
              print("Price -", "£" + display)
              cur.execute("SELECT power FROM `motorcycles` WHERE name = 'Ninja rr'")
              csscarver = cur.fetchall()
              for power in csscarver:
                  display = "".join(power)
              print(display, "Horsepower")
              cur.execute("SELECT fuel_capacity FROM `motorcycles` WHERE name = 'Ninja rr'")
              csscarver = cur.fetchall()
              for fuel in csscarver:
                  display = "".join(fuel)
              print("Fuel Capacity -", display + "Litres")
              cur.execute("SELECT description FROM `motorcycles` WHERE name = 'Ninja rr'")
              csscarver = cur.fetchall()
              for description in csscarver:
                  display = "".join(description)
              print("Description -", display)
              write("If you would like to purchase this bike after reading all the information please let me know\n1 - Purchase\n2- No\n")
              response = input().strip()
              if response == "1":
                  webbrowser.open_new(r"C:\Users\Joshk\OneDrive\Desktop\Uni Year 3\Block 2 - Global Intelligence\Final Assignment\Assessment Task 2\Chatbot\Kakashi Homepage\Index.html")
                  endmsg()
              elif response == "2":
                  p.speak("Would you like to see more information on another bike?")
                  print("Would you like to see more information on another bike? \n1 - Yes\n2 - No")
                  answer = input("\n")
                  if answer == "1":
                      recommendation()
                  elif answer == "2":
                      endmsg()
          #--------------------------------------------------------------Mt-01---------------------------------------------------------
          elif allrounderoption == "Mt-01":
              p.speak("The M T zero one. excellent bike. Please find all the information for the bike below")
              print("The MMt-01. excellent bike, Please find all the information for the bike below\n")
              cur.execute("SELECT brand FROM `motorcycles` WHERE name = 'Mt-01'")
              csscarver = cur.fetchall()
              for brand in csscarver:
                  display = "".join(brand)
              print("Brand -", display)
              cur.execute("SELECT year FROM `motorcycles` WHERE name = 'Mt-01'")
              csscarver = cur.fetchall()
              for year in csscarver:
                  display = "".join(year)
              print("Year -", display)
              cur.execute("SELECT price FROM `motorcycles` WHERE name = 'Mt-01'")
              csscarver = cur.fetchall()
              for price in csscarver:
                  display = "".join(price)
              print("Price -", "£" + display)
              cur.execute("SELECT power FROM `motorcycles` WHERE name = 'Mt-01'")
              csscarver = cur.fetchall()
              for power in csscarver:
                  display = "".join(power)
              print(display, "Horsepower")
              cur.execute("SELECT fuel_capacity FROM `motorcycles` WHERE name = 'Mt-01'")
              csscarver = cur.fetchall()
              for fuel in csscarver:
                  display = "".join(fuel)
              print("Fuel Capacity -", display + "Litres")
              cur.execute("SELECT description FROM `motorcycles` WHERE name = 'Mt-01'")
              csscarver = cur.fetchall()
              for description in csscarver:
                  display = "".join(description)
              print("Description -", display)
              write("If you would like to purchase this bike after reading all the information please let me know\n1 - Purchase\n2- No\n")
              response = input().strip()
              if response == "1":
                  webbrowser.open_new(r"C:\Users\Joshk\OneDrive\Desktop\Uni Year 3\Block 2 - Global Intelligence\Final Assignment\Assessment Task 2\Chatbot\Kakashi Homepage\Index.html")
                  endmsg()
              elif response == "2":
                  p.speak("Would you like to see more information on another bike?")
                  print("Would you like to see more information on another bike? \n1 - Yes\n2 - No")
                  answer = input("\n")
                  if answer == "1":
                      recommendation()
                  elif answer == "2":
                      endmsg()
          #--------------------------------------------------------------Monster 1200 S---------------------------------------------------------
          elif allrounderoption == "Monster 1200 S":
              p.speak("The Monster one thousand two hundred S. The best bike on the market. Please find all the information for the bike below")
              print("The Monster 1200 S. the best bike on the market, Please find all the information for the bike below\n")
              cur.execute("SELECT brand FROM `motorcycles` WHERE name = 'Monster 1200 S'")
              csscarver = cur.fetchall()
              for brand in csscarver:
                  display = "".join(brand)
              print("Brand -", display)
              cur.execute("SELECT year FROM `motorcycles` WHERE name = 'Monster 1200 S'")
              csscarver = cur.fetchall()
              for year in csscarver:
                  display = "".join(year)
              print("Year -", display)
              cur.execute("SELECT price FROM `motorcycles` WHERE name = 'Monster 1200 S'")
              csscarver = cur.fetchall()
              for price in csscarver:
                  display = "".join(price)
              print("Price -", "£" + display)
              cur.execute("SELECT power FROM `motorcycles` WHERE name = 'Monster 1200 S'")
              csscarver = cur.fetchall()
              for power in csscarver:
                  display = "".join(power)
              print(display, "Horsepower")
              cur.execute("SELECT fuel_capacity FROM `motorcycles` WHERE name = 'Monster 1200 S'")
              csscarver = cur.fetchall()
              for fuel in csscarver:
                  display = "".join(fuel)
              print("Fuel Capacity -", display + "Litres")
              cur.execute("SELECT description FROM `motorcycles` WHERE name = 'Monster 1200 S'")
              csscarver = cur.fetchall()
              for description in csscarver:
                  display = "".join(description)
              print("Description -", display)
              write("If you would like to purchase this bike after reading all the information please let me know\n1 - Purchase\n2- No\n")
              response = input().strip()
              if response == "1":
                  webbrowser.open_new(r"C:\Users\Joshk\OneDrive\Desktop\Uni Year 3\Block 2 - Global Intelligence\Final Assignment\Assessment Task 2\Chatbot\Kakashi Homepage\Index.html")
                  endmsg()
              elif response == "2":
                  p.speak("Would you like to see more information on another bike?")
                  print("Would you like to see more information on another bike? \n1 - Yes\n2 - No")
                  answer = input("\n")
                  if answer == "1":
                      recommendation()
                  elif answer == "2":
                      endmsg()

      #------------------------------------------------------------------OFF-ROAD------------------------------------------------------------------
      elif recommendcategory == "4s":
          print("I see you are going for the Sport. We have 4 different models of off-road bikes from different companies. \n")
          p.speak("I see you are going for the sport. We have 4 different models of off-road bikes from different companies")
          cur.execute("SELECT name FROM `motorcycles` WHERE category_id = '3'")
          allroundernames = cur.fetchall()
          for bikes in allroundernames:
              print("\n".join(bikes))
          p.speak("Please choose a bike from the list above and type it's exact name")
          print("\nPlease choose a bike from the list above and type it's exact name")
          allrounderoption = input("\n")
          #----------------------------------------------------------------Lac Rose--------------------------------------------------------
          if allrounderoption == "Lac Rose":
              p.speak("Lac Rose. Fantastic choice. Please find all the information for the bike below")
              print("The Lac Rose. fantastic choice, Please find all the information for the bike below\n")
              cur.execute("SELECT brand FROM `motorcycles` WHERE name = 'Lac Rose'")
              csscarver = cur.fetchall()
              for brand in csscarver:
                  display = "".join(brand)
              print("Brand -", display)
              cur.execute("SELECT year FROM `motorcycles` WHERE name = 'Lac Rose'")
              csscarver = cur.fetchall()
              for year in csscarver:
                  display = "".join(year)
              print("Year -", display)
              cur.execute("SELECT price FROM `motorcycles` WHERE name = 'Lac Rose'")
              csscarver = cur.fetchall()
              for price in csscarver:
                  display = "".join(price)
              print("Price -", "£" + display)
              cur.execute("SELECT power FROM `motorcycles` WHERE name = 'Lac Rose'")
              csscarver = cur.fetchall()
              for power in csscarver:
                  display = "".join(power)
              print(display, "Horsepower")
              cur.execute("SELECT fuel_capacity FROM `motorcycles` WHERE name = 'Lac Rose'")
              csscarver = cur.fetchall()
              for fuel in csscarver:
                  display = "".join(fuel)
              print("Fuel Capacity -", display + "Litres")
              cur.execute("SELECT description FROM `motorcycles` WHERE name = 'Lac Rose'")
              csscarver = cur.fetchall()
              for description in csscarver:
                  display = "".join(description)
              print("Description -", display)
              write("If you would like to purchase this bike after reading all the information please let me know\n1 - Purchase\n2- No\n")
              response = input().strip()
              if response == "1":
                  webbrowser.open_new(r"C:\Users\Joshk\OneDrive\Desktop\Uni Year 3\Block 2 - Global Intelligence\Final Assignment\Assessment Task 2\Chatbot\Kakashi Homepage\Index.html")
                  endmsg()
              elif response == "2":
                  p.speak("Would you like to see more information on another bike?")
                  print("Would you like to see more information on another bike? \n1 - Yes\n2 - No")
                  answer = input("\n")
                  if answer == "1":
                      recommendation()
                  elif answer == "2":
                      endmsg()
              
          #-------------------------------------------------------100 g5---------------------------------------------------
          elif allrounderoption == "100 g5":
              p.speak("The 100 G five. perfect for the dirt. Please find all the information for the bike below")
              print("The 100 g5. perfect for the dirt, Please find all the information for the bike below\n")
              cur.execute("SELECT brand FROM `motorcycles` WHERE name = '100 g5'")
              csscarver = cur.fetchall()
              for brand in csscarver:
                  display = "".join(brand)
              print("Brand -", display)
              cur.execute("SELECT year FROM `motorcycles` WHERE name = '100 g5'")
              csscarver = cur.fetchall()
              for year in csscarver:
                  display = "".join(year)
              print("Year -", display)
              cur.execute("SELECT price FROM `motorcycles` WHERE name = '100 g5'")
              csscarver = cur.fetchall()
              for price in csscarver:
                  display = "".join(price)
              print("Price -", "£" + display)
              cur.execute("SELECT power FROM `motorcycles` WHERE name = '100 g5'")
              csscarver = cur.fetchall()
              for power in csscarver:
                  display = "".join(power)
              print(display, "Horsepower")
              cur.execute("SELECT fuel_capacity FROM `motorcycles` WHERE name = '100 g5'")
              csscarver = cur.fetchall()
              for fuel in csscarver:
                  display = "".join(fuel)
              print("Fuel Capacity -", display + "Litres")
              cur.execute("SELECT description FROM `motorcycles` WHERE name = '100 g5'")
              csscarver = cur.fetchall()
              for description in csscarver:
                  display = "".join(description)
              print("Description -", display)
              write("If you would like to purchase this bike after reading all the information please let me know\n1 - Purchase\n2- No\n")
              response = input().strip()
              if response == "1":
                  webbrowser.open_new(r"C:\Users\Joshk\OneDrive\Desktop\Uni Year 3\Block 2 - Global Intelligence\Final Assignment\Assessment Task 2\Chatbot\Kakashi Homepage\Index.html")
                  endmsg()
              elif response == "2":
                  p.speak("Would you like to see more information on another bike?")
                  print("Would you like to see more information on another bike? \n1 - Yes\n2 - No")
                  answer = input("\n")
                  if answer == "1":
                      recommendation()
                  elif answer == "2":
                      endmsg()
          #--------------------------------------------------------------Pw80---------------------------------------------------------
          elif allrounderoption == "Pw80":
              p.speak("The P W eighty. wondeful choice. Please find all the information for the bike below")
              print("The Pw80. wonderful choice, Please find all the information for the bike below\n")
              cur.execute("SELECT brand FROM `motorcycles` WHERE name = 'Pw80'")
              csscarver = cur.fetchall()
              for brand in csscarver:
                  display = "".join(brand)
              print("Brand -", display)
              cur.execute("SELECT year FROM `motorcycles` WHERE name = 'Pw80'")
              csscarver = cur.fetchall()
              for year in csscarver:
                  display = "".join(year)
              print("Year -", display)
              cur.execute("SELECT price FROM `motorcycles` WHERE name = 'Pw80'")
              csscarver = cur.fetchall()
              for price in csscarver:
                  display = "".join(price)
              print("Price -", "£" + display)
              cur.execute("SELECT power FROM `motorcycles` WHERE name = 'Pw80'")
              csscarver = cur.fetchall()
              for power in csscarver:
                  display = "".join(power)
              print(display, "Horsepower")
              cur.execute("SELECT fuel_capacity FROM `motorcycles` WHERE name = 'Pw80'")
              csscarver = cur.fetchall()
              for fuel in csscarver:
                  display = "".join(fuel)
              print("Fuel Capacity -", display + "Litres")
              cur.execute("SELECT description FROM `motorcycles` WHERE name = 'Pw80'")
              csscarver = cur.fetchall()
              for description in csscarver:
                  display = "".join(description)
              print("Description -", display)
              write("If you would like to purchase this bike after reading all the information please let me know\n1 - Purchase\n2- No\n")
              response = input().strip()
              if response == "1":
                  webbrowser.open_new(r"C:\Users\Joshk\OneDrive\Desktop\Uni Year 3\Block 2 - Global Intelligence\Final Assignment\Assessment Task 2\Chatbot\Kakashi Homepage\Index.html")
                  endmsg()
              elif response == "2":
                  p.speak("Would you like to see more information on another bike?")
                  print("Would you like to see more information on another bike? \n1 - Yes\n2 - No")
                  answer = input("\n")
                  if answer == "1":
                      recommendation()
                  elif answer == "2":
                      endmsg()
              
              
              
                  
    #Typewriter effect - Found (https://replit.com/talk/learn/Typewriter-effect-Python/139897)
    def write(write):
        for i in write:
            sys.stdout.write(i)
            sys.stdout.flush()
            time.sleep(.04)

              
    #Local HTML homepage for Kakashi motors outside of function  
    kakashimotorshomepage = r"C:\Users\Joshk\OneDrive\Desktop\Uni Year 3\Block 2 - Global Intelligence\Final Assignment\Kakashi Homepage\Index.html"
    
    #Grabs user input
    write("What can I help you with? \n")
    p.speak("What can I help you with?")
    userinput = input().lower()
        
    #Connects to Wit.ai and grabs the response string to identify intent
    wit_response = client.message(userinput)

    #INTENT - Purchase an item
    if ("purchase_items" in str(wit_response)):
     p.speak("Do you know what bike you would like to purchase?")
     biketobuy = input("Do you know what bike you would like to purchase?\n1 - Yes \n2 - No \n").strip()
     if biketobuy == "1":
      print("Perfect. You can order a motorcycle from our website, would you like me to open it for you? Please type 1 for yes and 2 for no \n")
      p.speak("Perfect. You can order a motorcycle from our website, would you like me to open it for you? Please type 1 for yes and 2 for no")
      open_website = input("1 - Yes \n2 - No \n ").strip()
      if open_website == "1":
        webbrowser.open_new(r"C:\Users\Joshk\OneDrive\Desktop\Uni Year 3\Block 2 - Global Intelligence\Final Assignment\Assessment Task 2\Chatbot\Kakashi Homepage\Index.html")
        endmsg()
      elif open_website == "2":
         endmsg()
     elif biketobuy == "2":
      p.speak("That's no worries. Would you like some recommendations?")
      recommendbike = input("That's no worries. Would you like some recommendations? \n1 - Yes\n2 - No \n")
      if recommendbike == "1":
             p.speak("Amazing")
             print("Amazing")
             recommendation()
      elif recommendbike == "2":
             endmsg()

    #INTENT - Power of motorcycles
    elif ("power_limit" in str(wit_response)):
     p.speak("The limit of a motorcycle power without a full licence is 125 horsepower and with a full icense it is 200 horsepower")
     print("No license - 125HP  |  Full license - 200HP")
     endmsg()
     
    #INTENT - Request website
    elif ("request_website" in str(wit_response)):
     p.speak("Our website is w w w dot kakashi motors dot com")
     print("www.kakashimotors.com")
     p.speak("Would you like me to open it for you?")
     request_open_website = input("1 - Yes \n2 - No \n ").strip()
     if request_open_website == "1":
         webbrowser.open_new(r"C:\Users\Joshk\OneDrive\Desktop\Uni Year 3\Block 2 - Global Intelligence\Final Assignment\Assessment Task 2\Chatbot\Kakashi Homepage\Index.html")
         endmsg()
     elif request_open_website == "2":
         endmsg()
     
    #INTENT - Stores open times
    elif ("store_times" in str(wit_response)):
     print("Moday to Friday - 9:00AM to 7:00PM  |  Ssaturday & Sunday 10:00AM to 6:00PM")
     p.speak("All stores are open from Monday to Friday at 9 A M to 7 P M and 10 A M to 6 P M on Saturday and Sunday")
     endmsg()
     
    #INTENT - Stores locations
    elif ("store_locations" in str(wit_response)):
        print("I have identified that you are looking for a store location, however, I need to know which store is closer to you. Please type 1 for Manchester and 2 for London")
        p.speak("I have identified that you are looking for a store location however, I need to know which store is closer to you. Please type 1 for Manchester and 2 for London")
        where = input("1 - Manchester \n2 - London \nInput: ").strip()
        if where == "1":
            print("Manchester store - 21 New Cathedral St, Manchester, M1 1AD")
            p.speak("Our Manchester store is located on 21 new cathedral street. I have listed the full address. Would you like me to open the location on google maps, type 1 for yes and 2 for no")
            open_location = input("1 - Yes \n2 - No \nInput: ").strip()
            if open_location == "1":
                webbrowser.open("https://goo.gl/maps/E1LCusbuLDg1gYbx7")
            elif open_location == "2":
             endmsg()
        elif where == "2":
            print("London store - 333 Oxford St, London, W1S 1DA")
            p.speak("Our London store is located on 333 oxford street. I have listed the full address. Would you like me to open the location on google maps, type 1 for yes and 2 for no")
            open_location = input("1 - Yes \n2 - No \nInput: ").strip()
            if open_location == "1":
                webbrowser.open_new("https://goo.gl/maps/d7sxj7LvLLCpSi6D8")
            elif open_location == "2":
             endmsg()

    #INTENT - More information
    elif ("more_information" in str(wit_response)):
     p.speak("Our Sales executive teams manager is Tony and his number is listed below, if you are unable to contact him, both store contact numbers are also listed")
     print("Name: Tony Thomas-Butler  |  Contact number - +44 07938451332")
     print("Manchester store - 0161 507 1992  |  London store - 0161 246 5201")
     endmsg()

    #INTENT - Warranty
    elif ("vehicle_warranty" in str(wit_response)):
     p.speak("We offer warranty for 1, 2 and 5 years with all of our vehicles, for more information on prices of warranty please visit our website")
     print("www.kakashimotors.com")
     p.speak("Would you like me to open it for you?")
     request_open_website = input("1 - Yes \n2 - No \n ").strip()
     if request_open_website == "1":
         new = 2
         webbrowser.open(kakashimotorshomepage,new=new)
         endmsg()
     elif request_open_website == "2":
         endmsg()

    #INTENT - Vehicle problems
    elif ("vehicle_problems" in str(wit_response)):
     p.speak("We have recommended mechanics in both Manchester and London who offer 10% off to our customers")
     print("London - DS AUTOS LONDON LTD - 07906649769  |  Manchester - M60 Autos - 01614257660 ")
     endmsg()

    #INTENT - Recommendations
    elif ("vehicle_recommendations" in str(wit_response)):
     p.speak("I have identified that you are looking for recommendations. Is that correct?\n1 - Yes\n2 - No")
     response = input("I have identified that you are looking for recommendations. Is that correct?\n1 - Yes\n2 - No\n")
     if response == "1":
         p.speak("Absolutely")
         print("Absolutely")
         recommendation()
     elif response == "2":
         endmsg()

    #INTENT - Sales
    elif ("any_sales" in str(wit_response)):
     p.speak("We currently have a sale of 15% off for customers who sign up and order online in the next week! Head over to our website to see more information")
     print("15% off until the 16th of December")
     endmsg()

    #INTENT - Payment methods
    elif ("payment_methods" in str(wit_response)):
     p.speak("We accept credit and debit cards from any country in the world on our online store and in our pyhsical store we can also accept cash")
     print("We accept credit and debit cards from any country in the world on our online store and in our pyhsical store we can also accept cash")
     endmsg()

    #INTENT - Shipping
    elif ("shipping_time" in str(wit_response)):
     p.speak("We can ship a motorcycle to any address in the United Kingdom in 2 to 3 days for 150 pounds. If you are outside of the UK it can take up to 2 weeks depndening on what country you want the bike delivered to and will cost 250 pounds")
     print("We can ship a motorcycle to any address in the United Kingdom in 2 to 3 days for 150 pounds. If you are outside of the UK it can take up to 2 weeks depndening on what country you want the bike delivered to and will cost 250 pounds")
     endmsg()

    #INTENT - Free delivery
    elif ("free_delivery" in str(wit_response)):
     p.speak("With purchases over 7 and a half thousand pounds, we offer free delivery inside the UK. Outside the UK the order must be ten thousand pounds more more for free delivery")
     print("With purchases over £7,500, we offer free delivery inside the UK. Outside the UK the order must be over £10,000 pounds for free delivery")
     endmsg()

    #INTENT - Returns
    elif ("return_products" in str(wit_response)):
     p.speak("We have a strict no return policy however, in certain circumstances we will accept a return")
     print("We have a strict no return policy however, in certain circumstances we will accept a return")
     endmsg()

     #INTENT - Problems with website
    elif ("website_problems" in str(wit_response)):
     p.speak("We are sorry to hear that. Our web development team are working on fixing it now. Would you like to speak with our manager")
     pww_contact = input("1 - Yes \n2 - No \nInput: ").strip()
     if pww_contact == "1":
         p.speak("Our Sales executive teams manager is Tony and his number is listed below")
         print("Name: Tony Thomas-Butler  |  Contact number - +44 07938451332")
     elif pww_contact == "2":
         endmsg()

    #-------------------------------------Unrelated questions-------------------------------------|
    #INTENT - Hello
    elif ("hello_greeting" in str(wit_response)):
     p.speak("Hello")
     print(":-}")
     endmsg()

    #INTENT - Name request
    elif ("name_request" in str(wit_response)):
     p.speak("My name is Mr Kakashi, it is a pleasure to meet you")
     print(":-}")
     endmsg()

    #INTENT - How are you
    elif ("artificial_feelings" in str(wit_response)):
     p.speak("I am doing very well thank you")
     endmsg()

    #INTENT - Are you a robot
    elif ("robot_response" in str(wit_response)):
     p.speak("Yes I am a robot but I was designed by a human and created for the sole purpose of helping you")
     print("Created by: Joshua Thomas-Butler")
     endmsg()

    #-------------------------------------Unrelated questions-------------------------------------|
    #Ends program
    elif ("exit" in userinput) or ("quit" in userinput):
     p.speak("Thank you for choosing Kakashi Motors, have a nice day")
     print("Goodbye :-)")
     

    #If users input is not recognized  	
    else:
     p.speak("I'm sorry, I did not quite understand your enquiry, please try again or rephrase your question")
     print("I'm sorry, I did not quite understand your enquiry, please try again or rephrase your question")
     main()

main()
