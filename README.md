# Personal Portfolio — Django Beginner Assignment

A simple personal portfolio website built with **Django, HTML, and CSS**,
following the standard Django flow: **Model → View → URL → Template**.

## Features

- **Home page** — name, profile picture, short introduction, skills list, navigation menu
- **Projects page** — all projects displayed as cards (title, short description, technologies, GitHub link)
- **Project details page** — full information for a single project at `/projects/<id>/`
- **Django Admin** — add, edit, and delete projects from `/admin/`
- **Responsive design** — sticky navbar with a mobile hamburger menu, project cards, buttons, footer
- **Bonus features included**:
  - About page (`/about/`)
  - Optional project images (via `ImageField`, shown on cards and detail page)
  - "View on GitHub" button on every project
  - Contact section (`/contact/`)

## Technologies Used

- Python 3 / Django 6.1
- **PostgreSQL** (database, configured in `settings.py`)
- Pillow (for project image uploads)
- python-dotenv (loads `.env` config)
- HTML5, CSS3 (custom, no framework — hand-written responsive layout)
- Vanilla JavaScript (mobile nav toggle only)

## Project Structure

```
portfolio_project/        # Django project (settings, root urls)
portfolio/                 # Django app
    models.py               # Project model
    views.py                # home, about, contact, project_list, project_detail
    urls.py                 # app routes
    admin.py                 # ProjectAdmin registration
    templates/portfolio/    # base.html, home.html, projects.html,
                             # project_detail.html, about.html, contact.html
    static/portfolio/css/   # style.css
manage.py
requirements.txt
```

## Installation / Setup

1. **Clone the repository**
   ```bash
   git clone <your-repo-url>
   cd portfolio_project
   ```

2. **Create and activate a virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate       # on Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up PostgreSQL**

   Create a database matching `portfolio_project/settings.py`:
   ```sql
   -- inside psql
   CREATE DATABASE django_batch_12;
   -- uses the existing 'postgres' role — set its password to match settings.py
   ALTER USER postgres WITH PASSWORD 'pgadmin';
   ```

   The connection is configured directly in `portfolio_project/settings.py`:
   ```python
   DATABASES = {
       'default': {
           'ENGINE': 'django.db.backends.postgresql',
           'NAME': 'django_batch_12',
           'USER': 'postgres',
           'PASSWORD': 'pgadmin',
           'HOST': '127.0.0.1',
           'PORT': '5432',
       }
   }
   ```
   Update these values (especially `USER`/`PASSWORD`) to match your local
   PostgreSQL setup before running migrations.

5. **Run migrations**
   ```bash
   python manage.py migrate
   ```

6. **Create an admin (superuser) account**
   ```bash
   python manage.py createsuperuser
   ```

7. **Run the development server**
   ```bash
   python manage.py runserver
   ```

8. Visit:
   - Site: http://127.0.0.1:8000/
   - Admin panel: http://127.0.0.1:8000/admin/ (log in and add projects here)

## Pages / Routes

| Page            | URL                  |
|-----------------|----------------------|
| Home            | `/`                  |
| Projects        | `/projects/`         |
| Project Details | `/projects/<id>/`    |
| About (bonus)   | `/about/`            |
| Contact (bonus) | `/contact/`          |
| Admin           | `/admin/`            |

## Screenshots

_Add screenshots of the Home page, Projects page, Project Details page, and
Admin panel here after running the project locally._

```
![Home page](screenshots/home.png)
![Projects page](screenshots/projects.png)
![Project details](screenshots/project_detail.png)
![Admin panel](screenshots/admin.png)
```

## Notes

- Update your name, profile picture, skills, and contact info in
  `portfolio/templates/portfolio/home.html`, `about.html`, and `contact.html`.
- Drop a profile photo at `portfolio/static/portfolio/img/profile.jpg`
  (a placeholder is shown automatically if it's missing).
- Add projects through the Django Admin at `/admin/` — no code changes needed.
