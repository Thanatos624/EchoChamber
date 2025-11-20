Echo Chamber

🚧 Under active development — This project is a work-in-progress. Features and UI may change; issues and PRs are welcome.

Echo Chamber is a smart, collaborative blogging platform that leverages machine learning for personalized content recommendations and WebSocket technology for real-time user interaction. It serves as a comprehensive example of a modern, full-stack Django application.

Overview

This project demonstrates a robust architecture combining traditional web development with advanced data science and real-time features:

Smart Recommendation Engine:

Content-Based Filtering: Uses TF-IDF (Term Frequency-Inverse Document Frequency) and Cosine Similarity to recommend articles with similar text content.

Collaborative Filtering: Implements Matrix Factorization (SVD) to provide personalized "For You" recommendations based on user viewing history and "like" patterns.

Real-time Chat: Each blog post features a dedicated live chat room powered by Django Channels, Redis, and WebSockets, allowing readers to discuss content instantly.

Full-Featured Blog: Complete CRUD (Create, Read, Update, Delete) functionality for posts, including image uploads and rich text content.

User Engagement: Secure user authentication, user profiles, commenting system, and a "like" feature that feeds back into the recommendation engine.

Modern UI: A responsive, polished interface built with Bootstrap 5, featuring a dark mode toggle and a clean, professional aesthetic.

Perfect for developers, data science enthusiasts, and students looking to understand how to integrate machine learning models and real-time features into a production-ready web application.

Features

Authentication: Secure registration, login, and logout.

Smart Feed: A "For You" page with personalized article suggestions.

Interactive UI: Dark mode support, responsive design, and dynamic content loading.

Search: Full-text search capability to find relevant articles.

Media Management: Support for user-uploaded header images for blog posts.

Tech Stack

Backend: Django, Django REST Framework

Real-time: Django Channels, Daphne, Redis

Database: PostgreSQL (Production), SQLite (Development)

Machine Learning: Scikit-learn, Pandas, NumPy

Frontend: HTML5, CSS3, JavaScript, Bootstrap 5

Screenshots

<img width="565" height="565" alt="image" src="https://github.com/user-attachments/assets/be0cc55b-ceda-48f8-9c99-dd5fbb3d7228" />
<img width="627" height="491" alt="image" src="https://github.com/user-attachments/assets/742e187d-9037-440a-a54e-22523e1dff10" />


Installation

Clone the repository:

git clone [https://github.com/Thanatos624/EchoChamber.git](https://github.com/Thanatos624/EchoChamber.git)
cd EchoChamber


Create a virtual environment:

python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`


Install dependencies:

pip install -r requirements.txt


Apply migrations:

python manage.py migrate


Run the development server:

daphne -p 8000 blog_project.asgi:application
