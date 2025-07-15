Python backend + Flask + SQLAlchemy for your 2nd microservice

✅ Learn Python backend development
✅ Use Flask + SQLAlchemy for your 2nd microservice
✅ Connect it to PostgreSQL
✅ Prepare for microservices working side-by-side
Let’s call this microservice: vehicle-service

🚀 VEHICLE-SERVICE: Python + Flask + SQLAlchemy

🧱 1. Folder Structure
Create a new folder inside your exploresl project:
```
exploresl/
├── user-service/          # Node.js microservice ✅
└── vehicle-service/       # Python microservice (new) 🚧
```
⚙️ 2. Setup Python Environment
let’s get your Python environment fully configured on Windows so you can run vehicle-service.

✅ Step-by-Step: Set Up Python on Windows

🔹 1. 📥 Download & Install Python (latest stable)

	• Visit: https://www.python.org/downloads/windows/
	• Click “Download Python 3.x.x” (64-bit)
	• Run the installer with the following settings:
 
✅ Important: On the installer screen:

	• ☑️ Check “Add Python to PATH”
	• 📌 Click “Customize installation”
	• Leave all defaults → then click Next
	• ☑️ On next screen, enable:
		○ “Install for all users”
		○ “Add Python to environment variables”
  
✅ Then click Install.

🔹 2. 🔁 Restart Terminal
After installation:

	• Close Command Prompt / PowerShell / VS Code
	• Reopen new terminal window (important for PATH changes)
 
Then test:
```
python --version
pip --version
You should see something like:
Python 3.12.x
pip 23.x.x
```
🔹 3. 🛠 Create Virtual Environment
```
cd exploresl
mkdir vehicle-service
cd vehicle-service
python -m venv venv
```
🔹 4. ✅ Activate Virtual Environment
```
venv\Scripts\activate
```
You should now see (venv) in your terminal prompt.

🔹 5. 📦 Install Required Packages
```
pip install flask flask_sqlalchemy psycopg2-binary
pip freeze > requirements.txt
```
✅ Now you're ready to begin development of the Python Flask microservice.

✅ Confirm All Works:
```
python -m flask --version
```
You should see something like:
```
Python 3.12.x
Flask 3.x.x
```
Navigate to the new folder:
```
cd exploresl
mkdir vehicle-service
cd vehicle-service
```
Create virtual environment:
```
python -m venv venv
source venv/bin/activate      # macOS/Linux
venv\Scripts\activate         # Windows
```
Install required packages:
```
pip install flask flask_sqlalchemy psycopg2-binary
```
Freeze dependencies:
```
pip freeze > requirements.txt
```
📄 3. Basic Files Structure
```
vehicle-service/
├── app.py
├── models.py
├── config.py
└── requirements.txt
```

🧠 4. Define Database Config (config.py)
```
import os
DB_USER = os.getenv("DB_USER", "postgres")
DB_PASS = os.getenv("DB_PASS", "1212")
DB_HOST = os.getenv("DB_HOST", "localhost")
DB_NAME = os.getenv("DB_NAME", "exploresl")
SQLALCHEMY_DATABASE_URI = f"postgresql://{DB_USER}:{DB_PASS}@{DB_HOST}:5432/{DB_NAME}"
SQLALCHEMY_TRACK_MODIFICATIONS = False
```
🚗 5. Define Vehicle Model (models.py)

```
from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()
class Vehicle(db.Model):
    __tablename__ = 'vehicles'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    type = db.Column(db.String(50))  # e.g., car, tuk, van
    area = db.Column(db.String(100)) # e.g., Ahangama, Galle
    price_per_day = db.Column(db.Float, nullable=False)
    contact = db.Column(db.String(100), nullable=False)
```
🚀 6. Create Flask App (app.py)
```
from flask import Flask, jsonify
from models import db, Vehicle
import config
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = config.SQLALCHEMY_DATABASE_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = config.SQLALCHEMY_TRACK_MODIFICATIONS
db.init_app(app)
@app.route('/')
def index():
    return jsonify({"message": "Vehicle Service Running ✅"})
@app.route('/vehicles')
def get_vehicles():
    vehicles = Vehicle.query.all()
    return jsonify([{
        "id": v.id,
        "title": v.title,
        "type": v.type,
        "area": v.area,
        "price_per_day": v.price_per_day,
        "contact": v.contact
    } for v in vehicles])
if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
```
🧪 7. Test Locally
Make sure PostgreSQL is running, then:
python app.py
Visit:
```
	• http://localhost:5000/ → "Vehicle Service Running ✅"
	• http://localhost:5000/vehicles → (empty list or data)
```
🐙 8. Push to GitHub
Initialize repo:
```
git init
git add .
git commit -m "Initial commit - Vehicle service using Flask"
git remote add origin https://github.com/your-username/vehicle-service.git
git push -u origin main
```

