# Understanding HTTP and HTTPS
# task 0
## Overview
This document provides a concise guide to HTTP and HTTPS protocols, the structure of HTTP/2 requests and responses, commonly used HTTP methods, and typical HTTP status codes. It is organized for clarity and quick reference.

---

## 1. HTTP vs HTTPS

### HTTP (HyperText Transfer Protocol)
- **Purpose**: Transfers hypertext data on the web.
- **Port**: Uses port **80**.
- **Security**: Transmits data in **plain text**, making it vulnerable to interception.
- **Ideal Use**: For non-sensitive content like blogs or open informational pages.

### HTTPS (HyperText Transfer Protocol Secure)
- **Purpose**: Secure version of HTTP using **SSL/TLS encryption**.
- **Port**: Uses port **443**.
- **Security**: Encrypts data for confidentiality, integrity, and authentication.
- **Ideal Use**: Required for sensitive data like logins, payments, and personal information.

### Comparison Table
| Feature       | HTTP         | HTTPS                  |
|---------------|--------------|------------------------|
| Security      | Not secure   | Encrypted with SSL/TLS |
| Port          | 80           | 443                    |
| Encryption    | No           | Yes                    |
| Trust         | No cert.     | Requires CA certificate|

---

## 2. HTTP/2 Request & Response Structure

### Request Components
- `:method`: e.g., GET, POST  
- `:scheme`: URL scheme (http/https)  
- `:authority`: Domain (e.g., example.com)  
- `:path`: Resource path (/index.html)  
- **Headers**: Metadata like User-Agent, Accept  
- **Body**: Payload (only for POST, PUT, etc.)

**Example Request:**
```
:method: GET
:scheme: https
:authority: www.example.com
:path: /index.html
user-agent: Mozilla/5.0
accept: text/html
```

### Response Components
- `:status`: Status code (e.g., 200, 404)  
- **Headers**: Metadata (e.g., Content-Type)  
- **Body**: HTML or other content

**Example Response:**
```
:status: 200
content-type: text/html
content-length: 1234

<html>
  <body>
    <h1>Hello, World!</h1>
  </body>
</html>
```

### HTTP/2 Key Features
- **Multiplexing**: Multiple messages in one connection  
- **Header Compression**: Reduces header size using HPACK  
- **Stream Prioritization**: Assigns priorities to resources  
- **Server Push**: Sends resources without client request

---

## 3. Common HTTP Methods

| Method   | Description                                  | Use Case                                     |
|----------|----------------------------------------------|----------------------------------------------|
| GET      | Retrieves data                               | Loading a web page or API response           |
| POST     | Sends data to server                         | Form submission, file upload                 |
| PUT      | Updates or replaces a resource               | User info update                             |
| DELETE   | Removes a resource                           | Deleting a record or file                    |
| PATCH    | Partially modifies a resource                | Changing a single profile field              |
| HEAD     | Same as GET, but only headers are returned   | Checking if resource exists                  |
| OPTIONS  | Describes communication options              | Checking supported HTTP methods              |
| CONNECT  | Creates a tunnel (used for HTTPS)            | SSL tunneling                                |
| TRACE    | Echoes request back to the sender            | Diagnostic/debugging                         |

---

## 4. Common HTTP Status Codes

| Code | Meaning                   | Description                                        | Example Scenario                              |
|------|----------------------------|----------------------------------------------------|------------------------------------------------|
| 200  | OK                         | Request succeeded                                  | Page loaded successfully                      |
| 201  | Created                    | Resource was created                               | New user registered                            |
| 204  | No Content                 | Successful request, no content returned            | Resource deleted without returning data       |
| 400  | Bad Request                | Server couldn't understand the request             | Missing required parameters                   |
| 401  | Unauthorized               | Authentication needed                              | Accessing protected content without login     |
| 403  | Forbidden                  | Server refuses to authorize                        | Unauthorized access to restricted area        |
| 404  | Not Found                  | Resource not found                                 | Page or file doesn't exist                    |
| 500  | Internal Server Error      | Generic server-side error                          | Unexpected error in application logic         |
| 502  | Bad Gateway                | Invalid response from upstream server              | Gateway timeout or misconfigured proxy        |
| 503  | Service Unavailable        | Server not ready or overloaded                     | Maintenance or heavy traffic                  |

---

## Conclusion
Understanding the differences between HTTP and HTTPS, the workings of HTTP/2, and the roles of various HTTP methods and status codes is essential for web development, cybersecurity, and API design. HTTPS should always be used where privacy, integrity, and trust are important.

