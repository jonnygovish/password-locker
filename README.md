# password-locker
An application that allows the user to generate and store password for various accounts
## Created by [John Mutavi](https://github.com/jonnygovish)

## Description
This is an application that stores a user's website password. It allows the user to generate random password and other information which it stores safely. In addition, it enable a user to store and generate websites password for various accounts.

## User Specifications
* To create an account with user details - log in and password
* Store user existing login credentials
* Generate a password for a new credential/account

## Behaviours
| Behaviour | Input | Output |
| ------------ |:----------:| -------: | 
| Create user account | User_name: Puppah <br> Password: battousae| Hello Puppah, your account has been created |
| User Login|  User_name: Puppah <br> Password: battousae |  Welcome Puppah,how are you today?. What would you like to do? | 
| Create a Credential|Account name/ Site name: facebook <br> Site user_name: Govish <br> Site Password: 7kDzR6^l |New created account: <br> Account:facebook <br> User Name:Govish <br> Password:  7kDzR6^l |
| Display Credentials | DA| Site:Facebook <br> User Name:Govish <br> Password:7kDzR6^l|
| Genearate password or Enter existing passord|ep or gp  |Ep: Hakunapassword <br> or <br> gp: 7kDzR6^l |
| Exit Application | ex  | Come back again.......Goodbye!!|

## Installation
Clone this repo to a folder on your computer with

git clone  https://github.com/jonnygovish/password-locker.git

Run the run.py script to open the program.

## Technologies Used
* Python 3.6
## License
MIT (C) **[John Mutavi](https://github.com/jonnygovish)**
