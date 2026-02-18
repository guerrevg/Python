# Practice Programs: Web Basics (12_web)

**Total Programs:** 10 | **Easy:** 5 | **Medium:** 3 | **Hard:** 2

---

## Easy Programs (1-5)

### 001 - Hello Web with Flask
**Difficulty:** Easy  
**Description:** Create basic Flask hello world.  
**Learning:** Flask setup, routes  
**Expected:** `@app.route('/')` returns "Hello, World!"

### 002 - Dynamic Route
**Difficulty:** Easy  
**Description:** Route that accepts name parameter.  
**Learning:** Dynamic routes `<name>`  
**Expected:** `/hello/Alice` → "Hello, Alice!"

### 003 - HTML Response
**Difficulty:** Easy  
**Description:** Return HTML from route.  
**Learning:** HTML strings in responses  
**Expected:** Formatted HTML page

### 004 - Multiple Routes
**Difficulty:** Easy  
**Description:** Create app with several routes.  
**Learning:** Multiple `@app.route` decorators  
**Expected:** `/`, `/about`, `/contact`

### 005 - URL Parameters
**Difficulty:** Easy  
**Description:** Handle query parameters.  
**Learning:** `request.args.get()`  
**Expected:** `/search?q=python` works

---

## Medium Programs (6-8)

### 006 - Simple Form Handler
**Difficulty:** Medium  
**Description:** Create and handle HTML form.  
**Learning:** GET/POST, forms  
**Expected:** Form submission works

### 007 - JSON API Endpoint
**Difficulty:** Medium  
**Description:** Create API returning JSON.  
**Learning:** `jsonify()`, API design  
**Expected:** `{"message": "Hello"}`

### 008 - Static Files Server
**Difficulty:** Medium  
**Description:** Serve CSS and images.  
**Learning:** `static` folder, templates  
**Expected:** Styled web page

---

## Hard Programs (9-10)

### 009 - REST API with CRUD
**Difficulty:** Hard  
**Description:** Full CRUD API for resources.  
**Learning:** REST principles, all methods  
**Expected:** GET, POST, PUT, DELETE work

### 010 - Web Scraper Basic
**Difficulty:** Hard  
**Description:** Scrape data from website.  
**Learning:** `requests`, `BeautifulSoup`  
**Expected:** Extracted data saved

---

## Files to Create

```
basics/12_web/
├── flask_basics/
│   ├── 01_hello_flask.py
│   ├── 02_dynamic_route.py
│   ├── 03_html_response.py
│   ├── 04_multiple_routes.py
│   └── 05_url_parameters.py
├── forms_api/
│   ├── 06_form_handler.py
│   ├── 07_json_api.py
│   └── 08_static_files.py
└── advanced/
    ├── 09_rest_api_crud.py
    └── 10_web_scraper.py
```

## Requirements

```txt
# basics/12_web/requirements.txt
flask>=2.0.0
requests>=2.28.0
beautifulsoup4>=4.11.0
```

## Example Flask App Structure

```python
from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello, World!"

@app.route('/hello/<name>')
def hello(name):
    return f"Hello, {name}!"

@app.route('/api/data')
def get_data():
    return jsonify({"key": "value"})

if __name__ == '__main__':
    app.run(debug=True)
```
