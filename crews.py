from crewai import Crew, Process
import os
import streamlit as st
import PyPDF2
import io
from agents import (legal_researcher, legal_summarizer, contract_drafter, legal_advisor, 
                   document_reviewer, case_predictor)
from tasks import (research_task, summarize_task, contract_drafting_task, legal_advice_task,
                  document_review_task, case_prediction_task)

os.makedirs('outputs', exist_ok=True)

st.set_page_config(
    page_title="Nyaya Mitra",
    page_icon="⚖️",
    layout="wide",
    initial_sidebar_state="expanded"
)

with st.sidebar:
    st.image("image.png")
    st.title("Indian Legal Assistant")
    st.markdown("Your comprehensive legal solution for:")
    st.markdown("- Research & Analysis")
    st.markdown("- Legal Consultation")
    st.markdown("- Document Preparation")
    st.markdown("- Case Outcome Prediction")
    
    st.markdown("---")
    st.markdown("### How to use:")
    st.markdown("1. Select a service tab")
    st.markdown("2. Enter required information")
    st.markdown("3. Submit your request")
    st.markdown("4. Download or copy results")

tab1, tab2, tab3, tab4, tab5 = st.tabs([
    "📚 Legal Research", 
    "💬 Legal Advice", 
    "📝 Contract Drafting", 
    "🔍 Document Review", 
    "⚖️ Case Prediction"
])

with tab1:
    st.header("Legal Research")
    st.markdown("*Generate a structured legal research report on your chosen topic*")
    
    research_topic = st.text_input("Enter legal topic:", "Contract Breach in Indian Law", key="research_topic")
    
    col1, col2 = st.columns([1, 3])
    with col1:
        research_button = st.button("Generate Research", key="research_button", use_container_width=True)
    
    if research_button:
        if research_topic:
            with st.spinner(f"Researching: {research_topic}"):
                try:
                    research_crew = Crew(
                        agents=[legal_researcher, legal_summarizer],
                        tasks=[research_task, summarize_task],
                        process=Process.sequential,
                        verbose=True
                    )
                    
                    result = research_crew.kickoff(inputs={"legal_topic": research_topic})
                    report_text = result if isinstance(result, str) else str(result)
                    
                    output_path = f'outputs/legal_research.md'
                    with open(output_path, 'w') as f:
                        f.write(report_text)
                    
                    st.success("Research completed successfully!")
                    st.markdown("### Generated Legal Research:")
                    
                    with st.expander("View Full Research Report", expanded=True):
                        st.markdown(report_text)
                    
                    st.download_button(
                        label="Download Research Report",
                        data=report_text,
                        file_name="Legal_Research_Report.md",
                        mime="text/markdown"
                    )
                except Exception as e:
                    st.error(f"An error occurred: {e}")
        else:
            st.warning("Please enter a legal topic.")

with tab2:
    st.header("Legal Advice")
    st.markdown("*Get personalized legal advice on your specific query*")
    
    legal_query = st.text_area("Enter your legal question:", "What rights do I have if my landlord refuses to fix maintenance issues?", key="legal_query", height=150)
    
    col1, col2 = st.columns([1, 3])
    with col1:
        advice_button = st.button("Get Legal Advice", key="advice_button", use_container_width=True)
    
    if advice_button:
        if legal_query:
            with st.spinner("Analyzing your legal query..."):
                try:
                    advice_crew = Crew(
                        agents=[legal_researcher, legal_advisor],
                        tasks=[research_task, legal_advice_task],
                        process=Process.sequential,
                        verbose=True
                    )
                    
                    result = advice_crew.kickoff(inputs={"legal_topic": legal_query})
                    advice_text = result if isinstance(result, str) else str(result)
                    
                    output_path = f'outputs/legal_advice.md'
                    with open(output_path, 'w') as f:
                        f.write(advice_text)
                    
                    st.success("Analysis completed!")
                    st.markdown("### Legal Advice:")
                    
                    with st.expander("View Complete Legal Advice", expanded=True):
                        st.markdown(advice_text)
                    
                    st.download_button(
                        label="Download Legal Advice",
                        data=advice_text,
                        file_name="Legal_Advice.md",
                        mime="text/markdown"
                    )
                except Exception as e:
                    st.error(f"An error occurred: {e}")
        else:
            st.warning("Please enter your legal question.")

