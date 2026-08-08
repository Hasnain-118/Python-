# 🚀 AI & Software Engineering Projects Portfolio

> A comprehensive collection of AI-powered applications, algorithm visualizations, and software engineering projects

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![Streamlit](https://img.shields.io/badge/Streamlit-1.28+-red.svg)
![OpenCV](https://img.shields.io/badge/OpenCV-4.8+-green.svg)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)
![Status](https://img.shields.io/badge/Status-Active-success.svg)
![PRs](https://img.shields.io/badge/PRs-Welcome-brightgreen.svg)

---

## 📖 Table of Contents

- [Overview](#-overview)
- [All Projects Summary](#-all-projects-summary)
- [Projects](#-projects)
  - [📚 Book Budget Finder](#-book-budget-finder)
  - [🌤️ Weather Dashboard](#️-weather-dashboard)
  - [✋ AI Gesture Control System](#-ai-gesture-control-system)
  - [🚗 Vehicle Monitoring System](#-vehicle-monitoring-system)
  - [🤖 Hasnain AI Chatbot](#-hasnain-ai-chatbot)
  - [🧭 Search Algorithm Visualizer](#-search-algorithm-visualizer)
  - [🗺️ Pathfinding Visualizer](#️-pathfinding-visualizer)
- [🛠️ Technologies Used](#️-technologies-used)
- [📦 Installation Guide](#-installation-guide)
- [🎯 Usage Instructions](#-usage-instructions)
- [📁 Project Structure](#-project-structure)
- [🤝 Contributing](#-contributing)
- [📄 License](#-license)
- [📧 Contact](#-contact)

---

## 📖 Overview

### About This Repository

This portfolio showcases **7 complete, production-ready projects** demonstrating proficiency in modern software engineering, artificial intelligence, and computer vision. Each project is independently functional, well-documented, and follows industry best practices.

### Developer Profile

**Muhammad Hasnain Iftikhar**
- 🎓 **Education:** Bachelor's in Software Engineering
- 🏛️ **University:** COMSATS University Islamabad, Sahiwal Campus
- 💻 **Skills:** Python, Java, C++, SQL, AI/ML, Web Development
- 🔬 **Interests:** Artificial Intelligence, Computer Vision, NLP, Algorithm Design

---

## 📊 All Projects Summary

| # | Project | Lines of Code | Files | Status | Framework |
|---|---------|--------------|-------|--------|-----------|
| 1 | 📚 Book Budget Finder | ~80 | 1 | ✅ Complete | Streamlit |
| 2 | 🌤️ Weather Dashboard | ~70 | 1 | ✅ Complete | Streamlit |
| 3 | ✋ AI Gesture Control | ~350 | 1 | ✅ Complete | OpenCV + Tkinter |
| 4 | 🚗 Vehicle Monitoring | ~250 | 2 | ✅ Complete | YOLO + OCR |
| 5 | 🤖 Hasnain AI Chatbot | ~400 | 3 | ✅ Complete | Streamlit + Groq |
| 6 | 🧭 Search Visualizer | ~350 | 1 | ✅ Complete | Jupyter Notebook |
| 7 | 🗺️ Pathfinding Visualizer | ~500 | 1 | ✅ Complete | Tkinter |

**Total:** ~2000 lines of code | 10+ files | 7 complete applications

---

## 🎯 Projects

### 📚 Book Budget Finder

**Real-time book price scraping and budget analysis tool**

[![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=flat&logo=Streamlit&logoColor=white)](https://streamlit.io)
[![BeautifulSoup](https://img.shields.io/badge/BeautifulSoup-4.12-blue)](https://www.crummy.com/software/BeautifulSoup/)

#### Description
A web application that scrapes real-time book data from an online bookstore and helps users find affordable books within their budget. Perfect for book lovers who want to maximize their purchasing power.

#### Features
- 🔄 **Real-time Web Scraping:** Fetches live data from books.toscrape.com
- 💰 **Interactive Budget Slider:** Adjust from £10 to £60 with 0.5 increments
- 📊 **Dynamic Filtering:** Instantly shows books within budget
- 🎨 **Clean UI:** Professional dark theme with responsive design
- 📈 **Statistics:** Shows total books analyzed and affordable count

#### Technical Details
```python
def scrape_books():
    url = "https://books.toscrape.com/"
    response = requests.get(url, timeout=10)
    soup = BeautifulSoup(response.text, "html.parser")
    cards = soup.find_all("article", class_="product_pod")
    
    books_list = []
    for card in cards:
        title = card.h3.a["title"]
        price_text = card.find("p", class_="price_color").text
        price = float(re.findall(r"\d+\.\d+", price_text)[0])
        books_list.append({"title": title, "price": price})
    return books_list




2. 🌤️ Weather Dashboard

A real-time weather dashboard that allows users to search for weather information by city.

✨ Features
🌍 Search weather by city
🌡️ Temperature
☁️ Weather conditions
💧 Humidity
💨 Wind speed
💡 Weather recommendations
⏱️ Real-time weather data
🛠️ Technologies
Python
Streamlit
Requests
wttr.in API
▶️ Run
streamlit run weather_dashboard.py
3. ✋ AI Gesture Control System

A computer vision application that allows users to control their computer using hand gestures through a webcam.

✨ Gesture Controls
Gesture	Action
✊ Fist	Play / Pause
☝️ 1 Finger	Volume Up
✌️ 2 Fingers	Volume Down
3 Fingers	Scroll Up
4 Fingers	Scroll Down
🖐️ 5 Fingers	Screenshot
👍 Thumb	Mute Toggle
🛠️ Technologies
Python
OpenCV
MediaPipe
PyAutoGUI
Tkinter
▶️ Run
python gesture_control.py
4. 🚗 Vehicle Monitoring System

An AI-powered traffic monitoring system for detecting vehicles, identifying vehicle colors, and recognizing license plates.

✨ Features
🚗 Vehicle detection
🤖 YOLOv8 object detection
🎨 Vehicle color detection
📝 License plate recognition
🔎 OCR using EasyOCR
📧 Email alerts for newly detected plates
🚘 Supported Vehicles
🚗 Cars
🏍️ Motorcycles
🚌 Buses
🚛 Trucks
🛠️ Technologies
Python
OpenCV
YOLOv8
Ultralytics
EasyOCR
PyTorch
▶️ Run
python vehicle_monitor.py
5. 🤖 Hasnain AI Chatbot

An AI-powered conversational chatbot built with Streamlit and the Groq API.

The chatbot includes a personal knowledge base and supports conversational interactions in English and Urdu.

✨ Features
🌍 English and Urdu support
🧠 Personal knowledge base
💾 Persistent chat history
🔄 Chat management
🔍 Search conversations
✏️ Rename chats
🗑️ Delete chats
📤 Export conversations
📄 TXT and JSON export
🧠 Supported Models
Model	Speed	Quality
llama-3.1-8b-instant	⚡ Fast	Good
gemma2-9b-instant	⚖️ Balanced	Better
llama-3.3-70b-versatile	🐢 Slower	Best
🛠️ Technologies
Python
Streamlit
Groq API
JSON
Python-dotenv
🔐 API Key

Create a .env file:

GROQ_API_KEY=your_groq_api_key
▶️ Run
streamlit run hasnain_ai.py
6. 🧭 Search Algorithm Visualizer

An interactive Jupyter Notebook for visualizing and understanding different search algorithms.

🔎 Algorithms
🔵 Breadth-First Search (BFS)
🔵 Depth-First Search (DFS)
🔵 Uniform Cost Search (UCS)
🔵 Greedy Best-First Search
🔵 A* Search
🎨 Visualization
Indicator	Meaning
🟩 Green	Start
🟥 Red	Goal
⬛ Black	Wall
🔵 Blue	Explored
🟡 Yellow	Final Path
🛠️ Technologies
Python
Jupyter Notebook
Matplotlib
NumPy
Data Structures & Algorithms
▶️ Run
jupyter notebook search_visualizer.ipynb
7. 🗺️ Pathfinding Visualizer

A Tkinter desktop application for visualizing and comparing pathfinding algorithms.

✨ Features
🖱️ Draw walls interactively
🎯 Set start and destination
🔎 Visualize pathfinding
⚡ Speed control
📊 Algorithm statistics
🔬 Algorithm comparison
🧠 Algorithms
BFS
DFS
Greedy Best-First Search
A* Search
🛠️ Technologies
Python
Tkinter
Data Structures & Algorithms
▶️ Run
python pathfinding_visualizer.py
🛠️ Technologies Used
Category	Technologies
Programming	Python
Web Development	Streamlit
Web Scraping	BeautifulSoup, Requests
Computer Vision	OpenCV, MediaPipe
Object Detection	YOLOv8, Ultralytics
OCR	EasyOCR
AI / LLM	Groq API
Machine Learning	PyTorch
Data Processing	NumPy, Pandas
Visualization	Matplotlib
GUI	Tkinter
Automation	PyAutoGUI
Notebook	Jupyter
Data Format	JSON
📦 Installation
1. Clone the Repository
git clone https://github.com/Hasnain-118/Python-.git
cd Python-
2. Create Virtual Environment
Windows
python -m venv venv
venv\Scripts\activate
Linux / macOS
python3 -m venv venv
source venv/bin/activate
3. Install Dependencies
pip install -r requirements.txt
📋 Requirements

The main dependencies used across the projects are:

streamlit
beautifulsoup4
requests
opencv-python
mediapipe
pyautogui
ultralytics
easyocr
torch
numpy
matplotlib
pandas
groq
python-dotenv
jupyter

You can install them manually with:

pip install streamlit beautifulsoup4 requests opencv-python mediapipe pyautogui ultralytics easyocr torch numpy matplotlib pandas groq python-dotenv jupyter
🔐 Environment Variables

Some projects require API credentials.

Create a .env file where required:

GROQ_API_KEY=your_groq_api_key

⚠️ Never upload API keys, passwords, .env files, or other sensitive credentials to GitHub.

▶️ Project Commands
#	Project	Command
1	📖 Book Budget Finder	streamlit run book_budget_finder.py
2	🌤️ Weather Dashboard	streamlit run weather_dashboard.py
3	✋ Gesture Control	python gesture_control.py
4	🚗 Vehicle Monitoring	python vehicle_monitor.py
5	🤖 Hasnain AI	streamlit run hasnain_ai.py
6	🧭 Search Visualizer	jupyter notebook search_visualizer.ipynb
7	🗺️ Pathfinding Visualizer	python pathfinding_visualizer.py
📁 Project Structure
Python-/
│
├── book_budget_finder/
│   └── book_budget_finder.py
│
├── weather_dashboard/
│   └── weather_dashboard.py
│
├── gesture_control/
│   └── gesture_control.py
│
├── vehicle_monitor/
│   ├── vehicle_monitor.py
│   └── Traffic.mp4
│
├── hasnain_ai/
│   ├── hasnain_ai.py
│   ├── Hasnain.json
│   └── chat_histories/
│
├── search_visualizer/
│   └── search_visualizer.ipynb
│
├── pathfinding_visualizer/
│   └── pathfinding_visualizer.py
│
├── requirements.txt
└── README.md
🎯 Skills Demonstrated
🐍 Python Programming
🧱 Object-Oriented Programming
🌐 Web Scraping
🌐 Web Application Development
🤖 Artificial Intelligence
👁️ Computer Vision
✋ Gesture Recognition
🚗 Object Detection
🔎 Optical Character Recognition
🧠 LLM Integration
💬 Chatbot Development
🧮 Data Structures & Algorithms
🗺️ Pathfinding Algorithms
📊 Data Visualization
🖥️ Desktop GUI Development
🔌 API Integration
📂 JSON Handling
⚙️ Automation
📈 Learning Journey

These projects represent a practical learning journey from basic programming concepts toward more advanced software engineering and AI applications.

Python Programming
        ↓
Web Scraping
        ↓
Web Applications
        ↓
API Integration
        ↓
Computer Vision
        ↓
Artificial Intelligence
        ↓
LLM / Chatbot Development
        ↓
Data Structures & Algorithms
        ↓
Algorithm Visualization
🚀 Future Improvements
 Add more AI-powered projects
 Improve UI/UX across applications
 Add automated testing
 Improve error handling
 Deploy more applications online
 Add database integration
 Add authentication
 Add project screenshots
 Add live demos
 Add CI/CD workflows
 Dockerize selected projects
👨‍💻 Developer

Muhammad Hasnain Iftikhar

🎓 Bachelor's in Software Engineering
🏫 COMSATS University Islamabad, Sahiwal Campus

📧 University: fa24-bse-118@students.cuisahiwal.edu.pk
📧 Personal: mhasnain48776246@gmail.com

📄 License

This repository is licensed under the MIT License.

See the LICENSE file for more information.

⭐ Support

If you find these projects useful or interesting, consider giving the repository a ⭐ on GitHub.

© 2026 Muhammad Hasnain Iftikhar | Python Projects Portfolio
