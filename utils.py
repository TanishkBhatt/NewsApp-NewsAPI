import requests
import streamlit as st
from datetime import datetime

CATEGORIES = ["business", "entertainment", "sports", "science", "technology", "general", "health"]

def date_formatter(date: str) -> str:
    return datetime.strftime(
        datetime.strptime(
                date,
                "%Y-%m-%dT%H:%M:%SZ"
            ), 
        "%Y-%m-%d, %I: %M: %p"
        )


def get_news(category: str) -> list[dict]:
    res = requests.get(f"https://newsapi.org/v2/top-headlines?country=us&category={category}&apiKey={st.secrets.API_KEY}")

    if res.status_code == 200:
        articles = []
        data = res.json()

        for article in data["articles"]:
            df = {
                "title": article["title"],
                "source": article["source"]["name"],
                "description": article["description"],
                "content": article["content"],
                "published_at": date_formatter(article["publishedAt"]),
                "image": article["urlToImage"],
                "content_url": article["url"]
            }
            if df["description"] and df["content"]:
                articles.append(df)

        return articles
    raise Exception("FAILED TO FETCH DATA!")


def display_news(news: dict[str, str]):
    with st.container(border=True):
            st.markdown(f"#### {news["title"]}")
            col1, col2 = st.columns(2)
            with col1:
                st.caption(f"SOURCE - {news["source"].upper()}")
            with col2:
                st.caption(f"PUBLISHED AT - {news["published_at"]}")
            
            st.markdown("")
            col1, col2 = st.columns(2)
            with col1:
                st.write(news["description"])
                st.write(news["content"])
                st.link_button("__READ FULL CONTENT__", news["content_url"])
            with col2:
                if news["image"]:
                    st.image(news["image"])
                else:
                    st.warning("No IMAGE FOR THIS NEWS!")
                      
    st.markdown("")
    st.markdown("")
