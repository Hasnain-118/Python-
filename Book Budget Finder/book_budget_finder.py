from bs4 import BeautifulSoup
import streamlit as st
import requests
import re

def scrape_books():
    url = "https://books.toscrape.com/"
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, "html.parser")
        books_list = []
        cards = soup.find_all("article", class_="product_pod")
        for card in cards:
            title = card.h3.a["title"]
            price_text = card.find("p", class_="price_color").text
            price = float(re.findall(r"\d+\.\d+", price_text)[0])
            books_list.append({
                "title": title,
                "price": price
            })
        return books_list
    except Exception as e:
        st.error(f"Error fetching books: {e}")
        return []

st.set_page_config(page_title="Book Budget Finder", page_icon="📚")

st.title("📚 Book Budget Finder")
st.write("Scrape real-time book data and check your purchasing power.")

budget = st.slider("What is your maximum budget (£)?", 10.0, 60.0, 30.0, step=0.5)

if st.button("🔍 Fetch and Analyze Books"):
    with st.spinner("📖 Fetching books..."):
        all_books = scrape_books()
    
    if not all_books:
        st.error("❌ Could not fetch books. Please check your internet connection.")
    else:
        affordable_books = [b for b in all_books if b["price"] <= budget]
        st.divider()
        
        if affordable_books:
            st.success(f"✅ Found {len(affordable_books)} books within your £{budget} budget!")
            for book in affordable_books:
                with st.container():
                    col1, col2 = st.columns([3, 1])
                    col1.write(f"**{book['title']}**")
                    col2.write(f"£{book['price']:.2f}")
                    st.write("---")
        else:
            st.error("❌ No books found in that price range. Try increasing your budget!")
            
        st.divider()
        st.caption(f"📊 Total books analyzed: {len(all_books)}")
