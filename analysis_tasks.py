from crewai import Task
from textwrap import dedent


class AnalysisTasks:

    def __init__(self, urls):
        self.urls = urls

    def scrape(self, agent):
        return Task(
            description=dedent(f"""
            Take a list of websites that contains AI content, scrape the content and use it for your research. 
            Here is the list of URLs from the user that you need to scrape: {self.urls}. Only scrape the websites provided by the user.
            {self.__tip_section()}"""
                               ),
            expected_output='A detailed compilation of relevant content from the specified URLs',
            agent=agent
        )

    def research(self, agent):
        return Task(
            description=dedent(f"""
            Using the content obtained from the scraped websites, conduct a thorough analysis of the current AI hype, with a specific focus on democratic risks, 
            the dynamics of the labor market, and how it compares to past technological disruptions. 
            Consider short-term trends in AI application, demand for different AI competencies, early adopters in various industries, 
            and long-term scenarios involving AGI. Aim to provide an objective analysis that avoids political biases.
            {self.__tip_section()}"""
                               ),
            expected_output='A detailed analysis of the content scraped from the websites',
            agent=agent
        )

    def write(self, agent):
        return Task(
            description=dedent(
                f"""Examine the AI hype's landscape through a unique lens, focusing on its democratic implications, 
                labor market dynamics, and comparisons with historical technological revolutions. Highlight emerging trends 
                in AI adoption across various industries and the evolving demand for AI skills. Reflect on long-term scenarios 
                involving Artificial General Intelligence (AGI) and bring your own insights into how these developments parallel, 
                contrast, or echo past technological disruptions. Your analysis should transcend mere reporting by weaving 
                together a narrative that connects the dots between the past, present, and potential future of technological 
                evolution. Use primary content obtained from the scraped websites as a base but elevate the discourse with 
                your perspective and expertise. {self.__tip_section()}"""
            ),
            expected_output="An essay that transcends a simple synthesis of scraped content, embodying a rich tapestry of analysis, critique, and prognostication. This essay should not only articulate the nuanced implications of AI on democracy, the labor market, and societal structures but also offer a thoughtful exploration of how AI might shape our future in both utopian and dystopian scenarios. Your narrative should draw clear lines from past technological disruptions to the present day, providing a comprehensive discussion on potential futures while grounding your argument in both the content obtained and your analytical prowess. The essay should culminate in a visionary yet grounded reflection on how society can navigate the AI epoch, ensuring that technological advancements align with ethical imperatives and human-centric values.",
            agent=agent
        )

    def __tip_section(self):
        return "If you do your BEST WORK, I'll give you a $10,000 commission!"
