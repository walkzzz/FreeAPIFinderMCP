# MCP Server Metadata

METADATA = {
    "name": "FreeAPIFinderMCP",
    "display_name": "Free API Finder",
    "description": "Discover and search for free public APIs",
    "version": "1.0.0",
    "tags": ["api", "free", "discovery", "public"],
    "icon": "🔍",
    "features": [
        {
            "name": "API Search",
            "description": "Search for APIs by name or description"
        },
        {
            "name": "Category Browsing",
            "description": "Browse APIs by category"
        },
        {
            "name": "Automatic Crawling",
            "description": "Regularly crawls multiple sources for new APIs"
        }
    ],
    "api_endpoints": [
        {
            "path": "/apis",
            "method": "GET",
            "description": "Get all APIs"
        },
        {
            "path": "/apis/search",
            "method": "GET",
            "description": "Search APIs"
        },
        {
            "path": "/apis/categories",
            "method": "GET",
            "description": "Get all categories"
        }
    ],
    "author": "",
    "license": "MIT",
    "repository": "",
    "homepage": ""
}