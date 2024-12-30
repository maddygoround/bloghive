# BlogHive

BlogHive is an automated system for creating well-researched and engaging blog posts. It leverages multiple agents to research, analyze, and write content based on a given topic.

## Project Structure
. ├── __init__.py ├── pycache/ ├── config/ │ ├── agents.yaml │ ├── tasks.yaml ├── crew.py ├── main.py └── README.md

- `__init__.py`: Initialization file for the package.
- `config/agents.yaml`: Configuration file for defining agent roles, goals, and backstories.
- `config/tasks.yaml`: Configuration file for defining tasks for each agent.
- `crew.py`: Contains the `BlogPostWriter` class which defines agents and tasks.
- `main.py`: Entry point for running the blog creation process.
- `README.md`: Project documentation.

## How It Works

The system uses the `BlogPostWriter` class to define and manage agents and tasks. The agents are responsible for researching, analyzing, and writing content. The tasks specify what each agent needs to accomplish.

### Agents

- **Research Agent**: Conducts comprehensive research on the given topic.
- **Content Analyzer Agent**: Analyzes the research findings and organizes key information.
- **Writer Agent**: Writes a comprehensive blog post based on the analyzed research.

### Tasks

- **Research Agent Task**: Defines the steps and expected output for the research agent.
- **Content Analyzer Agent Task**: Defines the steps and expected output for the content analyzer agent.
- **Writer Agent Task**: Defines the steps and expected output for the writer agent.

## Running the Project

To run the project, execute the `main.py` script:

```sh
python main.py

The script will initialize the BlogPostWriter crew and kick off the process with the provided inputs.

Example
The main.py script provides an example of how to run the crew with a specific topic:

inputs = {
    "topic": "Burnout in the Workplace",
    "additional_urls": [
        "https://www.who.int/news-room/detail/28-05-2019-burn-out-an-occupational-phenomenon-international-classification-of-diseases",
        "https://www.mayoclinic.org/healthy-lifestyle/adult-health/in-depth/burnout/art-20046642",
    ],
}
result = BlogPostWriter().crew().kickoff(inputs=inputs)
print(result)
```

This will generate a blog post on the topic "Burnout in the Workplace" using the specified additional URLs for research.

Dependencies
crewai: A library for managing agents and tasks.
pysbd: A library for sentence boundary detection (used with a warning filter).
License
This project is licensed under the MIT License.