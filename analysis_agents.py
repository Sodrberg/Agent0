from crewai import Agent
# from crewai_tools import SerperDevTool
from tools.scrape_tool import Scraper

# search_tool = SerperDevTool()
scraper_tool = Scraper()


class AnalysisAgents:
    def researcher(self):
        return Agent(
            role='Senior Researcher',
            goal="""Investigate the current AI hype, focusing on democratic risks, labor market dynamics, and comparisons with past technological disruptions.""",
            backstory="""Driven by curiosity, you're at the forefront of
            innovation, eager to explore and share knowledge that could change
            the world.""",
            verbose=True,
            memory=True,
            tools=[scraper_tool],
            allow_delegation=True
        )

    def writer(self):
        return Agent(
            role='Writer',
            goal="Compose a narrative that delves into the AI hype, addressing democratic risks, changes in the labor market, and the technology's future potential.",
            backstory="""With a flair for simplifying complex topics, you craft
            engaging narratives that captivate and educate, bringing new
            discoveries to light in an accessible manner.""",
            verbose=True,
            memory=True,
            allow_delegation=False
        )
