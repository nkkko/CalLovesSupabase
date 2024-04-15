# Cal.com x Supabase ❤️

This quick project is a Flask-based web application that integrates with the Cal.com calendar service and the Supabase database platform. The application sets up a webhook endpoint to receive events from Cal.com and stores the event data in a Supabase table.

## Table of Contents

- [Features](#features)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
- [Configuration](#configuration)
- [Deployment](#deployment)
- [Contributing](#contributing)
- [License](#license)

## Features

- Receives webhook events from Cal.com
- Extracts relevant event data from the webhook payload
- Port forward your dev server using [Daytona](https://github.com/daytonaio/daytona)
- Stores the event data in a Supabase table

## Prerequisites

Before you can run this project, you'll need to have the following installed:

- [Daytona](https://github.com/daytonaio/daytona)
- Python 3.7 or later
- Flask
- Supabase Python client
- Dotenv

You'll also need to have a Supabase account and API keys.

## Installation

1. Create new workspace using Daytona, which will clone the repository:

```bash
git clone https://github.com/nkkko/callovessupabase.git
```

2. Change to the project directory:

```bash
cd callovessupabase
```

3. Set up your development workspace manually or use the provided `devcontainer.json`:

```bash
sudo apt update
sudo apt install pip
pip install supabase
pip install python-dotenv
```

Install the required dependencies:

```bash
pip install -r requirements.txt
```

4. Create a `.env` file in the project directory and add your Supabase URL and API key:

```
SUPABASE_URL=your-supabase-url
SUPABASE_KEY=your-supabase-api-key
```

## Usage

1. Start the Flask development server:

```bash
python3 listener.py
```

This will start the web server on `http://localhost:5000/`.

2. Use the `daytona` tool to forward your localhost port to be accessible publicly:

```bash
daytona forward 5000 --public
```

You will get a URL that you can paste in the Cal.com webhook Subscriber URL.

3. Configure your Cal.com webhook to send events to the generated URL. You can do this by navigating to the Cal.com dashboard, selecting your event, and configuring the webhook settings.

Whenever a webhook event is received from Cal.com, the `handle_cal_com_webhook()` function will be called, which will extract the event data and store it in the Supabase table.

## Configuration

There are no additional configuration options for this project. All the necessary configuration is done through the `.env` file, which should contain your Supabase URL and API key.

## Deployment

To deploy this application, you can use a production-ready WSGI server, such as Gunicorn or uWSGI. Here's an example of how you can use Gunicorn:

1. Install Gunicorn:

```bash
pip install gunicorn
```

2. Create a `wsgi.py` file in the project directory with the following content:

```python
from listener import app

if __name__ == "__main__":
    app.run()
```

3. Run the Gunicorn server:

```bash
gunicorn --bind 0.0.0.0:5000 wsgi:app
```

This will start the Gunicorn server and serve the Flask application on port 5000.

## Contributing

If you find any issues or have suggestions for improvements, feel free to submit a pull request or open an issue on the [GitHub repository](https://github.com/your-username/callovessupabase).

## License

This project is licensed under the [Apache](LICENSE).
