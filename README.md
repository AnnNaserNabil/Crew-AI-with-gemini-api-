# Customer Support Analysis System with CREW AI and Gemini API

This system automates the analysis of customer support data using CREW AI framework and Google's Gemini 2.5 Pro Experimental model. It provides a multi-agent approach to analyze support data, identify bottlenecks, and generate executive reports for decision-makers.

## System Overview

The system consists of three specialized AI agents working together:

1. **Data Analyst Agent**
   - Analyzes customer support data to identify trends and patterns
   - Focuses on recurring issues and their impact
   - Uses a custom tool to fetch support data

2. **Process Optimizer Agent**
   - Identifies bottlenecks in support processes
   - Proposes actionable improvements
   - Focuses on root cause analysis

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
