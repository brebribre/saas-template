# Sellis Backend

This repository contains the backend for the Sellis project. The backend is responsible for processing the data and serving it to the frontend and Telegram.

## Features

- **Flask-based RESTful API**: Handles client requests and serves a processed data.
- **Data Processing**: Formatting order information from Ginee API and then storing it to a MongoDB database.
- **Daily Report**: Automatic report of daily sales and profit via Telegram.
- **Dynamic Cost Update**: Fetching cost information from a Google Sheets database.

## Prerequisites

Before you begin, ensure you have met the following requirements:

- Python 3.8 or higher
- `pip` for managing Python packages

## Installation

To install and set up the project locally:

1. **Clone the repository:**
   ```bash
   git clone https://github.com/brebribre/sellis-backend.git
   cd sellis-backend
   ```

2. **Activate virtual environment(optional):**
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   pip install -r requirements.txt
   ```

3. **Once installed, ensure to add the environment variables:**
   ```bash
   ATLAS_URI=mongodb+srv://<your-username>:admin@<cluster-name>.lnlrf4e.mongodb.net/?retryWrites=true&w=majority
   ```

4. **Then, you can run the Flask development server by using:**
   ```bash
   flask run
   ```
