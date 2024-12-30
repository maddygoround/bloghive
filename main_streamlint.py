import streamlit as st
import warnings
from datetime import datetime
from crew import BlogPostWriter
import random
import string

# Suppress specific warnings
warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")

# Helper function to validate date format


def validate_date(date_str):
    try:
        datetime.strptime(date_str, "%Y-%m-%d")
        return True
    except ValueError:
        return False


# Initialize session states
if 'url_keys' not in st.session_state:
    st.session_state.url_keys = []


def generate_key():
    """Generate a unique key for text input"""
    return f"url_{random.choice(string.ascii_uppercase)}{str(random.randint(0, 999999))}"


def add_new_row():
    """Add a new URL input field with a unique key"""
    new_key = generate_key()
    st.session_state.url_keys.append(new_key)


def collect_urls():
    """Collect all non-empty URLs from the text inputs"""
    urls = []
    for key in st.session_state.url_keys:
        if key in st.session_state and st.session_state[key].strip():
            urls.append(st.session_state[key].strip())
    return urls


def main():
    # Configure page layout
    st.set_page_config(
        page_title="Write a blog post",
        page_icon="✈️",
        layout="wide",
        initial_sidebar_state="expanded",
    )

    # Add title with emoji and styling
    st.markdown(
        """
        <style>
        .main-title {
            text-align: center;
            font-size: 3rem;
            color: #0078D7;
        }
        .description {
            text-align: center;
            color: #6c757d;
            margin-top: -15px;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )
    st.markdown(
        '<h1 class="main-title">🌍✈️ Write a blog post</h1>',
        unsafe_allow_html=True,
    )
    st.markdown(
        '<p class="description">Use this tool to write a blog post on a given topic. Enter the topic and provide additional URLs for reference to generate a comprehensive blog post!</p>',
        unsafe_allow_html=True,
    )

    # Create layout with columns
    input_col, result_col = st.columns([1, 2])

    # Input fields in the left column
    with input_col:
        st.subheader("Search Inputs")
        topic = st.text_input(
            "Topic",
            value="Burnout",
            help="Enter the topic for which you want to write a blog.",
        )

        # Add URL input fields
        st.subheader("Additional URLs")

        # Button to add new URL input
        if st.button("Add new URL"):
            add_new_row()

        # Display all URL inputs
        for key in st.session_state.url_keys:
            url_value = st.text_input("Enter URL for research", key=key)

        # Display current URLs for debugging
        st.write("Current URLs added:", len(st.session_state.url_keys))

        # Submit button
        if st.button("🔍 Write a blog"):
            # Collect all URLs
            additional_urls = collect_urls()

            # Prepare inputs
            inputs = {
                "topic": topic,
                "additional_urls": additional_urls
            }

            try:
                # Run the crew process
                result = BlogPostWriter().crew().kickoff(inputs=inputs)

                # Display the result on the right
                with result_col:
                    st.success("Blog post generated successfully!")
                    st.markdown(result, unsafe_allow_html=True)
            except Exception as e:
                with result_col:
                    st.error(f"An error occurred: {str(e)}")

    # Add background styling
    st.markdown(
        """
        <style>
        body {
            background-color: var(--background-color);
            color: var(--text-color);
        }

        .stButton>button {
            background-color: var(--button-background);
            color: var(--button-text-color);
        }

        .stMarkdown {
            color: var(--markdown-text-color);
        }
        </style>
        """,
        unsafe_allow_html=True,
    )

    # Debug information
    with st.expander("Debug Information"):
        st.write("Session State URL Keys:", st.session_state.url_keys)
        st.write("Collected URLs:", collect_urls())


# Run the app
if __name__ == "__main__":
    main()
