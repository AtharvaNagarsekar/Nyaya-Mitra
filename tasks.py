from crewai import Task
from agents import legal_researcher, legal_summarizer, contract_drafter, legal_advisor, document_reviewer, case_predictor

research_task = Task(
    description=(
        "Conduct thorough research on the legal topic '{legal_topic}', focusing on Indian law. "
        "This includes finding relevant legal cases, statutes, judgments, and authoritative resources. "
        "Your research should cover:\n"
        "1. Applicable statutes and legal framework\n"
        "2. Leading case laws and precedents\n"
        "3. Legal principles and interpretations\n"
        "4. Recent developments or amendments\n"
        "5. Different perspectives on contentious issues\n\n"
        "Provide proper citations and ensure that all information is accurate and up-to-date with the "
        "latest legal developments in India. Organize your findings logically and highlight key points."
    ),
    expected_output='A detailed and comprehensive research document on the legal topic, with proper citations, organized sections, and highlighted key principles.',
    agent=legal_researcher,
)
summarize_task = Task(
    description=(
        "Summarize the findings from the legal research on '{legal_topic}' in a structured, accessible format. "
        "Your summary should include:\n"
        "1. An executive summary of key points\n"
        "2. The main legal principles and provisions that apply\n"
        "3. Relevant case precedents with brief case facts and holdings\n"
        "4. Practical implications and applications\n"
        "5. Areas of legal uncertainty or ongoing developments\n\n"
        "Use clear headings, bullet points where appropriate, and plain language explanations of complex legal concepts. "
        "The summary should be well-organized, easy to navigate, and highlight the most important aspects of the research."
    ),
    expected_output='A well-structured legal research summary with clear sections, highlighted key principles, and practical insights.',
    agent=legal_summarizer,
    async_execution=False,
    output_file='legal_research_summary.md',
)

contract_drafting_task = Task(
    description=(
        "Draft a legally sound and comprehensive contract based on '{legal_topic}'. Your contract should:\n"
        "1. Begin with proper parties, recitals, and definitions sections\n"
        "2. Include all necessary clauses and provisions specific to this contract type\n"
        "3. Address the specific requirements and details provided\n"
        "4. Incorporate appropriate risk management and protection clauses\n"
        "5. Ensure compliance with Indian contract law and relevant statutes\n"
        "6. Include proper execution provisions\n\n"
        "The contract should be clear, unambiguous, and formatted professionally with numbered sections and subsections. "
        "Avoid legal jargon where possible while maintaining legal precision. The final contract should be ready for "
        "execution after appropriate review."
    ),
    expected_output="A complete, well-structured contract document with all necessary clauses, tailored to the specific requirements and compliant with Indian law.",
    agent=contract_drafter,
    async_execution=False,
    output_file="drafted_contract.md",
)

legal_advice_task = Task(
    description=(
        "Based on the legal query '{legal_topic}', provide comprehensive yet practical legal advice tailored to "
        "the specific situation. Your advice should:\n"
        "1. Analyze the legal issues presented in the query\n"
        "2. Identify the relevant laws, statutes, and precedents that apply\n"
        "3. Explain the legal rights, obligations, and potential liabilities\n"
        "4. Outline practical steps and actionable recommendations\n"
        "5. Address potential risks and alternatives\n"
        "6. Highlight any time-sensitive actions or deadlines\n\n"
        "The advice should be clear, actionable, and in plain language while maintaining legal accuracy. "
        "Organize your response logically with appropriate headings and structure. Include a brief disclaimer "
        "about the general nature of the advice and the recommendation to consult with a licensed attorney "
        "for specific legal representation."
    ),
    expected_output="Clear, structured, and actionable legal advice that addresses the specific query with practical recommendations and appropriate legal context.",
    agent=legal_advisor,
    async_execution=False,
    output_file="legal_advice_response.md",
)

document_review_task = Task(
    description=(
        "Review and analyze the legal document described in '{legal_topic}'. Your review should:\n"
        "1. Identify the document type and its primary purpose\n"
        "2. Analyze key provisions and clauses\n"
        "3. Identify potential legal issues, ambiguities, or missing elements\n"
        "4. Assess compliance with relevant Indian laws and regulations\n"
        "5. Highlight risk areas and unfavorable terms\n"
        "6. Provide specific recommendations for improvements\n"
        "7. Rate the overall quality and effectiveness of the document\n\n"
        "Your analysis should be thorough, considering both legal and practical implications. "
        "Organize your review in a structured format with clear sections for findings and recommendations. "
        "Use bullet points where appropriate and prioritize issues by severity or importance."
    ),
    expected_output="A comprehensive document review with detailed analysis of provisions, identified issues, compliance assessment, and specific recommendations for improvement.",
    agent=document_reviewer,
    async_execution=False,
    output_file="document_review.md",
)

case_prediction_task = Task(
    description=(
        "Analyze the legal case described in '{legal_topic}' and predict its likely outcome based on similar precedents. "
        "Your prediction should:\n"
        "1. Identify the key legal issues and claims in the case\n"
        "2. Find and analyze similar cases with relevant precedential value in Indian courts\n"
        "3. Compare factual similarities and differences with precedent cases\n"
        "4. Analyze the current judicial trends in this area of law\n"
        "5. Consider jurisdiction-specific factors that might affect the outcome\n"
        "6. Provide a reasoned prediction with probability assessment (high, medium, low confidence)\n"
        "7. Outline potential alternative outcomes and key influencing factors\n\n"
        "Your analysis should be balanced, considering arguments from both sides. Include citations to relevant "
        "cases and statutes. Organize your prediction with clear reasoning and explicit assumptions. "
        "Acknowledge areas of uncertainty and provide a confidence level for your prediction."
    ),
    expected_output="A well-reasoned case outcome prediction with analysis of similar precedents, comparison of key factors, assessment of judicial trends, and clear probability statements.",
    agent=case_predictor,
    async_execution=False,
    output_file="case_prediction.md",
)