# WeatherApplication

This application is used to display the weather of a particular city. Users have the flexibility to add the new city to monitor the weather.

![image](https://user-images.githubusercontent.com/85877860/176993301-56c993cf-bbc5-4cc1-acaf-84dcc72e3e37.png)


# Steps to run the application in your laptop
1. Clone the repository to your local laptop using the command - git clone <repo_url>
2. Install Python3 and run the below command from the repository directory(WeatherApplication) to install the pre-requisite python packages that are required.
  
    pip3 install -r requirements.txt
  
3. Install the Postgres DataBase Server using the link - https://www.sqlshack.com/how-to-install-postgresql-on-windows/
4. run the database script under dbscripts/dbscript.sql file to create the table.
5. Once the packages are installed without any errors and database table is created, run the python file - app.py to start the application.
6. Access the application in your browser using the URL - http://localhost:5000/weather
