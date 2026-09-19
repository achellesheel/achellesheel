<div align="center">

[![Typing SVG](https://readme-typing-svg.demolab.com/?font=Cinzel+Decorative&size=36&duration=3500&pause=800&color=D4AF37&center=true&vCenter=true&width=900&height=100&lines=PRANAV+CHATURVEDI;AGENTIC+AI+%2F+RAG+ENGINEER;BUILDER+OF+TOOL-USE+LOOPS;ACCIO+PRODUCTION+SYSTEMS)](https://git.io/typing-svg)

*"Some are born great, some hack their way into greatness — one retrieval eval at a time."*

## 🐍 The Chamber of Secrets

*Something is slithering through the walls of the contribution graph...*

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/achellesheel/achellesheel/output/basilisk-dark.svg">
  <source media="(prefers-color-scheme: light)" srcset="https://raw.githubusercontent.com/achellesheel/achellesheel/output/basilisk-light.svg">
  <img alt="The Basilisk devours the contribution graph" src="https://raw.githubusercontent.com/achellesheel/achellesheel/output/basilisk.svg">
</picture>

*The Basilisk only answers to its master — and it feeds on every commit.*

<div align="center">

![divider](https://readme-typing-svg.demolab.com/?font=MedievalSharp&size=20&duration=1&pause=100000&color=8A2BE2&center=true&vCenter=true&width=700&height=40&lines=%E2%9D%A6+%E2%94%80%E2%94%80%E2%94%80+%E2%9A%A1+%E2%94%80%E2%94%80%E2%94%80+%E2%9D%A6)

</div>

</div>

## 🏆 The Triwizard Tournament — Agent Loops & RAG Systems

*Every champion carries a scar. Here's what each one actually broke, and what I did about it.*

| Trial | Project | Pattern | The Challenge | The Scar — What Broke → What I Did |
|---|---|---|---|---|
| 🐉 **The Dragon** | [research-agent](https://github.com/achellesheel/research-agent) | **Agent loop** (LangGraph) | Autonomous tool-use loop over web search + arXiv, persistent memory (SQLite + FAISS), structured research briefs. The LLM routes tool calls itself — no hardcoded pipeline. | ⚠️ **No scar logged yet.** Single-commit build, no incident write-up. This is the one champion that hasn't actually been to battle — next thing I fix before I call this story done. |
| 🌊 **The Black Lake** | [multilingual-rag-eval](https://github.com/achellesheel/multilingual-rag-eval) | **RAG eval** | Hindi + English retrieval evaluation across 4 FAISS index configs, 40 gold Q&A pairs, $0-cost proxy metrics for faithfulness/correctness/recall. | The multilingual embedding model I picked to support Hindi **quietly cost 21 points of English answer-correctness** in the same index (0.61 vs. 0.82) — invisible until I broke results out by language. [Full breakdown →](https://github.com/achellesheel/multilingual-rag-eval#design-decisions) |
| 🌀 **The Maze** | [llm-red-team-eval](https://github.com/achellesheel/llm-red-team-eval) | **Red-team eval** | Automated hallucination, injection, consistency, and refusal testing — generates a model report card. | First live run of the new `rag_injection` suite got a real model to **leak a fake admin backdoor code** from a single poisoned support doc, on a completely benign customer question. Verified with two independent retrievers so it wasn't a fluke. [Transcript →](https://github.com/achellesheel/llm-red-team-eval#-the-wedge-rag-pipelines-get-hacked-through-their-own-knowledge-base) |
| 📖 **The Restricted Section** | [knowledge-mcp-server](https://github.com/achellesheel/knowledge-mcp-server) | **RAG + MCP** | Local MCP server turning PDFs/notes into a semantic knowledge base — hybrid BM25/dense search, cross-encoder reranking. | **The Ghost Chunk** — a retrieval bug that silently corrupted every search snippet returned to the model, hunted down and fixed. [Full postmortem →](https://achellesheel.github.io/knowledge-mcp-server/) |
| ⚔️ **The Champion's Duel** | [search-ranking-service](https://github.com/achellesheel/search-ranking-service) | **Retrieval + re-ranking** | Two-stage production search: Elasticsearch BM25 retrieval → XGBoost learning-to-rank re-ranking, Dockerized, MLflow-tracked. | ⚠️ **No scar logged yet.** Runs and ranks correctly, but no documented incident — the second gap in the lineup. |

<div align="center">

![divider](https://readme-typing-svg.demolab.com/?font=MedievalSharp&size=20&duration=1&pause=100000&color=8A2BE2&center=true&vCenter=true&width=700&height=40&lines=%E2%9D%A6+%E2%94%80%E2%94%80%E2%94%80+%E2%9A%A1+%E2%94%80%E2%94%80%E2%94%80+%E2%9D%A6)

</div>

## 🎓 Hogwarts Coursework — GUVI-HCL Data Science (Batch DS-C-WE-E-B148)

| Project | What it does | The Scar |
|---|---|---|
| [omnifeedback-ai](https://github.com/achellesheel/omnifeedback-ai) | Capstone: enterprise feedback-triage platform — SQL star schema, TF-IDF/K-Means clustering, PyTorch BiLSTM + transfer-learned DistilBERT urgency scoring, BERT NER/BART summarization, GenAI copilot. | **Two real, publicly-logged bugs across 3 model versions**: an overfitting dataset (V1→V2), then a generalization failure a live user found — the model scored obviously-critical and obviously-positive feedback almost identically — fixed with transfer learning (V2→V3). Full build log in [`PROGRESS.md`](https://github.com/achellesheel/omnifeedback-ai/blob/main/PROGRESS.md). |
| [book-recommendation-system](https://github.com/achellesheel/book-recommendation-system) | Content-based + collaborative filtering book recommender with Streamlit UI | — |
| [garbage-classification-deep-learning](https://github.com/achellesheel/garbage-classification-deep-learning) | Deep learning image classifier for waste sorting — CNN with transfer learning | — |
| [real-estate-investment-advisor](https://github.com/achellesheel/real-estate-investment-advisor) | Real estate investment analysis tool — ROI calculation, market comparison, risk assessment | — |
| [brand-visibility-project](https://github.com/achellesheel/brand-visibility-project) | Brand visibility analysis using NLP — sentiment analysis, media monitoring, competitive intelligence | — |
| [brickview2.0](https://github.com/achellesheel/brickview2.0) | Property analytics dashboard — SQLite backend, data visualization | — |

## ✍️ The Daily Prophet — Articles

| Piece | Link |
|---|---|
| Women's Day 2026 | [achellesheel/womens_day_2026](https://github.com/achellesheel/womens_day_2026) |

<div align="center">

![divider](https://readme-typing-svg.demolab.com/?font=MedievalSharp&size=20&duration=1&pause=100000&color=8A2BE2&center=true&vCenter=true&width=700&height=40&lines=%E2%9D%A6+%E2%94%80%E2%94%80%E2%94%80+%E2%9A%A1+%E2%94%80%E2%94%80%E2%94%80+%E2%9D%A6)

</div>

## 🪄 The Wand Chooses the Engineer

<div align="center">

![Core](https://img.shields.io/badge/Core-Agentic%20AI%20%2F%20RAG-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Wood](https://img.shields.io/badge/Wood-LangChain%20%2F%20LangGraph%20%2F%20MCP-1C3C3C?style=for-the-badge)
![Loyalty](https://img.shields.io/badge/Loyalty-Retrieval%20%26%20Eval%2C%20End--to--End-8B0000?style=for-the-badge)
![House](https://img.shields.io/badge/House-Slytherin%20Ambition%20%C2%B7%20Ravenclaw%20Standards-1B4D3E?style=for-the-badge)
![Patronus](https://img.shields.io/badge/Patronus-Production--Grade%20Agent%20Systems-D4AF37?style=for-the-badge)

</div>

I don't build demos. I build **agent loops and RAG pipelines that get evaluated, get broken, and get fixed** — in public.

<div align="center">

![divider](https://readme-typing-svg.demolab.com/?font=MedievalSharp&size=20&duration=1&pause=100000&color=8A2BE2&center=true&vCenter=true&width=700&height=40&lines=%E2%9D%A6+%E2%94%80%E2%94%80%E2%94%80+%E2%9A%A1+%E2%94%80%E2%94%80%E2%94%80+%E2%9D%A6)

</div>

## 📜 Spells & Charms Cast Daily

- 🪄 **Accio Data** — retrieval that pulls exactly the right context, nothing extraneous (hybrid BM25 + dense + cross-encoder reranking)
- 🧭 **Point Me** — agent tool-routing: letting an LLM decide *when* to search, fetch, summarize, or stop, instead of a hardcoded pipeline
- 🛡️ **Protego** — input validation, guardrails, prompt-injection & indirect RAG-injection defense
- 🧠 **Legilimens** — LLM & RAG evaluation — hallucination rate, faithfulness, retrieval recall, not vibes
- 🕊️ **Expecto Patronum** — graceful fallback under real-world load
- 🧹 **Wingardium Leviosa** — CI/CD, shipped past `localhost`
- 🌀 **Confundo** — adversarial red-teaming and RAG-poisoning, breaking it before someone else does
- 😄 **Riddikulus** — five-minute incident fix, not a five-hour fire drill
- 🔓 **Alohomora** — reverse-engineering APIs with no manual

<div align="center">

![divider](https://readme-typing-svg.demolab.com/?font=MedievalSharp&size=20&duration=1&pause=100000&color=8A2BE2&center=true&vCenter=true&width=700&height=40&lines=%E2%9D%A6+%E2%94%80%E2%94%80%E2%94%80+%E2%9A%A1+%E2%94%80%E2%94%80%E2%94%80+%E2%9D%A6)

</div>

## 🧹 The Broom — Built for Speed

<div align="center">

![Docker](https://img.shields.io/badge/Containerized-Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white)
![K8s](https://img.shields.io/badge/Orchestrated-Kubernetes-326CE5?style=for-the-badge&logo=kubernetes&logoColor=white)
![MLflow](https://img.shields.io/badge/Tracked-MLflow-0194E2?style=for-the-badge&logo=mlflow&logoColor=white)
![FAISS](https://img.shields.io/badge/Retrieval-FAISS-4B8BBE?style=for-the-badge)
![MCP](https://img.shields.io/badge/Protocol-MCP-6A0DAD?style=for-the-badge)

</div>

Firebolt-class, not Nimbus 2000 nostalgia — if it's not fast enough to keep up, it doesn't make the team.

## ♟️ Wizard's Chess — Current Strategy

**Endgame: agentic AI systems that are measured, monitored, and trusted in production.** No checkers with side projects — pawns (retrieval eval pipelines) advancing, knights (agent tool-use loops) deep in enemy territory, queen (full production-grade agent stack, with every failure documented, not hidden) coming out soon.

<div align="center">

![divider](https://readme-typing-svg.demolab.com/?font=MedievalSharp&size=20&duration=1&pause=100000&color=8A2BE2&center=true&vCenter=true&width=700&height=40&lines=%E2%9D%A6+%E2%94%80%E2%94%80%E2%94%80+%E2%9A%A1+%E2%94%80%E2%94%80%E2%94%80+%E2%9D%A6)

</div>

## 🔮 The Marauder's Map

<div align="center">

![Followers](https://img.shields.io/github/followers/achellesheel?style=for-the-badge&logo=github&label=Followers&color=6A0DAD&labelColor=1A1A2E)

</div>

### 🪄 Grimoire (Tech Stack)

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![LangChain](https://img.shields.io/badge/LangChain%20%2F%20LangGraph-1C3C3C?style=for-the-badge&logo=langchain&logoColor=white)
![MCP](https://img.shields.io/badge/MCP%20Protocol-6A0DAD?style=for-the-badge)
![FAISS](https://img.shields.io/badge/FAISS-4B8BBE?style=for-the-badge)
![Docker](https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white)
![Kubernetes](https://img.shields.io/badge/Kubernetes-326CE5?style=for-the-badge&logo=kubernetes&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=fastapi&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)
![MLflow](https://img.shields.io/badge/MLflow-0194E2?style=for-the-badge&logo=mlflow&logoColor=white)
![SQLite](https://img.shields.io/badge/SQLite-07405E?style=for-the-badge&logo=sqlite&logoColor=white)

<div align="center">

![divider](https://readme-typing-svg.demolab.com/?font=MedievalSharp&size=20&duration=1&pause=100000&color=8A2BE2&center=true&vCenter=true&width=700&height=40&lines=%E2%9D%A6+%E2%94%80%E2%94%80%E2%94%80+%E2%9A%A1+%E2%94%80%E2%94%80%E2%94%80+%E2%9D%A6)

</div>

<div align="center">

### 🦉 Send an Owl

[![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/pranav-chaturvedi-4538b4276/)
[![Email](https://img.shields.io/badge/Email-D14836?style=for-the-badge&logo=gmail&logoColor=white)](mailto:pranvc114@gmail.com)

*"It is our choices, Harry, that show what we truly are, far more than our abilities."*
**— and my choice is to ship, break it in public, and fix it.**

![Footer](https://capsule-render.vercel.app/api?type=waving&color=gradient&customColorList=6,11,20&height=100&section=footer)

</div>