with tab3:
    st.header("Contract Drafting")
    st.markdown("*Generate a customized contract based on your requirements*")
    
    col1, col2 = st.columns(2)
    with col1:
        contract_type = st.text_input("Contract type:", "Service Agreement", key="contract_type")
    
    contract_details = st.text_area("Contract details and requirements:", 
                                   "- Between a software developer and client\n- 6-month project\n- Payment structure: 30% upfront, 30% at midpoint, 40% upon completion\n- Include confidentiality and IP ownership clauses", 
                                   key="contract_details", height=150)
    
    col1, col2 = st.columns([1, 3])
    with col1:
        contract_button = st.button("Draft Contract", key="contract_button", use_container_width=True)
    
    if contract_button:
        if contract_type and contract_details:
            with st.spinner(f"Drafting {contract_type} contract..."):
                try:
                    contract_crew = Crew(
                        agents=[legal_researcher, contract_drafter],
                        tasks=[research_task, contract_drafting_task],
                        process=Process.sequential,
                        verbose=True
                    )
                    
                    contract_input = f"Contract Type: {contract_type}\nDetails: {contract_details}"
                    
                    result = contract_crew.kickoff(inputs={"legal_topic": contract_input})
                    contract_text = result if isinstance(result, str) else str(result)
                    
                    output_path = f'outputs/drafted_contract.md'
                    with open(output_path, 'w', encoding='utf-8') as f:
                        f.write(contract_text)
                    
                    st.success("Contract drafted successfully!")
                    st.markdown("### Generated Contract:")
                    
                    with st.expander("View Complete Contract", expanded=True):
                        st.markdown(contract_text)
                    
                    st.download_button(
                        label="Download Contract",
                        data=contract_text,
                        file_name=f"{contract_type.replace(' ', '_')}_Contract.md",
                        mime="text/markdown"
                    )
                except Exception as e:
                    st.error(f"An error occurred: {e}")
        else:
            st.warning("Please enter both contract type and details.")

with tab4:
    st.header("Legal Document Review")
    st.markdown("*Get a comprehensive analysis of your legal document*")
    
    col1, col2 = st.columns(2)
    with col1:
        document_type = st.selectbox(
            "Document Type", 
            ["Contract", "Agreement", "Legal Notice", "Court Filing", "Policy Document", "Other"],
            key="document_type"
        )
    
    document_description = st.text_area(
        "Document description and concerns:",
        "Employment agreement with non-compete clause. Concerned about enforceability and scope of restrictions.",
        key="document_description",
        height=150
    )
    
    st.markdown("**Upload your document (optional):**")
    uploaded_file = st.file_uploader("Choose a file", type=["txt", "pdf", "docx"], key="doc_upload")
    
    col1, col2 = st.columns([1, 3])
    with col1:
        review_button = st.button("Review Document", key="review_button", use_container_width=True)
    
    if review_button:
        if document_type and document_description:
            with st.spinner(f"Analyzing {document_type}..."):
                try:
                    review_crew = Crew(
                        agents=[legal_researcher, document_reviewer],
                        tasks=[research_task, document_review_task],
                        process=Process.sequential,
                        verbose=True
                    )
                    
                    document_input = f"Document Type: {document_type}\nDescription: {document_description}"
                    
                    if uploaded_file is not None:
                        try:
                            if uploaded_file.name.lower().endswith('.pdf'):
                                try:
                                    pdf_reader = PyPDF2.PdfReader(io.BytesIO(uploaded_file.getvalue()))
                                    file_contents = ""
                                    for page_num in range(len(pdf_reader.pages)):
                                        page = pdf_reader.pages[page_num]
                                        file_contents += page.extract_text() + "\n"
                                except Exception as pdf_error:
                                    st.error(f"Error reading PDF: {pdf_error}")
                                    file_contents = "Could not extract text from PDF."
                            
                            elif uploaded_file.name.lower().endswith('.docx'):
                                try:
                                    import docx
                                    doc = docx.Document(io.BytesIO(uploaded_file.getvalue()))
                                    file_contents = "\n".join([para.text for para in doc.paragraphs])
                                except ImportError:
                                    st.warning("DOCX support requires python-docx library.")
                                    file_contents = "DOCX text extraction not implemented. Please install python-docx."
                                except Exception as docx_error:
                                    st.error(f"Error reading DOCX: {docx_error}")
                                    file_contents = "Could not extract text from DOCX."
                            
                            else:
                                file_contents = uploaded_file.getvalue().decode("utf-8", errors="replace")
                            
                            if file_contents:
                                document_input += f"\n\nDocument Content:\n{file_contents}"
                        
                        except Exception as file_error:
                            st.error(f"Error processing file: {file_error}")
                    
                    result = review_crew.kickoff(inputs={"legal_topic": document_input})
                    review_text = result if isinstance(result, str) else str(result)
                    
                    output_path = f'outputs/document_review.md'
                    with open(output_path, 'w') as f:
                        f.write(review_text)
                    
                    st.success("Document analysis completed!")
                    st.markdown("### Document Analysis:")
                    
                    with st.expander("View Complete Analysis", expanded=True):
                        st.markdown(review_text)
                    
                    st.download_button(
                        label="Download Document Review",
                        data=review_text,
                        file_name="Document_Review.md",
                        mime="text/markdown"
                    )
                except Exception as e:
                    st.error(f"An error occurred: {e}")
        else:
            st.warning("Please provide document type and description.")

