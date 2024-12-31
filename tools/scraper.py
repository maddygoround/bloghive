from crewai.tools import BaseTool
from pydantic import BaseModel, Field
import requests
import json
from bs4 import BeautifulSoup
from typing import Type


class WebSracperInput(BaseModel):
    topic: str = Field(..., title="Topic",
                       description="The topic to search for")
    additional_urls: list[str] = Field(..., title="Additional URLs",
                                       description="Additional URLs to scrape content from")


class ScrapURLs(BaseTool):
    name: str = "Scrap urls to generate a blog post"
    description: str = (
        "This tool queries multiple URLs to generate a blog post on a given topic."
    )
    args_schema: Type[BaseModel] = WebSracperInput

    def scrape_website(self, url: str) -> str:
        """Scrape content from a given URL"""
        try:
            response = requests.get(url)
            soup = BeautifulSoup(response.text, 'html.parser')

            # Remove script and style elements
            for script in soup(["script", "style"]):
                script.decompose()

            # Get text content
            text = soup.get_text(separator='\n')

            # Clean up text
            lines = (line.strip() for line in text.splitlines())
            chunks = (phrase.strip()
                      for line in lines for phrase in line.split("  "))
            text = ' '.join(chunk for chunk in chunks if chunk)

            return text
        except Exception as e:
            return f"Error scraping {url}: {str(e)}"

    def _run(
        self,
        topic: str,
        additional_urls: list[str]
    ) -> str:
        """
        Compile research from multiple URLs and search results.
        
        This tool is designed to aggregate and synthesize information from various online sources.
        It takes a list of URLs and search queries, fetches the content, and processes it to extract
        relevant data. The goal is to provide a comprehensive and cohesive summary of the topic at hand,
        enabling the creation of well-informed and insightful blog posts or articles.
        
        Key Features:
        - Fetches content from a list of provided URLs.
        - Performs web searches to gather additional information.
        - Extracts and processes relevant data from the fetched content.
        - Summarizes the compiled research into a cohesive format.
        
        Usage:
        - Provide a list of URLs and/or search queries.
        - Run the scraper to compile and process the research.
        - Use the summarized data for content creation or further analysis.
        """
        try:
            print("Scraping URLs...", additional_urls)
            research_data = []
            # Then, scrape provided URLs
            if additional_urls:
                for url in additional_urls:
                    content = self.scrape_website(url)
                    research_data.append({
                        'source': 'provided_url',
                        'link': url,
                        'content': content
                    })

                # Compile all research into a structured format
            compiled_research = {
                'topic': topic,
                'url_content': [item for item in research_data if item['source'] == 'provided_url']
            }

            return json.dumps(compiled_research, indent=2)
        except Exception as e:
            raise Exception(f"Failed to scrap urls: {str(e)}")