You're about to:
  - ✅ Learn Python backend development
  - ✅ Use Flask + SQLAlchemy for your 2nd microservice
  - ✅ Connect it to PostgreSQL
  - ✅ Prepare for microservices working side-by-side
Let’s call this microservice: vehicle-service

🚀 VEHICLE-SERVICE: Python + Flask + SQLAlchemy

🧱 1. Folder Structure
Create a new folder inside your exploresl project:
```
exploresl/
├── user-service/          # Node.js microservice ✅
└── vehicle-service/       # Python microservice (new) 🚧
```
⚙️ 2. Setup Python Environment
Navigate to the new folder:
```
cd exploresl
mkdir vehicle-service
cd vehicle-service
Create virtual environment:
python -m venv venv
source venv/bin/activate      # macOS/Linux
venv\Scripts\activate         # Windows
Install required packages:
pip install flask flask_sqlalchemy psycopg2-binary
Freeze dependencies:
pip freeze > requirements.txt
```
📄 3. Basic Files Structure
```
vehicle-service/
├── app.py
├── models.py
├── config.py
└── requirements.txt
```

🧠 4. Define Database Config (config.py)
```
import os
DB_USER = os.getenv("DB_USER", "postgres")
DB_PASS = os.getenv("DB_PASS", "1212")
DB_HOST = os.getenv("DB_HOST", "localhost")
DB_NAME = os.getenv("DB_NAME", "exploresl")
SQLALCHEMY_DATABASE_URI = f"postgresql://{DB_USER}:{DB_PASS}@{DB_HOST}:5432/{DB_NAME}"
SQLALCHEMY_TRACK_MODIFICATIONS = False
```
🚗 5. Define Vehicle Model (models.py)
```
from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()
class Vehicle(db.Model):
    __tablename__ = 'vehicles'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    type = db.Column(db.String(50))  # e.g., car, tuk, van
    area = db.Column(db.String(100)) # e.g., Ahangama, Galle
    price_per_day = db.Column(db.Float, nullable=False)
    contact = db.Column(db.String(100), nullable=False)
```
🚀 6. Create Flask App (app.py)
```
from flask import Flask, jsonify
from models import db, Vehicle
import config
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = config.SQLALCHEMY_DATABASE_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = config.SQLALCHEMY_TRACK_MODIFICATIONS
db.init_app(app)
@app.route('/')
def index():
    return jsonify({"message": "Vehicle Service Running ✅"})
@app.route('/vehicles')
def get_vehicles():
    vehicles = Vehicle.query.all()
    return jsonify([{
        "id": v.id,
        "title": v.title,
        "type": v.type,
        "area": v.area,
        "price_per_day": v.price_per_day,
        "contact": v.contact
    } for v in vehicles])
if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
```
🧪 7. Test Locally
Make sure PostgreSQL is running, then:
```
python app.py
```
Visit:

	• http://localhost:5000/ → "Vehicle Service Running ✅"
	• http://localhost:5000/vehicles → (empty list or data)


PART 2: Dockerize with Flask + PostgreSQL                

🐳 VEHICLE-SERVICE — PART 2: Dockerize with Flask + PostgreSQL

🛠 Step-by-Step: Install Docker on Windows

✅ Step 1: Download Docker Desktop
Go to:

👉 https://www.docker.com/products/docker-desktop/
Click Download for Windows (Intel/AMD).

✅ Step 2: Install Docker Desktop
  1. Run the installer
  2. On the setup screen:
      - ○ ☑ Enable WSL 2 (recommended)
      - ○ ☑ Add Docker to PATH (should be checked by default)
	3. Let it complete and reboot if asked

✅ Step 3: Start Docker
After install:
	• Open Docker Desktop from the Start menu
	• Wait until it says: ✅ "Docker is running"

✅ Step 4: Verify Docker in Terminal
Open new Command Prompt or PowerShell and run:
```
docker --version
```
You should see something like:
Docker version 25.x.x, build abc123

🧠 Optional: Enable WSL 2 Backend
If Docker Desktop prompts you to install WSL 2, follow the prompt or:
	• Download WSL 2 Update
	• Run this in terminal:
 ```
wsl --install
```
✅ This gives you faster performance and better compatibility.

