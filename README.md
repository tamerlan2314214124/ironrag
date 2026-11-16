# 🛡️ IronRAG

**Industrial-grade RAG pipeline with layout-aware parsing and zero-hallucination fact verification.**

[![License](https://img.shields.io/badge/License-Apache_2.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)
[![Python 3.11+](https://img.shields.io/badge/python-3.11+-blue.svg)](https://www.python.org/downloads/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.100+-green.svg)](https://fastapi.tiangolo.com/)

IronRAG solves the two biggest pain points of enterprise AI: **garbage data ingestion** and **LLM hallucinations**. It parses complex documents (tables, technical PDFs, scans) with exact coordinate mapping and enforces strict verification before returning an answer.

---

## ⚡ Key Features

- **Coordinate-Mapped Parsing:** Extracts text, tables, and structured blocks while preserving exact page, table, and block IDs.
- **Built-in Fact Verifier (Guardrails):** Cross-checks every generated claim and number against source chunks.
- **Verifiable Citations:** Every response includes traceable references to the exact source block/page.
- **100% Local & Privacy-First:** Run completely on your own infrastructure. No data leaves your servers.

---

## 🚀 Quick Start (v0.1)

1. Clone the repository:
   ```bash
   git clone [https://github.com/tamerlan2314214124/ironrag.git](https://github.com/tamerlan2314214124/ironrag.git)
   cd ironrag

