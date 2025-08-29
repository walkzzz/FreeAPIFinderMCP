# FreeAPIFinderMCP

FreeAPIFinderMCP 是一个用于发现和索引免费 API 的 MCP 服务器。它通过爬虫自动收集网络上的免费 API 信息，并提供 API 接口供开发者查询和使用。

## 功能特性

- 自动爬虫系统，定时从多个源收集免费 API 信息
- 完善的数据库模型，存储 API 的详细信息
- RESTful API 接口，提供查询、筛选功能
- Docker 支持，易于部署

## 技术栈

- Python 3.11
- FastAPI
- SQLAlchemy
- BeautifulSoup4
- Uvicorn
- Docker