---
Build & Run Docker Container

✅ Step 1: Create a Dockerfile
In the root of vehicle-service/, create a file named Dockerfile (no extension):
```
# Dockerfile
# Base image
FROM python:3.12-slim
# Set the working directory
WORKDIR /app
# Copy the project files to the container
COPY . .
# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt
# Expose port Flask will run on
EXPOSE 5000
# Run the Flask app
CMD ["python", "app.py"]
```
✅ Step 2: Add .dockerignore (optional but recommended)
Also in vehicle-service/, create .dockerignore:
```
venv/
__pycache__/
*.pyc
```
This tells Docker not to copy unnecessary files like virtual env and cache files into the container.

✅ Step 3: Build the Docker Image
From inside the vehicle-service/ folder:
```
docker build -t vehicle-service .
```
✅ This creates a Docker image named vehicle-service.

✅ Step 4: Run the Docker Container
Make sure your local PostgreSQL is running (exploresl DB exists).
Then run:
```
docker run -p 5000:5000 vehicle-service
```
Now open your browser:

	• http://localhost:5000 → "Vehicle Service Running ✅"
	• http://localhost:5000/vehicles

✅ Step 5: (Optional) Use Environment Variables
If you want to pass DB config dynamically:
```
docker run -p 5000:5000 
  -e DB_USER=postgres 
  -e DB_PASS=1212 
  -e DB_HOST=host.docker.internal 
  -e DB_NAME=exploresl 
  vehicle-service
  ```
ℹ️ host.docker.internal lets Docker talk to your local machine’s PostgreSQL on Windows.

✅ Step 6: Check Everything Works
You now have:
  - • 🐳 A fully Dockerized Python + Flask microservice
  - • 💾 Connected to PostgreSQL from inside Docker
  - • 🌐 Accessible on port 5000 from browser/Postman

🔍 Step-by-Step Debug: Why http://localhost:5000 Doesn’t Work

✅ 1. Confirm Docker Container is Running
Run this in terminal:
```
docker ps
Do you see something like:
CONTAINER ID   IMAGE             PORTS                    NAMES
abc123         vehicle-service   0.0.0.0:5000->5000/tcp   ...
```
If not: the container may have exited due to a crash.
Use:
```
docker logs <container-id>
```
✅ 2. Fix Flask to Listen on All Interfaces
Inside app.py, update the bottom section:
🔁 Change this:
```
app.run(debug=True)
```
✅ To this:
```
app.run(host='0.0.0.0', port=5000, debug=True)
```
Why?
host='0.0.0.0' makes Flask listen to traffic coming from outside the container, including from your browser.

✅ 3. Rebuild Docker Image
After updating app.py, run:
```
docker build -t vehicle-service .
```
✅ 4. Run Container Again
```
docker run -p 5000:5000 
  -e DB_USER=postgres 
  -e DB_PASS=1212
  -e DB_HOST=host.docker.internal 
  -e DB_NAME=exploresl 
  vehicle-service
```
Now open:
	• http://localhost:5000
	• http://localhost:5000/vehicles

PART 3: Push Dockerized Vehicle Service to GitHub

vehicle-service Flask microservice is now:
 - ✅ Dockerized
 - ✅ Connected to PostgreSQL
 - ✅ Running inside a container
 - ✅ Accessible from your browser
 - ✅ Returning data from /vehicles route

🚀 What's Next?
Now let’s do:
✅ PART 3: Push Dockerized Vehicle Service to GitHub
  1. .gitignore setup
  2. Commit and push to GitHub
  3. GitHub Actions (CI) for Python
  4. Optionally prepare for docker-compose later

✅ Step 1: Create .gitignore (in vehicle-service/)
```
# .gitignore
venv/
__pycache__/
*.pyc
.env
*.db
.DS_Store
*.log
```
✅ Step 2: Initialize Git (if not already)
```
cd vehicle-service
git init
```
✅ Step 3: Stage and Commit
```
git add .
git commit -m "Initial commit: Dockerized Flask vehicle service"
```
✅ Step 4: Create GitHub Repo
Go to https://github.com/new
	• Repo name: vehicle-service
	• Keep it public (or private if you prefer)
	• Do not initialize with README
Copy the remote URL they give (e.g. https://github.com/yourname/vehicle-service.git)

✅ Step 5: Push to GitHub
```
git remote add origin https://github.com/yourname/vehicle-service.git
git branch -M main
git push -u origin main

```






