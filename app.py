import streamlit as st

def convert_to_view_source_url(url):
    if url.startswith("http://"):
        url = url[7:]
    elif url.startswith("https://"):
        url = url[8:]
    
    return f"view-source:{url}"

def main():
    st.title("Webpage View Source Redirect")
    st.write("Enter the URL of a webpage and click the button to view its source.")

    url = st.text_input("Enter the URL")
    view_source_url = convert_to_view_source_url(url)

    if st.button("View Source"):
        st.experimental_set_query_params(url=view_source_url)
        st.experimental_rerun()

if __name__ == "__main__":
    main()
