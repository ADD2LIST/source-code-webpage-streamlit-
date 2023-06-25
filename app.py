import streamlit as st
import requests

def download_source_code(url):
    response = requests.get(url)
    if response.status_code == 200:
        content = response.text
        return content
    else:
        return None

def main():
    st.title("Webpage Source Code Downloader")
    st.write("Enter the URL of a webpage and click the button to download its source code.")

    url = st.text_input("Enter the URL")

    if st.button("Download Source Code"):
        source_code = download_source_code(url)
        if source_code is not None:
            st.code(source_code, language="html")
            st.download_button("Download", data=source_code, file_name="source_code.html", mime="text/html")
        else:
            st.write("Failed to download the source code.")

if __name__ == "__main__":
    main()

