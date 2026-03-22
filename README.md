# 🧠 MCP Memory Chat Agent (Weather Tool Integration)

An interactive AI chat application built using **MCP (Model Context Protocol)** Agent with built-in conversation memory.

This project demonstrates how an LLM can connect with external tools (like a Weather Server) using MCP architecture and maintain conversation context across multiple user queries.

---

## 🚀 Features

✅ Interactive CLI Chat
✅ MCP Tool Integration (Weather Server)
✅ Built-in Conversation Memory
✅ Async Execution using asyncio
✅ Clear Chat History Command
✅ Graceful Session Cleanup
✅ Environment Variable Based API Key Handling

---

## 🏗️ Architecture

User → MCPAgent → MCPClient → MCP Server (Weather Tool)

* **MCPAgent**
  Handles reasoning, memory, and tool execution

* **MCPClient**
  Connects to external MCP servers

* **LLM (Groq Llama Model)**
  Generates responses and decides tool usage

---

## 📦 Tech Stack

* Python
* asyncio
* LangChain Groq
* MCP Use Library
* dotenv

---

## 📁 Project Structure

```
project/
│
├── main.py
├── server/
│   └── weather.json
├── .env
└── README.md
```

---

## ⚙️ Setup Instructions

### 1️⃣ Clone the Repository

```
git clone <repo-url>
cd <repo-name>
```

---

### 2️⃣ Create Virtual Environment

```
python -m venv venv
```

Activate:

Windows:

```
venv\Scripts\activate
```

Mac/Linux:

```
source venv/bin/activate
```

---

### 3️⃣ Install Dependencies

```
pip install -r requirements.txt
```

---

### 4️⃣ Setup Environment Variables

Create `.env` file:

```
GROQ_API_KEY=your_api_key_here
```

---

### 5️⃣ Configure MCP Server

Update the config file path:

```
config_file = "server/weather.json"
```

Ensure the MCP weather server is correctly defined.

---

## ▶️ Run the Application

```
python main.py
```

---

## 💬 Chat Commands

| Command     | Description               |
| ----------- | ------------------------- |
| exit / quit | End chat session          |
| clear       | Clear conversation memory |

---

## 🧠 How Memory Works

* When `memory_enabled=True`, MCPAgent automatically stores previous user interactions.
* This allows contextual conversations like:

```
User: What is weather in Chennai?
User: What about tomorrow?
```

Agent understands that *"tomorrow"* refers to Chennai.

---

## 🧹 Session Cleanup

All MCP sessions are safely closed when the application exits.

---

## 🎯 Learning Outcome

This project helps understand:

* MCP Architecture
* Tool-Calling LLM Agents
* Async AI Systems
* Memory Management in Agents
* Real-world AI Integration Patterns

---

## 📌 Future Improvements

* Add Streaming Response Support
* Add Multiple Tool Servers (DB / Email / Maps)
* Add Persistent Memory (Vector DB)
* Build Web UI using FastAPI / React

---

## 👨‍💻 Author

Built as part of learning MCP Agent Systems and AI Tool Integration.
