# Password Generator Dashboard
An interactive __Streamlit-based Password Generator__ application that allows users to generate secure passwords using three different strategies:
* PIN Code Generator
* Random Password Generator
* Memorable Password Generator  

The application provides a simple and user-friendly dashboard for customizing password options and generating secure credentials instantly.


## Features
### PIN Code Generator
* Select PIN length (4–10 digits)
* Generates numeric-only secure PIN codes

### Random Password Generator
* Select password length (8–32 characters)
* Optional inclusion of:
    - Numbers
    - Symbols
* Generates strong, randomized passwords

### Memorable Password Generator
* Select number of words (2–10)
* Custom separator (default: -)
* Optional word capitalization
* Generates human-readable but secure passwords


## User Interface
The application is built with Streamlit and includes:
* Clean dashboard layout
* Interactive sliders and toggles
* Dynamic password generation
* Custom banner image support


## Project Structure
```.
├── src/
│   └── password_generator.py
|   └── dashboard.py
├── image/
│   └── banner.png
└── README.md
```
* `dashboard.py` → Streamlit dashboard
* `password_generator.py` → Core password generator classes
* `image/banner.png` → UI banner image


## Object-Oriented Design
This project follows Object-Oriented Programming (OOP) principles: 
* Class-based architecture
* Encapsulation of password logic
* Modular and scalable design
* Clear separation between UI and business logic