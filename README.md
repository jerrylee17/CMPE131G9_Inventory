[![Build Status](https://travis-ci.com/jerrylee17/CMPE131G9_Inventory.svg?branch=master)](https://travis-ci.com/jerrylee17/CMPE131G9_Inventory)

Instructions to run Application

-Application starts at main-menu page
-From main page, user can have access to al features of the application
-In order to make changes that affect the database, user needs to log in
-Users have different credentials that allow them to access high level procedures

8 Features of the application

-Login
-Logout
-Register
-Input Ingredients
-Order Food

# CMPE131G9_Inventory

Due to the large number of ingredients that a restaurant uses for its operation, it is sometimes difficult to keep track of every single product. Consequently, a lack of a proper inventory can lead to producing waste, monetary losses, and food poisoning. Our application aims to properly and accurately manage, track, and reduce the waste of perishable and non-perishable products of a restaurant. The main features include keeping an inventory of supplies, tracking sales, ordering supplies, and alerting managers when products are near their due date.

Our application will be active in most operations run by the restaurant. For example, there will be a function for when the restaurant receives supplies, as well as for when a dish is ordered. We will have an input method for which a food type is selected and a number value for the amount of food added. This will be added to our database after every input. A similar interface will also be available for whenever a dish is ordered, with food type and amount number. We could have pre-calculations for how much of each ingredient is used per dish. For example, a plate of spaghetti being ordered would deduct our overall supply of paste, meatballs, etc. There should be a get method to determine how much supply of an ingredient there is left, as well as an automated alert system if something runs low in supply so we know to restock. A good way to display all this information would be the use of gauges and color-coding it based on how much supply we have left. We will also provide a way for the user to see the costs and profits of their different dishes. By seeing the costs and sales of each different type of order, they can determine the trends based on which dishes are the most popular.

Furthermore, our application has competitors such as BlueCart and Orderly to name a few.  BlueCart is similar to our application because it allows its customers to browse through different foods.  It possesses a high variety of food catalog products that restaurants can order depending on their needs. The big catch with BlueCart is that its a wholesaler, which forces clients to buy in bulk; opposed to buying in small quantities to meet restaurant demands.  Also, another competitor is Orderly and it has features that we want our application to possess.  Orderly is the closest platform to our application’s design.  Some of these features are managing and controlling food costs, which is what our team is advocating for.  For our application to thrive in this industry, the application must be easy to navigate, provide graphical visuals to the user, and possess some of the features that our competitors possess.  The application must bring the most useful and important features together to be able to compete with these platforms.

	Some of the challenges we will face include figuring out a way to store and organize different types of food and their quantities. We could use a text file to store all the different types of food we have. This will allow us to organize the different food types with ease and read or modify the file. Another challenge would be creating a way to show the user how much of each food supply is left. For this, we will need to create some sort of unique user interface for all the different ingredients and their remaining quantities. One solution would be to use tabs and boxes to display a list of ingredients next to the numerical value of their remaining amount in ounces or something. Another way would be to use a more visualizing appealing display, like a bar graph. Finally, we need to create a way for the user to see and compare the costs and profits of different meals. We can do this by calculating the costs of a specific supply of food per week for example, as well as finding the number of sales per week. This could also be displayed in a table, or a line chart.
