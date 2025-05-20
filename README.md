# Customer Support Analysis System with CREW AI and Gemini API

This system automates the analysis of customer support data using CREW AI framework and Google's gemini-2.0-flash model. It provides a multi-agent approach to analyze support data, identify bottlenecks, and generate executive reports for decision-makers.

## System Overview

This repository showcases three powerful Python programs that leverage Crew AI and Google's Gemini API for intelligent agent-based applications. Each program demonstrates different aspects of AI-powered analysis and decision-making.

## Project Overview

This project consists of three main programs:

1. **Philosophical Analysis System**
   - Performs deep philosophical analysis using AI agents
   - Analyzes historical context and ethical implications
   - Uses specialized agents for different aspects of philosophy

2. **Product Feature Analysis System**
   - Conducts comprehensive product feature analysis
   - Integrates market research and technical feasibility analysis
   - Provides actionable insights for product development

3. **Crew AI Integration with Gemini API**
   - Core integration layer between Crew AI and Gemini
   - Demonstrates agent-based architecture
   - Shows how to implement custom tools and agents

## How Crew AI Works with Gemini API

The system leverages Crew AI's agent-based architecture combined with Google's Gemini 2.0 Flash model to create intelligent, specialized agents that can work together to solve complex problems. Key components include:

### Core Components

1. **LLM Integration**
   ```python
   gemini_llm = LLM(
       model='gemini/gemini-2.0-flash', 
       api_key=gemini_api_key,
       temperature=0.7
   )
   ```
   
2. **Custom Tools**
   - Historical Context Analyzer
   - Ethical Implications Analyzer
   - Market Research Data Fetcher
   - Technical Feasibility Analyzer

3. **Agent Architecture**
   - Specialized agents for different domains
   - Collaborative problem-solving
   - Task delegation and coordination

### Implementation Details

Each program follows a similar pattern:
1. Initialize Gemini LLM with appropriate parameters
2. Define custom tools for specific tasks
3. Create specialized agents
4. Form a crew of agents to work together
5. Execute tasks through agent collaboration
3. **Report Writer Agent**
   - Compiles findings into executive reports
   - Formats information for senior leadership
   - Creates clear, concise summaries

## Setup Requirements

1. **Environment Variables**
   - Set `GEMINI_API_KEY` with your Google Gemini API key

2. **Python Dependencies**
   - Install required packages:
   ```bash
   pip install crewai
   ```

## System Architecture

The system follows a sequential workflow:

1. **Data Analysis Phase**
   - Fetches recent support data
   - Identifies recurring issues
   - Quantifies impact metrics

2. **Process Analysis Phase**
   - Identifies bottlenecks
   - Analyzes root causes
   - Proposes improvements

3. **Report Generation Phase**
   - Creates executive summaries
   - Formats recommendations
   - Generates professional reports

## Key Features

- Multi-agent collaboration using CREW AI framework
- Integration with Gemini 2.5 Pro Experimental model
- Custom tool for support data fetching
- Sequential processing workflow
- Clear role separation between agents
- Professional report generation

## Running the System

1. Ensure environment variables are set
2. Execute the main script
3. The system will:
   - Analyze support data
   - Identify process bottlenecks
   - Generate an executive report

## Output Format

The final output is a structured executive report containing:
- Key support issues with metrics
- Process bottlenecks analysis
- Actionable recommendations
- Clear executive summary

## Customization

The system can be customized by:
- Adjusting agent parameters
- Modifying tool implementations
- Changing analysis focus areas
- Updating process recommendations

## Error Handling

The system includes basic error handling:
- API key validation
- Missing environment variable checks
- Clear error messages for failures

## Security

- API keys are managed through environment variables
- No hardcoded credentials
- Secure data handling throughout the process

## Future Enhancements

Potential improvements:
- Add more specialized agents
- Implement parallel processing
- Add data visualization capabilities
- Integrate with real-time data sources
- Add more sophisticated analysis tools
