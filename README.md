# 🎧 Music Chart Application

A simple **web application** that displays a **music chart** and allows users to **search** for **songs**.

**Built** as part of a web development **learning** project.

This application **combines** the following technologies: `HTML`, `CSS`, `JS`, and `Python`.

<br>

## <span style="color: #32CD32">✔</span> Features

- **Music Chart** - View a list of top songs
- **Search Functionality** - Search for specific songs in the chart
- **Responsive Design** - Works on both desktop and mobile devices
- **Local Storage** - Saves song data in the browser's local storage

<br>

## <span style="color: #32CD32">✔</span> Installation

Clone the repository:

```bash
git clone https://github.com/Olli4ka/app_music_chart.git
cd app_music_chart
```

Create and activate a virtual environment:

```bash
python -m venv venv
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the application:

```bash
python src/main.py
```

Open your web browser and navigate to:

```
http://localhost:8080
```

<br>

## <span style="color: #32CD32">✔</span> Testing

The project includes automated tests written with pytest to verify the correct behavior of the Python HTTP server.

#### What is tested:

 - Server startup

 - Main page (/) returns HTTP 200

 - Search page (/search) returns HTTP 200

 - Non-existing routes return HTTP 404

 - Server correctly handles HTTP requests

#### Run tests:

```bash
pytest tests/test_main.py
```

All tests should pass successfully.

<br>

## <span style="color: #32CD32">✔</span> Project Structure

```
app_music_chart
├── src/
│   ├── __init__.py          # package marker
│   │   
│   ├── static/
│   │   ├── css/
│   │   │   └── styles.css   # CSS styles
│   │   ├── js/
│   │   │    └── script.js    # Client-side JavaScript
│   │   ├── images/           # image assets for the app    
│   │   │ 
│   ├── templates/
│   │   ├── index.html       # Main page with music chart
│   │   ├── search.html      # Search page
│   │   └── error.html       # Error page
│   │
│   └── main.py              # Python HTTP server
│
├── tests/
│   ├── conftest.py          # fixtures for pytest
│   └── test_main.py         # Pytest tests for the server
│
├── .gitignore
├── requirements.txt         # project dependencies
└── README.md
```

<br>

## <span style="color: #32CD32">✔</span> Usage

**Viewing the Chart:**

- The main page displays a list of top songs
- Songs are loaded from the HTML and stored in the browser's local storage

**Searching for Songs:**

- Click on "Search The Song" to navigate to the search page
- Enter a song name in the search box
- Click the "Search" button to find matching songs

<br>

## <span style="color: #32CD32">✔</span> Technologies Used

- **Backend**: `Python` (`http.server`)
- **Frontend**: `HTML5`, `CSS3`, `JavaScript`
- **Testing**: pytest
- **Storage**: Browser Local Storage

---
