# Project Name: The Concord School Management System Software

## Reason for Creating the School Management System
The School Management System was created for my high school to make many processes easier for staff and give them a way of storing vital information. I explain each app in my web app and their functions in detail below

## Academic
Mainly contains information about the school's classes, department.. Each class has a guide teacher. The app also contains a Current session to which students are enrolled every session. There can only be one current session at a time.

## Account
3 major types of accounts currently: Either a user is an admin, a student or a teacher. They each have different dashboard views and are able to perform or view different functions. Each Guide Teacher gets to view only his/her class information, can only create attendance or prepare results for his/her students. And each child can only view his' /her's information

## Employee
Mainly collects information on school staffs

## Inventory
Used to keep tracks of the school's assests, where they are at a particular point, their value and quantity. Items can also be assigned to classes like school notes, textbooks etc, hence the school can keep track of who received what item and at what time.

## Library
Library feature similar to the inventory. Helps keep track of books. Books can be isssued to enrolled students and a return date set. Admin can view due books and who borowed them..

## Result
Each subject teacher is able to create a result for the student taking that subject. The Class Teacher can then prepare the result for each student in his/her class. Each result gets approved by the admin and then can be viewed by each child using on their dashboard.

## Store
An In-school store for students/parents to buy school items. They can add/remove items from their cart. View their cart at any time. Get and view discount prices on items and soon will be able to pay using paystack

## Student
Mainly collects student info. Students are to be enrolled each term based on a change in session. 

## Teacher
Collects teacher information

## Timetable
Creates an automated timetable for the school. This timetable collects the information of teachers; their unavailable days, subjects they teach, number of times the subjects are taught and generates an automated timetable that does not overlap teachers or subjects


## How To Setup On Linux
1. Clone This Project `git clone https://github.com/lawalkeyd/school_management_system.git`
2. Go To Project Directory `cd school_management_system`
3. Create a Virtual Environment `virtualenv env`
4. Activate Virtual Environment `source env/bin/activate`
5. Install Requirements Package `pip install -r requirements.txt`
6. Migrate Database `python manage.py migrate`
7. Create Super User `python manage.py createsuperuser`
8. Finally Run The Project `python manage.py runserver`

### This project was initially forked from sajib1066/school_management_system.
