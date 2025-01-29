# HNGIntern - Stage 0 - MyInfo

This repository contains the project for the HNG Internship Stage 0. The primary focus of this project is to build and demonstrate a simple Python-based web application using the Django framework.

## Table of Contents
- [Introduction](#introduction)
- [Features](#features)
- [Installation](#installation)
- [Setup](#setup)
- [Usage](#usage)
- [Methods](#methods)
- [Contributing](#contributing)
- [License](#license)

## Introduction

This project is part of the [HNG Internship program](https://hng.tech/hire/python-developers) stage 0. It is designed to help interns understand the basics of web development using Python and Django. The application showcases a public API that retrieves basic information.

## Features

- Django-based web application
- REST API support
- Cross-Origin Resource Sharing (CORS) configured
- Markdown support

## Installation

To install the necessary dependencies for this project, follow the steps below:

1. Clone the repository:
    ```bash
    git clone https://github.com/Tnkma/HNGIntern.git
    cd HNGIntern/stage0/MyInfo
    ```

2. Create a virtual environment:
    ```bash
    python -m venv env
    source env/bin/activate   # On Windows use `env\Scripts\activate`
    ```

3. Install the dependencies:
    ```bash
    pip install -r requirements.txt
    ```

## Setup

To run the project, follow these steps:

1. Run the development server:
    ```bash
    python manage.py runserver
    ```

2. Open your browser and navigate to `http://127.0.0.1:8000/` to access the application or send a GET request to the endpoint using Postman.

## Methods

The primary methods and functionalities implemented in the project include:

- **User Authentication**: Methods for registering, logging in, and managing user sessions.
- **API Endpoints**: REST API endpoints for CRUD operations.
- **CORS Handling**: Configuration to handle cross-origin requests.
- **Markdown Rendering**: Support for rendering Markdown content.

### API View: Info

- **Endpoint**: `/api/info/`
- **Method**: `GET`
- **Description**: This endpoint returns hardcoded information about the user, including email, current datetime, and GitHub URL.

## Contributing

If you would like to contribute to this project, feel free to fork the repository, make changes, and submit a pull request. We welcome improvements and suggestions!

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
