from crewai import Agent, Crew, Process, Task, LLM
from crewai.project import CrewBase, agent, crew, task

@CrewBase
class BlogPostWriter:

    agents_config = "config/agents.yaml"
    tasks_config = "config/tasks.yaml"

    def __init__(self):
        self.llm = LLM(
            model="ollama/llama3.2",
            base_url="http://localhost:11434"
        )

    @agent
    def research_agent(self) -> Agent:
        return Agent(
            config=self.agents_config["research_agent"],
            verbose=True,
            allow_delegation=False,
            llm=self.llm
        )

    @agent
    def content_analyzer_agent(self) -> Agent:
        return Agent(
            config=self.agents_config["content_analyzer_agent"],
            verbose=True,
            allow_delegation=False,
            llm=self.llm
        )
    
    @agent
    def writer_agent(self) -> Agent:
        return Agent(
            config=self.agents_config["writer_agent"],
            verbose=True,
            allow_delegation=False,
            llm=self.llm
        )
    
    @task
    def research_agent_task(self) -> Task:
        return Task(config=self.tasks_config["research_agent_task"])

    @task
    def content_analyzer_agent_task(self) -> Task:
        return Task(config=self.tasks_config["content_analyzer_agent_task"])
    
    @task
    def writer_agent_task(self) -> Task:
        return Task(config=self.tasks_config["writer_agent_task"])
    
    @crew
    def crew(self) -> Crew:
        return Crew(
            agents=self.agents,  # Automatically created by the @agent decorator
            tasks=self.tasks,  # Automatically created by the @task decorator
            process=Process.sequential,
            verbose=True,
        )