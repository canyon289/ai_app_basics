# Welcome!

This repo contains everything you need for a hands-on workshop where we’ll build, evaluate, and optimize a local LLM-powered system. Unlike many LLM demos that focus on text generation, we’ll be leveraging one of the most powerful (and often overlooked) capabilities of LLMs: **zero-shot classification**.

One of the great things about LLMs isn’t just their generative ability, but their **in-context learning** and ability to classify data without needing a dedicated training phase. Usually, doing this with large models can be **expensive** and **slow**, but thanks to **Gemma 2B** and **Ollama**, we’ll run everything **locally**, making it **fast, cost-free, and fun**.

## What This Is (and What It Isn’t)

This workshop, *Building AI for Real-World Use Cases: From Basics to Production*, is designed to take you from understanding the fundamentals of AI-powered systems to building, evaluating, and optimizing them for real-world use.

It was inspired by a talk given by **Ravin Kumar**, *Building Cars and Building AI Apps, Two Technologies A Hundred Years Apart*, in [Hugo's **Building LLM Powered Applications for Data Scientists and Software Engineers** course](https://maven.com/s/course/d56067f338). In that talk, Ravin shared insights from his work at Google on **Notebook LM** and **Mariner**. [The slides from his talk are here](https://docs.google.com/presentation/d/e/2PACX-1vQanphgWMnZb2DwQsLJUxUVh1XbU1gv162lQyc2BUbom2no5TThljEH6-YWLc9APfxApZYAJkwMDu4K/pub?start=false&loop=false&delayms=60000#slide=id.p).

### ✅ **What This Is**
- A **practical, hands-on** approach to building **LLM-powered classification systems** that run **locally**.
- A **workflow-focused** deep dive into **prompting, evaluation, and optimization**—not just model selection.
- A chance to **iteratively build** and refine an AI system using **Gemma 2B + Ollama** while learning **how real-world AI applications are developed**.

### ❌ **What This Isn’t**
- **A deep dive into every LLM tool or framework**—we focus on workflow, not exhaustive tool coverage.
- **A step-by-step AI recipe book**—you’ll experiment, iterate, and debug instead of following rigid instructions.
- **A guide to large-scale production deployment**—this workshop is about learning the fundamentals, but scaling beyond local models is a separate challenge.

## 🛠 What You’ll Be Doing

This workshop is structured into four progressive sections. In each section, we’ll be working through **Jupyter notebooks** (found in the `notebooks/` directory) and, in some cases, executing scripts (stored in `apps/`).

### **1. Building the MVP AI System**
We’ll start by building a **zero-shot classification system** that predicts whether a sports team is from the **US or Australia**.
- You’ll see how an AI system is **more than just a model**—we’ll integrate models, data, and (optionally) a front-end and database.
- The core model we’ll use is **Gemma 2B**, running locally via **Ollama**.

### **2. Vibe-Based Evaluation**
Before we get into systematic evaluation, we’ll **test things informally**:
- Try out different prompts and see how the model responds.
- Get a **sense of what works and what doesn’t**—before committing to structured testing.
- This is how LLM practitioners often start: iterate, tweak, and experiment.

### **3. Repeatable Evaluations with an Eval Harness**
Once we’ve got a feel for the model’s behavior, we move to a **repeatable, systematic evaluation process**:
- We’ll introduce an **evaluation harness**, a structured script for testing model performance.
- Instead of relying on "vibes," we’ll **programmatically test** the model across different datasets, starting with team names and expanding to real-world examples (e.g., news articles).
- This step makes our system **reliable and testable**.

### **4. Optimization**
Now that we have a solid evaluation process, we can **optimize and refine** the system:
- Try different models and compare performance using our eval harness.
- Measure **accuracy** and **speed**, and discuss whether we should consider **cost** as a factor.
- This is where we start thinking about **how we’d take this system beyond just an experiment**.

## 🚀 Getting Started

To run this workshop locally, you'll need to set up **Ollama** and a Python environment using **UV**.

### **1. Setting Up Ollama** (Most Critical Step)
We’ll be running **Gemma 2B locally** with **Ollama**, so you need to set this up first. This step will require a **large download (~10GB total)** and some **hardware considerations**.

#### **Install Ollama**
Download and install Ollama from [https://ollama.com/](https://ollama.com/).

#### **Pull the required models**
Once installed, run the following commands in your terminal to download the models:

```shell
ollama pull gemma2:2b
ollama pull gemma2:2b-instruct-fp16
ollama pull gemma2:2b-instruct-q2_K
```

⚠️ **Note:** Some models may not run depending on your hardware. AI models, while getting easier to use, still come with real-world constraints—this is part of the learning process!

---

### **2. Setting Up Your Python Environment**

We’ll be using **UV** to manage dependencies. This ensures a lightweight, reproducible Python environment.

#### **Install UV**
If you don’t have UV installed, first install it with:

```shell
pip install uv
```

#### **Create and activate your environment**

```shell
uv venv gemma-app
```

Activate the environment:

- **On macOS/Linux:**  
  ```shell
  source gemma-app/bin/activate
  ```
- **On Windows:**  
  ```shell
  gemma-app\Scripts\activate
  ```

#### **Install dependencies**
Once the environment is active, install all required Python packages:

```shell
uv pip install -r requirements.txt
```

---

### **3. Running Jupyter Notebooks**

If you’re using Jupyter notebooks in this repository:
- **Select the correct Python interpreter** before running the notebook.
- Ensure that Jupyter is using the Python environment (`gemma-app`) you just created.

---

Now you’re ready to start building! 🚀

