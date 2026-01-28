# -*- coding: utf-8 -*-
"""
Created on Tue Jan 27 17:32:56 2026

@author: BBarsch
"""

import streamlit as st

st.write("CSS 2026")

st.title("Day 3")

st.write("Hello, Streamlit!")

st.header("select a Number")

number = st.slider("Pick a number", 1, 100)
st.write(f"You picked: {number}")

st.markdown("select a text that you can write")