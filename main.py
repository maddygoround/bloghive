#!/usr/bin/env python
import warnings

from crew import BlogPostWriter

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")


def run():
    """
    Run the crew.
    """
    inputs = {
        "topic": "Burnout in the Workplace",
        "additional_urls": [
            "https://www.who.int/news-room/detail/28-05-2019-burn-out-an-occupational-phenomenon-international-classification-of-diseases",
            "https://www.mayoclinic.org/healthy-lifestyle/adult-health/in-depth/burnout/art-20046642",
        ],
    }
    result = BlogPostWriter().crew().kickoff(inputs=inputs)
    print(result)


if __name__ == "__main__":
    run()
