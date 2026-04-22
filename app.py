import streamlit as st
from utils import get_news, display_news, CATEGORIES

st.set_page_config(
    page_title="News App - NewsAPI"
)
st.title("LATEST NEWS APP - NEWSAPI")
st.caption("GET THE LATEST NEWS HEADLINES FROM THE UNITED STATES ACROSS VARIOUS FIELDS")
st.divider()

for category in CATEGORIES:
    try:
        newses = get_news(category)
    except Exception as e:
        st.error(str(e))
    else:
        st.markdown("")
        st.subheader(f"{category.upper()} SPECIFIC NEWS")
        st.markdown("")

        for news in newses[:2]:
            display_news(news)
                
        with st.expander(f"__EXPLORE MORE {category.upper()} NEWS__"):
            for news in newses[2:]:
                display_news(news)
        st.divider()

st.caption("MADE BY TANISHK - A STUDENT AND A PROGRAMMER")