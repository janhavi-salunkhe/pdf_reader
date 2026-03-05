import streamlit as st
import time

st.set_page_config(page_title="PaperBot", layout="wide")

st.title("📄 PaperBot")
st.write("Upload handwritten PDFs and ask questions from your notes.")

with st.sidebar:
    st.title("🤖 PaperBot")

    if st.button("➕ New Chat"):
        st.session_state.messages = []

    st.subheader("History")
    st.write("Chat 1")
    st.write("Chat 2")

    st.divider()

    st.write("User: krishna@gmail.com")
    st.write("Age: 20")


uploaded_files = st.file_uploader(
    "Upload Handwritten PDFs",
    type=["pdf"],
    accept_multiple_files=True
)

if uploaded_files:
    st.write("### Selected Files")

    for file in uploaded_files:
        st.write(file.name)

        

if uploaded_files:
    if st.button("Start Processing"):
        st.session_state.processing = True

        


if st.session_state.get("processing"):

    progress = st.progress(0)

    stages = [
        "Processing file...",
        "Extracting handwritten text...",
        "Processing diagrams...",
        "Saving to database...",
        "Indexing..."
    ]

    for i in range(5):
        st.write(stages[i])
        progress.progress((i+1)*20)
        time.sleep(1)

    st.success("Files processed successfully!")

    st.session_state.docs_uploaded = True



if st.session_state.get("docs_uploaded"):
    st.header("Chat with your Notes")


if "messages" not in st.session_state:
    st.session_state.messages = []
    

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])




prompt = st.chat_input("Ask something from your notes...")

if prompt:

    st.session_state.messages.append(
        {"role": "user", "content": prompt}
    )

    with st.chat_message("user"):
        st.write(prompt)
        


response = "This concept is explained in your notes on Page 3."

st.session_state.messages.append(
    {"role": "assistant", "content": response}
)

with st.chat_message("assistant"):
    st.write(response)
    

st.caption("📄 Source: Page 3, Section: Introduction")




col1, col2 = st.columns(2)

with col1:
    st.file_uploader("Upload PDFs", type=["pdf"])

with col2:
    st.write("We can process:")
    st.write("✔ Different handwriting")
    st.write("✔ Diagrams")
    st.write("✔ Tables")