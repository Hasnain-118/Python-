# 🚀 AI & Software Engineering Projects Portfolio

> A comprehensive collection of AI-powered applications, algorithm visualizations, and software engineering projects

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![Streamlit](https://img.shields.io/badge/Streamlit-1.28+-red.svg)
![OpenCV](https://img.shields.io/badge/OpenCV-4.8+-green.svg)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)
![Status](https://img.shields.io/badge/Status-Active-success.svg)

---

## 📋 Table of Contents

- [Overview](#overview)
- [Projects](#projects)
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

This portfolio showcases **7 complete projects** demonstrating proficiency in:

- 🤖 **Artificial Intelligence & Machine Learning**
- 👁️ **Computer Vision & Gesture Recognition**
- 🌐 **Web Development & Streamlit Applications**
- 📊 **Algorithm Design & Visualization**
- 🔄 **Data Processing & Automation**
- 💬 **Natural Language Processing**

**Developer:** Muhammad Hasnain Iftikhar  
**University:** COMSATS University Islamabad, Sahiwal Campus  
**Degree:** Bachelor's in Software Engineering

---

## 🎯 Projects

### 📚 Book Budget Finder
**Real-time book price scraping and budget analysis**

![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=flat&logo=Streamlit&logoColor=white)
![BeautifulSoup](https://img.shields.io/badge/BeautifulSoup-4.12-blue)

**Features:**
- 🔄 Real-time web scraping from books.toscrape.com
- 💰 Interactive budget slider (£10-£60)
- 📊 Dynamic price filtering
- 🎨 Clean, responsive UI

**How it works:**
```python
# Scrape books and filter by budget
books = scrape_books()
affordable = [b for b in books if b["price"] <= budget]
