
# E-commerce Website Automation Testing Project
This is a UI automation testing project for a mock e-commerce website "https://automationexercise.com/" done using **Python**, **Selenium**, and **Behave**


## Project Summary
Framework: Behave (BDD) <br>
Language: Python <br>
Tool: Selenium WebDriver <br>
Scenarios: 13–14 total <br>
Functionalities Tested: Login, Search, Cart, Register, Checkout <br>
Reports: screenshots included<br>
Status: Fully functional for most scenarios<br>
Version control: Git and Github

## Types of Testing Covered
Positive Testing* – Valid login, registration, add to cart <br>
Negative Testing– Invalid login, empty search input<br>
End-to-End Testing – Full flow: Register → Login → Add to Cart → Checkout<br>
UI Functional Testing – Buttons, links, forms, layout visibility<br>

## Setup Instructions
1. Install packages: `pip install selenium behave`
2. Run tests: `behave`
3. Ensure Microsoft Edge is installed and Edge WebDriver is in PATH

## How to Run the Tests
1. **Clone the repository**:
   ```
   git clone https://github.com/SakshamSharma2601/Automation_Behave_Project.git
   cd ecommerce-automation
   ```
2. **Create a virtual environment**:
   ```
   python -m venv venv
   source venv/bin/activate  # or venv\Scripts\activate on Windows
   ```
3. **Install dependencies**:
   ```
   pip install -r requirements.txt
   ```
4. **Run tests**:
   ```
   behave
   ```
   <br>
## Note on Register Functionality
The registration functionality (`register.feature`) is designed to work with a **unique username/email** and will **only run successfully once** with the provided data.<br>
To re-run the registration test:
- Manually update the username/email in the test data<br>
- Or maybe generate a random/unique user every time <br>
It is expected behavior and not a bug.


