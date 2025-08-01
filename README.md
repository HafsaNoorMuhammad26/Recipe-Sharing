# 🍽️ Recipe Sharing Platform

A Django-based web application where users can discover, share, and save their favorite recipes. Built with user-friendly features, allowing a seamless experience for both contributors and food enthusiasts.

## 📌 Features

- 👩‍🍳 **User Authentication**
  - Sign up, log in, log out functionality
  - Role-based access for contributors and general users

- 📖 **Recipe Management**
  - Add, edit, delete, and view detailed recipes
  - Upload recipe images, ingredients, and step-by-step instructions

- 🔍 **Search & Filter**
  - Search recipes by name or ingredients
  - Filter recipes by category or cooking time

- 🖼️ **Image Upload**
  - Add appetizing images to each recipe using Django media handling

## 🛠️ Tech Stack

- **Backend**: Django (Python)
- **Frontend**: HTML, CSS, Bootstrap
- **Database**: SQLite (default)
- **Version Control**: Git & GitHub

## 🚀 Getting Started

### 🔧 Prerequisites

- Python 3.6+
- Django 4.x or later
- Git

### 🧩 Installation

```bash
# Clone the repository
git clone https://github.com/HafsaNoorMuhammad26/Recipe-Sharing.git
cd Recipe-Sharing

# Create a virtual environment
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run migrations
python manage.py migrate

# Start the server
python manage.py runserver
````

### 🔐 Create a Superuser

```bash
python manage.py createsuperuser
```

Then go to `http://127.0.0.1:8000/admin/` to access the admin dashboard.

## 📁 Project Structure

```
Recipe-Sharing/
├── manage.py
├── recipe_sharing/
│   ├── settings.py
│   ├── urls.py
│   └── ...
├── templates/
│   └── ...
├── static/
│   └── ...
├── media/
│   └── recipe_images/
```


## 👩‍💻 Author

**Hafsa Noor Muhammad**

* 🌐 [GitHub](https://github.com/HafsaNoorMuhammad26)
* 💼 Software Engineering Student | Junior Data Analyst
* 📎 [LinkedIn](https://www.linkedin.com/in/hafsa-noor-muhammad-67b96331a/)


⭐ If you found this project helpful, don’t forget to star the repo and share with your peers!
