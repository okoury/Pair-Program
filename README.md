# 🌐 Web Form Application

A Python Flask web application that demonstrates form handling and basic error handling. Users can submit a form with various input fields, and the submitted data is stored in a list. The application also handles 404 and 500 errors, displaying relevant web pages.

## 🚀 Getting Started

### Prerequisites

- Python 3.6 or higher
- Flask 1.0 or higher

### Running the Application

1. 📁 Clone this repository to your local computer.
2. 🐍 Create a new virtual environment:
   - Windows: `python -m venv ./venv`
   - Mac: `python3 -m venv ./venv`
3. 🌐 Activate the new virtual environment:
   - Windows: `.\venv\Scripts\activate`
   - Mac: `source ./venv/bin/activate`
4. 📦 Install the dependencies: `pip install Flask`
5. 🚦 Run the application with `python app.py`

## 💻 Skills Utilized

This project helped me develop and showcase the following skills:

- Python
- Flask web framework
- Jinja2 template engine
- HTML5
- CSS3
- Bootstrap 5
- JavaScript
- Handling HTTP methods (GET, POST)
- Custom error pages (404, 500)
- Form handling and processing
- Flash messages for user alerts
- Basic navigation with templates

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white)
![Jinja2](https://img.shields.io/badge/Jinja2-B41717?style=for-the-badge&logo=jinja&logoColor=white)
![HTML5](https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white)
![CSS3](https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white)
![Bootstrap](https://img.shields.io/badge/Bootstrap-7952B3?style=for-the-badge&logo=bootstrap&logoColor=white)
![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black)

## 📂 File Structure

- `app.py`: The main Flask application file.
- `templates/`: Contains the HTML templates.
  - `index.html`: Main form template.
    - Extends `base.html`.
    - Displays the form for entering information about digital product management (title, author, pages, classification, details, and acquisition).
    - Shows a table with the submitted information.
  - `about.html`: About page.
  - `base.html`: Base template for layout inheritance.
    - Contains the basic HTML structure, including the DOCTYPE declaration, head, and body elements.
    - Imports Bootstrap 5 CSS and JavaScript libraries for styling and functionality.
    - Includes a simple navigation menu with links to the home and about pages.
    - Provides a container for the main content, which is filled by the content of the child templates using Jinja's block tags.
    - Handles flash messages for displaying alerts.
  - `404.html`: Custom 404 error page.
  - `500.html`: Custom 500 error page.



