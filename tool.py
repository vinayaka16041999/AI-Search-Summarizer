import requests


class Tools:
    def __init__(self):
        pass

    # Use the brave search summarizer to pass the summary of the web search to the model
    def get_summary(self, question: str) -> str:
        API_KEY = {BRAVE_API_KEY}

        # Brave Search API host
        API_HOST = "https://api.search.brave.com"

        # Brave Search API subpaths
        API_PATH = {
            "web": urljoin(API_HOST, "res/v1/web/search"),
            "summarizer_search": urljoin(API_HOST, "res/v1/summarizer/search"),
        }

        API_HEADERS = {
            "web": {"X-Subscription-Token": API_KEY, "Api-Version": "2023-10-11"},
            "summarizer": {
                "X-Subscription-Token": API_KEY,
                "Api-Version": "2024-04-23",
            },
        }

        # Create web search request params
        API_PARAMS_WEB = {
            "q": question,
            "summary": 1,
        }

        response = requests.get(
            API_PATH["web"], headers=API_HEADERS["web"], params=API_PARAMS_WEB
        )
        data = response.json()
        summary_key = data.get("summarizer", {}).get("key")
        summary_response = requests.get(
            API_PATH["summarizer_search"],
            headers=API_HEADERS["summarizer"],
            params={"key": summary_key, "entity_info": 1},
        )
        summary_data = summary_response.json()
        summary = summary_data.get("summary")[0].get("data")
        return f"{summary}"
