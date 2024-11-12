# Project Sentiments

This project provides a web application that performs sentiment analysis on user-provided text. The application is built using Flask and Docker, and utilizes a sentiment analysis module implemented with the `transformers` library.

## Project Structure

\```plaintext

Project Sentiments/
├── app/
│   ├── templates/
│   │   └── index.html
│   ├── static/
│   │   ├── mywebscript.js
│   │   └── styles.css
│   ├── requirements.txt    # Requirements for the application container
├── SentimentAnalysis/
│   ├── Dockerfile          # Dockerfile for the sentiment analysis container
│   ├── requirements.txt    # Requirements for the sentiment analysis container
│   ├── sentiment_analysis.py
│   ├── __init__.py
├── Dockerfile              # Dockerfile for the application container (root)
├── docker-compose.yml      # Docker Compose file for managing both containers
├── requirements.txt        # Root requirements file (if needed)
├── server.py               # Main server script for the Flask application (root)
└── README.md
\```

## Setup Instructions

### Prerequisites

Ensure you have the following installed:
- Docker
- Docker Compose

### Build and Run the Containers

1. **Clone the repository:**

    \```bash
    git clone https://github.com/your-username/project-sentiments.git
    cd project-sentiments
    \```

2. **Build and run the Docker containers:**

    \```bash
    docker-compose up --build
    \```

3. **Access the application:**

    Open your web browser and navigate to `http://localhost:5000`.

### Project Details

#### Application Service

- **Directory:** `app/`
- **Main Script:** `server.py`
- **Description:** This service hosts the Flask web application. It renders the main page and handles user input for sentiment analysis.

#### Sentiment Analysis Service

- **Directory:** `SentimentAnalysis/`
- **Main Script:** `sentiment_analysis.py`
- **Description:** This service handles sentiment analysis using the `transformers` library. It provides an API endpoint for the application service to call.

### Example Usage

1. **Navigate to `http://localhost:5000` in your web browser.**
2. **Enter the text you want to analyze in the provided input field.**
3. **Submit the form to receive the sentiment analysis result.**

### Development

#### Installing Dependencies

To install dependencies for local development, use the following commands:

- **For the Flask application:**

    \```bash
    pip install -r app/requirements.txt
    \```

- **For the sentiment analysis module:**

    \```bash
    pip install -r SentimentAnalysis/requirements.txt
    \```

#### Running the Application Locally

1. **Start the sentiment analysis service:**

    \```bash
    cd SentimentAnalysis
    python sentiment_analysis.py
    \```

2. **Start the Flask application:**

    \```bash
    cd ../app
    python server.py
    \```

### Contributing

Contributions are welcome! Please fork the repository and submit a pull request with your changes.

### License

This project is licensed under the MIT License. See the `LICENSE` file for details.

### Contact

For any questions or issues, please contact [your-email@example.com].

## Setup Instructions

### Prerequisites

Ensure you have the following installed:
- Docker
- Docker Compose

### Build and Run the Containers

1. **Clone the repository:**

    ```bash
    git clone https://github.com/your-username/project-sentiments.git
    cd project-sentiments
    ```

2. **Build and run the Docker containers:**

    ```bash
    docker-compose up --build
    ```

3. **Access the application:**

    Open your web browser and navigate to `http://localhost:5000`.

### Project Details

#### Application Service

- **Directory:** `app/`
- **Main Script:** `server.py`
- **Description:** This service hosts the Flask web application. It renders the main page and handles user input for sentiment analysis.

#### Sentiment Analysis Service

- **Directory:** `SentimentAnalysis/`
- **Main Script:** `sentiment_analysis.py`
- **Description:** This service handles sentiment analysis using the `transformers` library. It provides an API endpoint for the application service to call.

### Example Usage

1. **Navigate to `http://localhost:5000` in your web browser.**
2. **Enter the text you want to analyze in the provided input field.**
3. **Submit the form to receive the sentiment analysis result.**

### Development

#### Installing Dependencies

To install dependencies for local development, use the following commands:

- **For the Flask application:**

    ```bash
    pip install -r app/requirements.txt
    ```

- **For the sentiment analysis module:**

    ```bash
    pip install -r SentimentAnalysis/requirements.txt
    ```

#### Running the Application Locally

1. **Start the sentiment analysis service:**

    ```bash
    cd SentimentAnalysis
    python sentiment_analysis.py
    ```

2. **Start the Flask application:**

    ```bash
    cd ../app
    python server.py
    ```

### Contributing

Contributions are welcome! Please fork the repository and submit a pull request with your changes.

### License

This project is licensed under the MIT License. See the `LICENSE` file for details.

### Contact

For any questions or issues, please contact me.

