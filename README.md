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