with tab5:
    st.header("Legal Case Prediction")
    st.markdown("*Predict potential outcomes of your legal case based on similar precedents*")
    
    col1, col2 = st.columns(2)
    with col1:
        case_area = st.selectbox(
            "Area of Law", 
            ["Civil", "Criminal", "Corporate", "IP", "Family", "Labor", "Tax", "Constitutional", "Other"],
            key="case_area"
        )
    
    case_details = st.text_area(
        "Case scenario details:",
        "My company is being sued for trademark infringement. We've been using our brand name for 5 years, but recently discovered a similar name was registered by another company 7 years ago in a different industry.",
        key="case_details",
        height=200
    )
    
    col1, col2 = st.columns([1, 3])
    with col1:
        prediction_button = st.button("Predict Outcome", key="prediction_button", use_container_width=True)
    
    if prediction_button:
        if case_area and case_details:
            with st.spinner(f"Analyzing {case_area} case and predicting outcomes..."):
                try:
                    prediction_crew = Crew(
                        agents=[legal_researcher, case_predictor],
                        tasks=[research_task, case_prediction_task],
                        process=Process.sequential,
                        verbose=True
                    )
                    
                    case_input = f"Area of Law: {case_area}\nCase Details: {case_details}"
                    
                    result = prediction_crew.kickoff(inputs={"legal_topic": case_input})
                    prediction_text = result if isinstance(result, str) else str(result)
                    
                    output_path = f'outputs/case_prediction.md'
                    with open(output_path, 'w') as f:
                        f.write(prediction_text)
                    
                    st.success("Case analysis completed!")
                    st.markdown("### Case Prediction Analysis:")
                    
                    with st.expander("View Complete Prediction", expanded=True):
                        st.markdown(prediction_text)
                    
                    st.download_button(
                        label="Download Case Prediction",
                        data=prediction_text,
                        file_name="Case_Prediction.md",
                        mime="text/markdown"
                    )
                except Exception as e:
                    st.error(f"An error occurred: {e}")
        else:
            st.warning("Please provide both the area of law and case details.")

def display_error_details():
    import traceback
    st.error(f"Error details: {traceback.format_exc()}")

st.markdown("---")
st.markdown(
    """
    <div style="display: flex; justify-content: space-between; align-items: center;">
        <div>
            <p style="color: #666; font-size: 0.8em;">This legal assistant is for informational purposes only and does not constitute legal advice.</p>
        </div>
        <div>
            <p style="color: #666; font-size: 0.8em;">Made with ❤️ by Atharva</p>
        </div>
    </div>
    """, 
    unsafe_allow_html=True
)