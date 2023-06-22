import requests
import streamlit as st

def main():
    st.title('Resume Search')

    skill = st.text_input("Enter a skill:")
    if st.button("Search"):
        response = requests.post("http://localhost:5000/search", data={'skill': skill})
        results = response.json()

        if results:
            st.success("Found the skill in the following files:")
            for result in results:
                st.write(result)
        else:
            st.warning("Skill not found in any files.")

if __name__ == '__main__':
    main()
