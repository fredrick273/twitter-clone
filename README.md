
# Twitter Clone

Twitter Clone is a social media web application developed using Django. It allows users to create profiles, post tweets, follow other users, and engage with tweets through likes and comments.

## Features

- **User Authentication**: Users can create accounts, log in, and log out. User authentication is handled securely using Django's built-in authentication system.

- **Profiles**: Each user has a profile page displaying their bio, profile picture, number of tweets, followers, and following. Users can edit their profiles.

- **Tweets**: Users can create tweets, which can include text and optional images. Tweets are displayed on the home page and on user profiles.

- **Likes**: Users can like tweets, and the number of likes is displayed on each tweet.

- **Comments**: Users can comment on tweets, and the comments are displayed below each tweet.

- **Followers/Following**: Users can follow and unfollow other users. The follower/following counts are displayed on user profiles.

## Project Structure

The project is structured as follows:

- `twitter/`: This directory contains the main Django application for the Twitter clone.
  - `models.py`: Defines the database models for profiles, tweets, comments, and followers.
  - `forms.py`: Contains the forms for user registration, login, and profile editing.
  - `views.py`: Defines the views for various functionalities, such as creating tweets, following users, and user profiles.
  - `urls.py`: Handles URL routing and mapping to views.
  - `templates/twitter/`: Contains HTML templates for the application's pages.

- `media/`: Stores user profile pictures and tweet images.

- `static/`: Contains static files, including CSS stylesheets.

- `templates/`: Contains base HTML templates for the project layout.

## Getting Started

To run this Twitter clone on your local machine, follow these steps:

1. Clone the repository to your local machine:

   ```bash
   git clone <repository-url>
   ```

2. Navigate to the project directory:

   ```bash
   cd <project-directory>
   ```

3. Create a virtual environment (recommended) and install the project dependencies:

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   pip install -r requirements.txt
   ```

4. Apply the database migrations:

   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

5. Create a superuser account for admin access:

   ```bash
   python manage.py createsuperuser
   ```

6. Start the development server:

   ```bash
   python manage.py runserver
   ```

7. Access the application in your web browser at `http://localhost:8000/`.

8. Log in with your superuser account to access the admin panel at `http://localhost:8000/admin/`.

## Usage

- **Home Page**: After logging in, you'll be redirected to the home page where you can view tweets from users you follow and create your own tweets.

- **User Profiles**: Click on a username to view their profile, including tweets, followers, and following.

- **Tweet Details**: Click on a tweet to view its details, including likes and comments.

- **Edit Profile**: On your profile page, you can edit your bio, date of birth, and profile picture.

- **Follow/Unfollow**: On user profiles, you can choose to follow or unfollow a user.

- **Log Out**: Log out from the top right menu.

## Contributing

Contributions to the Twitter Clone project are welcome! If you find a bug, have a suggestion, or want to add a new feature, please feel free to open an issue or submit a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Disclaimer

This project is for educational and demonstrational purposes only. Use it at your own risk. The author is not responsible for any misuse or damages caused by this application.

Happy tweeting!
