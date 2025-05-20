import streamlit as st
import os
from datetime import datetime
from crewai import LLM, Agent, Task, Crew, Process
from crewai.tools import BaseTool
import json

# Initialize session state
if 'analysis_result' not in st.session_state:
    st.session_state.analysis_result = None
if 'running' not in st.session_state:
    st.session_state.running = False

# Streamlit UI
def main():
    st.title("Customer Support Analysis Dashboard")
    
    # Sidebar configuration
    with st.sidebar:
        st.header("Configuration")
        
        # Date range selection
        st.subheader("Analysis Period")
        start_date = st.date_input("Start Date", value=datetime.now().date().replace(day=1))
        end_date = st.date_input("End Date", value=datetime.now().date())
        
        # Analysis parameters
        st.subheader("Analysis Parameters")
        temperature = st.slider("Analysis Temperature", 0.0, 1.0, 0.0, 0.1)
        
        # Run analysis button
        if st.button("Run Analysis"):
            if not st.session_state.running:
                st.session_state.running = True
                st.session_state.analysis_result = run_analysis(start_date, end_date, temperature)
                st.session_state.running = False

    # Main content
    if st.session_state.running:
        st.info("Running analysis... Please wait.")
        st.spinner()
    
    if st.session_state.analysis_result:
        st.header("Analysis Results")
        
        # Display results in a structured way
        col1, col2 = st.columns(2)
        
        with col1:
            st.subheader("Key Findings")
            findings = st.session_state.analysis_result.get('findings', [])
            for finding in findings:
                st.markdown(f"- **{finding}**")
        
        with col2:
            st.subheader("Recommendations")
            recommendations = st.session_state.analysis_result.get('recommendations', [])
            for rec in recommendations:
                st.markdown(f"- **{rec}**")

        # Download button
        if st.button("Download Report"):
            report_text = json.dumps(st.session_state.analysis_result, indent=2)
            st.download_button(
                label="Download JSON Report",
                data=report_text,
                file_name=f"support_analysis_{datetime.now().strftime('%Y%m%d')}.json",
                mime="application/json"
            )

def run_analysis(start_date, end_date, temperature):
    """Run the customer support analysis using CREW AI"""
    # Initialize Gemini LLM
    gemini_api_key = os.getenv("GEMINI_API_KEY")
    if not gemini_api_key:
        raise ValueError("GEMINI_API_KEY environment variable not set.")
    
    gemini_llm = LLM(
        model='gemini/gemini-2.0-flash', 
        api_key=gemini_api_key,
        temperature=temperature
    )

    # Initialize tools and agents
    support_data_tool = CustomerSupportDataTool()
    
    data_analyst = Agent(
        role='Customer Support Data Analyst',
        goal='Analyze customer support data to identify trends and recurring issues.',
        backstory="""You are an expert data analyst specializing in customer support operations. 
        Your strength lies in identifying patterns and quantifying problems from raw support data.""",
        verbose=True,
        allow_delegation=False,
        tools=[support_data_tool],
        llm=gemini_llm
    )

    process_optimizer = Agent(
        role='Process Optimization Specialist',
        goal='Identify bottlenecks and inefficiencies in support processes.',
        backstory="""You are a specialist in optimizing business processes, particularly in customer support. 
        You excel at pinpointing root causes of delays and inefficiencies and suggesting concrete solutions.""",
        verbose=True,
        allow_delegation=False,
        llm=gemini_llm
    )

    report_writer = Agent(
        role='Executive Report Writer',
        goal='Compile analysis into a clear, actionable report.',
        backstory="""You are a skilled writer adept at creating executive summaries and reports. 
        You focus on clarity, conciseness, and highlighting the most critical information.""",
        verbose=True,
        allow_delegation=False,
        llm=gemini_llm
    )

    # Create and run tasks
    analysis_task = Task(
        description=f"""Analyze customer support data from {start_date} to {end_date}. 
        Focus on recurring issues, resolution times, and customer sentiment.""",
        agent=data_analyst
    )

    optimization_task = Task(
        description="""Based on the data analysis, identify process bottlenecks 
        and propose actionable improvements.""",
        agent=process_optimizer
    )

    report_task = Task(
        description="""Compile findings into a concise executive report.""",
        agent=report_writer
    )

    # Create and run the crew
    crew = Crew(
        agents=[data_analyst, process_optimizer, report_writer],
        tasks=[analysis_task, optimization_task, report_task],
        process=Process.sequential,
        verbose=True
    )

    result = crew.kickoff(inputs={'data_query': f"data from {start_date} to {end_date}"})
    
    # Format the result for display
    formatted_result = {
        'findings': [],
        'recommendations': []
    }
    
    # Parse the result and extract key information
    if isinstance(result, str):
        try:
            # Try to parse as JSON if possible
            parsed = json.loads(result)
            formatted_result['findings'] = parsed.get('findings', [])
            formatted_result['recommendations'] = parsed.get('recommendations', [])
        except:
            # If not JSON, split by common separators
            sections = result.split('\n\n')
            for section in sections:
                if 'finding' in section.lower():
                    formatted_result['findings'].append(section)
                elif 'recommendation' in section.lower():
                    formatted_result['recommendations'].append(section)
    
    return formatted_result

if __name__ == "__main__":
    main()
