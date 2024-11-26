# Flask-Web-Application
This repository features a Flask-based web application designed for text sentiment analysis. The application demonstrates the integration of Python, Flask, and the TextBlob library to process user input and classify it into sentiment categories. The code structure is modular and straightforward, making it an excellent example for learning Flask development with a practical use case.

Code Highlights:
Flask Framework:

The server is set up using Flask, with routes to handle both GET and POST requests.
The root route (/) processes user input and dynamically renders results on an HTML page.
Sentiment Analysis Functionality:

A custom Python function leverages TextBlob to compute the polarity of the entered text.
Polarity values are mapped to sentiment categories:
Positive (Polarity > 0)
Negative (Polarity < 0)
Neutral (Polarity = 0)
Each sentiment category is associated with a unique color for better visualization.
HTML Integration:

The index.html file acts as the front-end interface, featuring a simple form for user input.
Results are rendered dynamically on the same page using Flask's templating engine.
Modularity:

The code separates concerns by keeping logic for analysis in helper functions and using Flask's built-in templating for rendering the interface.
User Interaction:

Users can input any text via the form.
Results, including the sentiment category and corresponding color, are displayed immediately.
