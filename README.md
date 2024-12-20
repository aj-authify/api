# Authify API

Authify API provides a simple, secure way to manage phone number-based authentication for websites. It supports generating and verifying TPO (Temporary Passcode) codes for user authentication.

## Overview

Authify API offers two key endpoints for managing authentication:
1. **POST**: Generate a TPO code for a specific phone number and website.
2. **POST**: Verify the TPO code to validate user login.

This API is built with **FastAPI** for quick and scalable development, and uses **MongoDB** for secure data storage.

## Endpoints

### `POST /tpo/generate`
```
https://api-hj87.onrender.com/tpo/generate
```

Generate a TPO code for a phone number and website.

#### Request
- **Body**: A JSON object containing the phone number and website.
    ```json
    {
        "phone_number": "user-phone-number",
        "website": "website-url"
    }
    ```

---

### `POST /tpo/verify`
```
https://api-hj87.onrender.com/tpo/verify
```
Verify the TPO code for a phone number and website.

#### Request
- **Body**: A JSON object containing the phone number, website, and TPO code.
    ```json
    {
        "phone_number": "user-phone-number",
        "website": "website-url",
        "tpo": "123456"
    }
    ```

---

## Features
- **Generate TPO Code**: Authify creates a temporary passcode tied to a phone number and website.
- **Verify TPO Code**: Authify ensures the validity of the TPO code for secure user authentication.
- **Validation**: Input validation for phone numbers and websites.
- **Secure Storage**: MongoDB is used for secure and reliable data handling.

---
