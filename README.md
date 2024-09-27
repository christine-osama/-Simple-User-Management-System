# -Simple-User-Management-System
Description:

This Python script implements a basic user management system. It allows users to:

1.Create new users: Users can enter their first name, last name, email address, and password to create a new user account.
2.Display all users: After adding users, this option displays information about all created users, including their first and last name, email, password (for demonstration purposes, avoid storing passwords in plain text in real applications), and current status (which is currently set to "inactive" by default).
3.Exit: Users can exit the program at any point.
Key Features:

*User object creation: The User class stores user information (first name, last name, email, password, and status).
*Clear screen function: The clear_screen function clears the console screen for a better user experience when switching between menu options.
*User input validation: While not explicitly implemented in this code, consider adding validation for user input (e.g., email format, password strength) to enhance robustness.
*Status management: The status attribute in the User class could be used to track user account activation or additional information like account type in more advanced systems.
