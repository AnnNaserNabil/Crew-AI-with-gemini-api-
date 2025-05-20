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
    temperature=0.7  # Balanced temperature for philosophical analysis
)

from crewai.tools import BaseTool


# Tool for historical context analysis
class HistoricalContextTool(BaseTool):
    name: str = "Historical Context Analyzer"
    description: str = "Analyzes historical context and influences of philosophical ideas."

    def _run(self, argument: str) -> str:
        print(f"--- Analyzing historical context for: {argument} ---")
        return ("\n".join([
            "Historical Context Analysis:",
            "- Time period and cultural background",
            "- Key historical events influencing the philosophy",
            "- Social and political context",
            "- Cross-cultural comparisons"
        ]))

# Tool for ethical implications analysis
class EthicalImplicationsTool(BaseTool):
    name: str = "Ethical Implications Analyzer"
    description: str = "Analyzes the ethical implications and moral consequences of philosophical ideas."

    def _run(self, argument: str) -> str:
        print(f"--- Analyzing ethical implications for: {argument} ---")
        return ("\n".join([
            "Ethical Implications Analysis:",
            "- Moral implications for individuals",
            "- Societal impact analysis",
            "- Potential consequences",
            "- Ethical dilemmas"
        ]))

from crewai import Agent

# Agent 1: Zen Master
zen_master = Agent(
    role='Zen Master',
    goal='Analyze topics from a Zen Buddhist perspective, focusing on mindfulness, emptiness, and direct experience.',
    backstory=(
        "You are a Zen master with deep understanding of Zen Buddhism. You emphasize direct experience,"
        "mindfulness, and the nature of reality. You focus on practical wisdom and the path of enlightenment."
    ),
    verbose=True,
    allow_delegation=False,
    llm=gemini_llm
)

# Agent 2: Stoic Philosopher
stoic_philosopher = Agent(
    role='Stoic Philosopher',
    goal='Analyze topics from a Stoic perspective, focusing on virtue, reason, and acceptance of nature.',
    backstory=(
        "You are a Stoic philosopher in the tradition of Marcus Aurelius and Epictetus. You emphasize"
        "virtue, reason, and living in accordance with nature. You focus on what can be controlled."
    ),
    verbose=True,
    allow_delegation=False,
    llm=gemini_llm
)

# Agent 3: Machiavellian Strategist
machiavellian_strategist = Agent(
    role='Machiavellian Strategist',
    goal='Analyze topics from a pragmatic, realpolitik perspective, focusing on power, strategy, and effectiveness.',
    backstory=(
        "You are a political strategist in the tradition of Machiavelli. You prioritize practical outcomes,"
        "strategic thinking, and the effective use of power. You focus on results over idealism."
    ),
    verbose=True,
    allow_delegation=False,
    llm=gemini_llm
)

# Agent 4: Nietzschean Critic
nietzschean_critic = Agent(
    role='Nietzschean Critic',
    goal='Analyze topics from a Nietzschean perspective, focusing on power, will, and the critique of morality.',
    backstory=(
        "You are a critic in the tradition of Friedrich Nietzsche. You question traditional values,"
        "emphasize the will to power, and critique moral dogmatism. You focus on individual strength."
    ),
    verbose=True,
    allow_delegation=False,
    llm=gemini_llm
)

# Agent 5: Existentialist Thinker
existentialist_thinker = Agent(
    role='Existentialist Thinker',
    goal='Analyze topics from an existentialist perspective, focusing on freedom, choice, and individual existence.',
    backstory=(
        "You are a thinker in the tradition of Sartre and Camus. You emphasize individual freedom,"
        "authenticity, and the meaning of existence. You focus on personal responsibility."
    ),
    verbose=True,
    allow_delegation=False,
    llm=gemini_llm
)

from crewai import Task

# Task 1: Historical Context Analysis
def create_analysis_task(topic: str):
    return Task(
        description=(
            f"Analyze the philosophical topic: '{topic}' from the perspective of your philosophical tradition."
            "Consider the following aspects:"
            "1. Core principles and beliefs"
            "2. Practical applications"
            "3. Modern relevance"
            "4. Potential challenges or limitations"
        ),
        expected_output=(
            "A comprehensive analysis including:"
            "- Key philosophical insights"
            "- Practical implications"
            "- Critical perspectives"
            "- Integration with modern context"
        ),
        agent=None  # Will be set dynamically
    )

from crewai import Crew, Process

# Create the crew
def create_philosophical_crew():
    agents = [
        zen_master,
        stoic_philosopher,
        machiavellian_strategist,
        nietzschean_critic,
        existentialist_thinker
    ]
    
    # Create tasks for each philosophical perspective
    tasks = []
    for agent in agents:
        task = create_analysis_task("The Nature of Freedom")
        task.agent = agent
        tasks.append(task)
    
    return Crew(
        agents=agents,
        tasks=tasks,
        process=Process.sequential,  # Run analyses in parallel for different perspectives
        verbose=True
    )

# Example usage
if __name__ == "__main__":
    print("--- Starting Philosophical Analysis Crew ---")
    
    # Create and run the crew
    philosophical_crew = create_philosophical_crew()
    result = philosophical_crew.kickoff(inputs={'topic': 'The Nature of Freedom'})
    
    print("\n--- Crew Execution Finished ---")
    print("\n--- Philosophical Analyses from Different Perspectives ---")
    print(result)
