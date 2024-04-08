import os
from dotenv import load_dotenv
from crewai import Crew
from textwrap import dedent, fill
from analysis_agents import AnalysisAgents
from analysis_tasks import AnalysisTasks

load_dotenv()
os.environ["SERPER_API_KEY"]
os.environ["OPENAI_API_KEY"]
model = os.environ["OPENAI_MODEL_NAME"] = "gpt-4-0125-preview"


class ResearchCrew:
    def __init__(self):
        self.urls = []

    def run(self):

        agents = AnalysisAgents()
        tasks = AnalysisTasks(self.urls)

        researcher_agent = agents.researcher()
        writer_agent = agents.writer()

        scraper_task = tasks.scrape(researcher_agent)
        research_task = tasks.research(researcher_agent)
        write_task = tasks.write(writer_agent)

        crew = Crew(
            agents=[researcher_agent, writer_agent],
            tasks=[scraper_task, research_task, write_task],
            verbose=True
        )

        result = crew.kickoff()
        return result


if __name__ == "__main__":
    print("## Welcome to the research crew!")
    print('-------------------------------')
    urls = input(
        dedent("""
        What urls do you want to analyze?
         """))

    research_crew = ResearchCrew()
    research_crew.urls = [urls.strip() for urls in urls.split(',')]
    result = research_crew.run()
    with open('output_examples.txt', 'a') as file:
        file.write("\n\n########################")
        file.write(f"\n## Here is the Report using {model}")
        file.write("\n########################\n")
        wrapped_text = fill(str(result), width=80)
        file.write(wrapped_text)
