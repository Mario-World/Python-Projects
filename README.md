# Python & DSA Projects

This folder contains several Python projects and exercises, including a contact management system, a simple web server, and various Python and data structures & algorithms (DSA) practice files.

## Contents

- **contactList.py**  
  A simple contact management system.  
  - Add, search, and delete contacts.
  - Contacts are stored in `contacts.json`.
  - Usage: Run the script and follow the prompts.

- **contacts.json**  
  Stores contact data for `contactList.py`.

- **WebServer/main.py**  
  A basic HTTP web server using Python sockets.  
  - Serves `index.html` at `/` and `book.json` at `/book`.
  - Returns 404 for unknown paths.
  - Usage: Run `main.py` and visit `http://localhost:8080` in your browser.

- **WebServer/index.html**  
  The homepage served by the web server.

- **WebServer/book.json**  
  Example JSON data served at `/book`.

- **Other Python & DSA files**  
  Practice scripts for Python basics and data structures/algorithms.

## How to Run

1. **Contact List**
   - Make sure `contacts.json` exists (can be empty: `{"contacts": []}`).
   - Run:  
     ```
     python contactList.py
     ```

2. **Web Server**
   - Place `index.html` and `book.json` in the `WebServer` folder.
   - Run:  
     ```
     python WebServer/main.py
     ```
   - Open your browser at `http://localhost:8080`.

## Requirements

- Python 3.x

## Notes

- All data is stored locally in JSON files.
- The web server is for educational/demo purposes and is not secure for production use.

---

Feel free to explore and modify the scripts for learning and
