import pandas as pd
import streamlit as st
from dotenv import load_dotenv

from ai_assistant import (
    answer_question,
    extract_action_items,
    summarize_document,
)
from document_processor import extract_text


load_dotenv()

st.set_page_config(
    page_title="AI Business Document Assistant",
    page_icon="??",
    layout="wide",
)

st.title("AI Business Document Assistant")
st.caption(
    "An AI-assisted workspace for business-document analysis "
    "and action-item extraction."
)

with st.sidebar:
    st.header("About")
    st.write(
        "Upload a business document to explore AI-assisted "
        "summarization, question answering, and task extraction."
    )
    st.divider()
    st.markdown("**Supported formats:** PDF, DOCX, TXT")
    st.markdown("**Core technologies:** Python, Streamlit, OpenAI API")
    st.warning(
        "Do not upload confidential, personal, or sensitive business "
        "documents to this demo without appropriate authorization."
    )

uploaded_file = st.file_uploader(
    "Upload a business document",
    type=["pdf", "docx", "txt"],
)

if uploaded_file:
    try:
        document_text = extract_text(uploaded_file)
        st.success(f"Document loaded: {uploaded_file.name}")

        with st.expander("Preview extracted text"):
            preview_length = 5_000
            st.text_area(
                "Extracted content",
                value=document_text[:preview_length],
                height=250,
                disabled=True,
            )
            if len(document_text) > preview_length:
                st.caption(
                    f"Preview limited to {preview_length:,} characters. "
                    "The analysis may use more text, subject to its input limit."
                )

        tab_summary, tab_qa, tab_actions = st.tabs(
            ["Document Summary", "Ask a Question", "Action Items"]
        )

        with tab_summary:
            st.subheader("Executive Summary")
            st.write(
                "Generate a structured overview of the document, "
                "including key topics and outstanding issues."
            )

            if st.button(
                "Generate Summary",
                key="generate_summary",
                type="primary",
            ):
                with st.spinner("Analyzing document..."):
                    try:
                        result = summarize_document(document_text)
                        st.session_state["summary_result"] = result
                    except Exception as exc:
                        st.error(f"Could not generate summary: {exc}")

            if "summary_result" in st.session_state:
                st.markdown(st.session_state["summary_result"])

        with tab_qa:
            st.subheader("Document-Based Question Answering")
            question = st.text_area(
                "Enter your question",
                placeholder=(
                    "Example: What decisions were made, "
                    "and what information is still missing?"
                ),
                height=100,
                key="document_question",
            )

            if st.button(
                "Ask AI",
                key="ask_question",
                type="primary",
            ):
                if not question.strip():
                    st.warning("Please enter a question.")
                else:
                    with st.spinner("Finding an answer..."):
                        try:
                            result = answer_question(
                                document_text,
                                question.strip(),
                            )
                            st.session_state["qa_result"] = result
                        except Exception as exc:
                            st.error(f"Could not answer the question: {exc}")

            if "qa_result" in st.session_state:
                st.markdown(st.session_state["qa_result"])

        with tab_actions:
            st.subheader("Action-Item Extraction")
            st.write(
                "Identify tasks and capture owners, deadlines, "
                "supporting evidence, and status where available."
            )

            if st.button(
                "Extract Action Items",
                key="extract_actions",
                type="primary",
            ):
                with st.spinner("Extracting action items..."):
                    try:
                        actions = extract_action_items(document_text)
                        st.session_state["action_items"] = actions
                    except Exception as exc:
                        st.error(f"Could not extract action items: {exc}")

            if "action_items" in st.session_state:
                actions = st.session_state["action_items"]

                if not actions:
                    st.info("No action items were identified.")
                else:
                    dataframe = pd.DataFrame(actions)
                    preferred_columns = [
                        "task", "owner", "deadline", "status", "evidence"
                    ]
                    dataframe = dataframe[preferred_columns]

                    st.dataframe(
                        dataframe,
                        use_container_width=True,
                        hide_index=True,
                    )

                    csv_data = dataframe.to_csv(
                        index=False
                    ).encode("utf-8-sig")

                    st.download_button(
                        label="Download Action Items as CSV",
                        data=csv_data,
                        file_name="action_items.csv",
                        mime="text/csv",
                    )

    except Exception as exc:
        st.error(f"Could not process this document: {exc}")

else:
    st.info("Upload a PDF, DOCX, or TXT document to get started.")

st.divider()
st.caption(
    "Prototype for educational and demonstration purposes. "
    "Review AI-generated outputs before using them in business decisions."
)