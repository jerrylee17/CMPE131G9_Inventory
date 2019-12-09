[![Build Status](https://travis-ci.com/jerrylee17/CMPE131G9_Inventory.svg?branch=master)](https://travis-ci.com/jerrylee17/CMPE131G9_Inventory)

# MasterKitchen, the ultimate tool for a MasterChef

Masterkitchen is a utility that allows restraunts to keep track of their inventory. Masterkitchen comes with a variety of tools, as described below in the features, that helps control the chaos of finding ingredients. 

# Running this repository locally

1. Clone this repository:

```
git clone https://github.com/jerrylee17/CMPE131G9_Inventory.git
```

2. Install all necessary packages
```
pip install -U -r requirements.txt
```
3. set ```FLASK_APP``` to the proper file

<p align="center"> Windows</p>

```
set FLASK_APP=app
```

<p align="center"> Linux</p>

```
export FLASK_APP=app
```

# Information

Github repository: https://github.com/jerrylee17/CMPE131G9_Inventory

Website deployment: https://masterkitchen.herokuapp.com/main

# Main features

**1. Login Page.**
  
  Login Page is prompt once the application starts.

**2. Log out function**

  Log out of the application

**3. Register Page**

  Registers a new user. Click on the option "register" which is located in the login page. Enter a username, password, and confirm password. 

**4. Navigation Bar**

  A main navigation bar is displayed for easy access to all features. It is located at the top of the web page application.
  
**5. Input ingredient option**
  
  Input ingredients into the database of the website. To input ingredients, click "Input ingredients" in the navigation bar and input the ingredients from the dropdown. 
  
**6. Detailed Dish Recipe**

  Enter a new dish in the menu. To do this, access the dynamic webpage "Make Dish" by clicking "New Dish" in the navigation bar. When at the page, enter the dish name and add or remove ingredients accordingly. When "Create dish" is pressed, there will either be an error page that tells you where the error in the dish is or the dish will be made.

**7. Menu**

  View the current menu, or all of the dishes that have been inputted into the database

**8. Order Food**

  This feature allows users to order food to be made by the kitchen. To access this feature, select the "Order Food" option located in the navigation bar, select the dish, and click on order food button. 

**9. Checking stock by dish**

  This feature allows you to check the stock of every ingredient within a dish. To access this feature, select "stock" from the navigation bar and select "By Dish". Then, select the dish from the dropdown and click "Check!" Every product in the dish will be listed below, along with their product ID and their quantity. 

**10. Checking stock by ingredient**

  This feature allows you to check the stock of a single ingredient. To access this feature, select "stock" from the navigation bar and select "By Ingredient". Then, select the ingredient from the dropdown and click "Check!" The ID number and current stock of the ingredient will be given.  
  
**11. Food Disposal**
  
  This feature allows you to dispose of food that has gone bad or is potentially hazardous. To do this, select "Dispose" from the navigation bar. Select which ingredient to dispose of and enter the quantity. Then, add any comments as to why this ingredient is being thrown out. Then, click "Remove from Inventory" to complete the disposal method.
 
**10. Disposal Record**

  This feature allows you to view the disposal record. It allows you to view if someone has disposed of food incorrectly or just messed with the database. To view the disposal record, click on "Disposal Record" in the navigation bar. 
  
**11. "Enter a new dish" feature**
  
  A feature that allows a user with proper credentials to create a new dish. Name , ingredients, and quantities will be saved to the "detail dish recipe" database. To access this feature, select the "Enter Menu" option located in the navigation bar, enter the name of the dish, and enter the name of the ingredient, quantity, and unit measure. To create the new dish, click on "Create Dish" button.
  
**12. Main dashboard for users**

  This is the main dashboard where everything about the website will be displayed. To access this, click on "Home".

**13. Good flow of website**

  Every page of this website is encoded with a "go back" button. For example, when an ingredient is inputted, the user will either be directed to an error page that explains what is wrong with the ingredient input or it will lead the user to a "delivery successful" page. Each of these pages will have a go back button that allows the user to go back to filling out the form. This page exists in each of the pages, including "Input Ingredients", "New Dish", "Order Food", and each page within "Stock". 

# Testing
  All tests are located in the testing folder, which is in the main repository folder.
  They can be run by using the command pytest in the terminal

# Documentation

After cloning the file, go to ```./docs/build/html```. All of the documentation is within that folder. To view the full documentation, open ```index.html``` with a live server. 
