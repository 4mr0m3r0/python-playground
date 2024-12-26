import streamlit as st
import requests
import os
import pandas as pd
import numpy as np
from tornado.httpclient import HTTPError
import base64

github_token = os.environ['GITHUB_TOKEN']
headers = {
    'Authorization': f'Bearer {github_token}',
    'Accept': 'application/vnd.github+json'
}
def get_content_based_on_url(url: str) -> str:
    response = requests.get(url=url, headers=headers)
    try:
        if response.ok:
            return response.json()['content']
        return ""
    except HTTPError as e:
        return ""

def decode(g_content: str):
    return base64.b64decode(g_content).decode('utf-8')

@st.cache_data
def get_file_urls(url: str) -> dict:
    response = requests.get(url=url, headers=headers)
    file_urls = {}
    try:
        if response.ok:
            for item in response.json()['tree']:
                if item['type'] == 'blob':
                    file_urls[item['path']] = item['url']
        return file_urls
    except HTTPError as e:
        return file_urls

@st.fragment
def list_tree():
    l_url = st.text_input("Enter a valid API GitHub url, e.g.: https://api.github.com/repos/{github_owner}/{github_repo}/git/trees/main?recursive=true")
    btn_repo_clicked = st.button("Get URLs")
    if btn_repo_clicked:
        urls = get_file_urls(l_url)
        if urls:
            for key, value in urls.items():
                st.text(f'Path: {key}')
                st.text(f'Url: {value}')
                st.divider()

@st.fragment
def request_content():
    c_url = st.text_input("Enter a valid API GitHub url. Pick anyone from 'Listing valid urls' section.")
    btn_clicked = st.button("Read Content")
    if btn_clicked:
        content = get_content_based_on_url(c_url)
        if content:
            st.text("Loading content done!")
            st.code(decode(content))

st.title('GitHub repository reader')
st.warning("Before you run this streamlit file, you must set a GITHUB_TOKEN environment variable with your API token.")

st.write("# Requesting content")
request_content()

st.write("# Listing valid urls")
list_tree()


