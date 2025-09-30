🚀 Django Real-Time Chat Application
A fully functional, real-time one-to-one chat application built with Django and Channels. This project demonstrates how to build a modern, interactive web application with features like user authentication, a friend request system, and live messaging powered by WebSockets.

✨ Key Features
User Authentication: Secure user registration (Signup) and login system.

Friendship System: Users can search for other users, send friend requests, and accept/decline incoming requests.

Real-Time One-to-One Chat: Once users are friends, they can engage in private, real-time conversations.

Modern UI/UX: A clean, professional, and responsive user interface with a "glassmorphism" design for the dashboard and authentication pages.

Scalable Backend: Uses Django Channels and Redis to handle persistent WebSocket connections efficiently.

🛠️ Tech Stack
Backend: Python, Django

Real-Time Communication: Django Channels, WebSockets

Message Broker / Channel Layer: Redis

Database: SQLite3 (for development)

Frontend: HTML, CSS, JavaScript

Web Server (for Channels): Daphne (ASGI)

📋 Prerequisites
Before you begin, ensure you have the following installed on your system:

Python (version 3.8 or higher)

pip (Python package installer)

Redis Server: For Windows users, the recommended way is to install it via WSL (Windows Subsystem for Linux).

⚙️ Setup and Installation
Follow these steps to get the project up and running on your local machine.

1. Clone the Repository
git clone <your-repository-url>
cd chat_web

2. Create and Activate a Virtual Environment
This keeps your project dependencies isolated.

# Create the environment
python -m venv venv

# Activate it (Windows)
.\venv\Scripts\Activate.ps1

# Activate it (macOS/Linux)
# source venv/bin/activate

3. Install Dependencies
Install all the required Python packages from the requirements.txt file.

pip install -r requirements.txt

4. Start Redis Server
The Redis server must be running in the background for the chat to work. If you are using WSL:

# Open your Ubuntu/WSL terminal and run:
sudo service redis-server start

Important: Keep this terminal window open and running.

5. Apply Database Migrations
This will set up your database schema based on the models defined in the project.

python manage.py makemigrations
python manage.py migrate

6. Run the Development Server
Now, you are ready to start the application!

python manage.py runserver

The application will be available at http://127.0.0.1:8000/.

🚀 How to Use
Create Two Users: Open two different browsers (or one normal and one incognito window).

In the first browser, go to the signup page and create a user (e.g., user1).

In the second browser, do the same and create another user (e.g., user2).

Send a Friend Request:

Logged in as user1, you will see user2 in the "Other Users" list on the dashboard.

Click the "Add Friend" button.

Accept the Friend Request:

In user2's browser, refresh the dashboard. You will see a friend request from user1.

Click the "Accept" button.

Start Chatting:

Both users will now see each other in their "My Friends" list.

Click the "Chat" button to open the private chat room and start messaging in real-time!

📂 Project Structure
chat_application/: Contains the main project settings, including settings.py and urls.py.

users/: A Django app responsible for user authentication (signup, login, logout).

chat/: The core Django app that handles the friendship system, chat views, and real-time WebSocket communication via consumers.py.

templates/: Contains all the HTML files.

static/: Contains all the CSS and static assets.

🔮 Future Scope
This project has a strong foundation that can be extended with many more features:

Group Chat: Create chat rooms with multiple users.

Multimedia Sharing: Implement functionality to send images, videos, and documents.

Advanced Messaging: Add features like typing indicators, read receipts (blue ticks), and online/offline status.

Push Notifications: Notify users of new messages even when the browser tab is not active.

Profile Customization: Allow users to set a profile picture and status message.
