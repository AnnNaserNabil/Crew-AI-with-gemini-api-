import os
from crewai import LLM

# Read your API key from the environment variable
gemini_api_key = os.getenv("GEMINI_API_KEY")

if not gemini_api_key:
    raise ValueError("GEMINI_API_KEY environment variable not set.")

# Use Gemini 2.5 Pro Experimental model
gemini_llm = LLM(
    model='gemini/gemini-2.0-flash', 
    api_key=gemini_api_key,
    temperature=0.7  # Higher temperature for creative feature analysis
)

from crewai.tools import BaseTool


# Tool for fetching market research data
class MarketResearchTool(BaseTool):
    name: str = "Market Research Data Fetcher"
    description: str = "Fetches market research data, competitor analysis, and customer feedback. Returns a structured data summary."

    def _run(self, argument: str) -> str:
        print(f"--- Fetching market research data for: {argument} ---")
        return ("\n".join([
            "Market Research Summary:",
            "- Competitor Analysis: 3 main competitors identified with similar features.",
            "- Customer Feedback: 60% users want improved mobile experience, 40% request AI integration.",
            "- Market Trends: Growing demand for personalized features and automation.",
            "- Price Analysis: Average competitor pricing $19.99 - $49.99 monthly.",
            "- Feature Comparison: Missing features: Mobile app, AI assistant, analytics dashboard."
        ]))

# Tool for fetching technical feasibility data
class TechFeasibilityTool(BaseTool):
    name: str = "Technical Feasibility Analyzer"
    description: str = "Analyzes technical feasibility of proposed features based on current tech stack and resources."

    def _run(self, argument: str) -> str:
        print(f"--- Analyzing technical feasibility for: {argument} ---")
        return ("\n".join([
            "Technical Feasibility Analysis:",
            "- Current Tech Stack: Python, React, PostgreSQL",
            "- Resource Availability: 5 developers, 2 QA engineers",
            "- Integration Complexity: Medium for AI features, Low for UI improvements",
            "- Infrastructure: Cloud hosting with auto-scaling capabilities",
            "- Security Considerations: GDPR compliance required for new features"
        ]))

from crewai import Agent

# Agent 1: Market Analyst
market_analyst = Agent(
    role='Market Research Analyst',
    goal='Analyze market trends, competitor features, and customer needs to identify gaps and opportunities.',
    backstory=(
        "You are an expert market researcher with deep knowledge of tech industry trends and customer behavior."
        "You excel at identifying market gaps and emerging opportunities."
    ),
    verbose=True,
    allow_delegation=False,
    tools=[MarketResearchTool()],
    llm=gemini_llm
)

# Agent 2: Product Manager
product_manager = Agent(
    role='Product Manager',
    goal='Design new product features that align with market needs and technical feasibility.',
    backstory=(
        "You are an experienced product manager with a track record of successful feature launches."
        "You balance user needs, technical constraints, and business goals effectively."
    ),
    verbose=True,
    allow_delegation=False,
    tools=[TechFeasibilityTool()],
    llm=gemini_llm
)

# Agent 3: UX Designer
ux_designer = Agent(
    role='UX Designer',
    goal='Design intuitive and user-friendly interfaces for new features.',
    backstory=(
        "You are a UX design expert focused on creating seamless user experiences."
        "You prioritize user feedback and accessibility in your designs."
    ),
    verbose=True,
    allow_delegation=False,
    llm=gemini_llm
)

from crewai import Task

# Task 1: Market Analysis
market_analysis_task = Task(
    description=(
        "Conduct a comprehensive market analysis to identify:"
        "1. Key competitor features and strengths"
        "2. Customer pain points and unmet needs"
        "3. Emerging market trends and opportunities"
        "Use the Market Research Data Fetcher tool to gather relevant data."
    ),
    expected_output=(
        "A detailed market analysis report including:"
        "- Competitor feature matrix"
        "- Customer needs analysis"
        "- Market opportunity assessment"
        "- Recommended feature priorities"
    ),
    agent=market_analyst
)

# Task 2: Feature Design
feature_design_task = Task(
    description=(
        "Based on the market analysis, design new product features that:"
        "1. Address identified customer needs"
        "2. Differentiate from competitors"
        "3. Are technically feasible"
        "Use the Technical Feasibility Analyzer tool to validate proposed features."
    ),
    expected_output=(
        "A feature design specification including:"
        "- Proposed new features"
        "- Technical requirements"
        "- Integration considerations"
        "- Resource estimates"
    ),
    agent=product_manager
)

# Task 3: UX Design
ux_design_task = Task(
    description=(
        "Design intuitive user interfaces for the proposed features:"
        "1. Create wireframes for new feature screens"
        "2. Define user interaction flows"
        "3. Ensure accessibility compliance"
        "4. Consider mobile-first approach"
    ),
    expected_output=(
        "UX design documentation including:"
        "- Wireframes and mockups"
        "- User flow diagrams"
        "- Accessibility considerations"
        "- Mobile responsiveness guidelines"
    ),
    agent=ux_designer
)

from crewai import Crew, Process

# Create the crew
feature_design_crew = Crew(
    agents=[market_analyst, product_manager, ux_designer],
    tasks=[market_analysis_task, feature_design_task, ux_design_task],
    process=Process.sequential,
    verbose=True
)

# Start the crew's work
print("--- Starting Feature Design Crew ---")
result = feature_design_crew.kickoff(inputs={'product_name': 'TechPro Suite'})

print("--- Crew Execution Finished ---")
print("--- Final Feature Design Documentation ---")
print(result)
