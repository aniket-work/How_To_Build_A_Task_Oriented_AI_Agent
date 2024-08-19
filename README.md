# How_To_Build_A_Task_Oriented_AI_Agent
We're building task oriented AI Agent in this project. Task-oriented AI focuses on performing specific tasks rather than engaging in general conversations.


## Introduction

Full Article : [https://medium.com/@learn-simplified/how-to-build-task-oriented-ai-agents-1c130cad7158


## What's This Project About?

What Is This Article About?
This article is about AgentLite, a new software library designed to help developers build more efficient and effective AI systems that can handle specific tasks. Task-oriented AI systems are becoming increasingly important as they allow machines to perform complex functions, such as customer service, data analysis, or even creative work like writing and art. AgentLite offers a streamlined and accessible approach to creating these AI systems, making it easier for developers to design, build, and advance task-oriented AI agents without needing extensive resources or advanced technical expertise.

## Why Use This Project?

AI is rapidly changing the world around us, from the way businesses operate to the services we use every day. Understanding how these systems are built and improved is crucial for anyone interested in the future of technology. This article explains how AgentLite can simplify the development of AI agents, making the technology more accessible and versatile. Whether you’re a developer looking to enhance your AI skills, a business leader curious about integrating AI into your operations, or just someone interested in the future of technology, this article will provide valuable insights into the next wave of AI innovation.

## Architecture
![Design Diagram](design_docs/design.png)


# Tutorial: Setting Up and Running AI Agent Powered Refund Processing System

## Prerequisites
- Python installed on your system.
- A basic understanding of virtual environments and command-line tools.

## Steps

1. **Virtual Environment Setup:**
   - Create a dedicated virtual environment for our project:
   
     ```bash
     python -m venv How_To_Build_A_Task_Oriented_AI_Agent
     ```
   - Activate the environment:
   
     - Windows:
       ```bash
       How_To_Build_A_Task_Oriented_AI_Agent\Scripts\activate
       ```
     - Unix/macOS:
       ```bash
       source How_To_Build_A_Task_Oriented_AI_Agent/bin/activate
       ```

2. **Install Project Dependencies:**

   - Navigate to your project directory and install required packages using `pip`:
   
    ```bash 
   pip install -r requirements.txt
       
   if you wish to use original AgentLite repo, follow below
    git clone https://github.com/SalesforceAIResearch/AgentLite.git
    cd AgentLite
    pip install -e .     
    
    
    ```

3. **Run - Task Oriented AI Agents**

   Finally, execute the following command to start the "Task Oriented AI Agents" application:

   ```bash 
   # Run Task Oriented AI Agents
   (How_To_Build_A_Task_Oriented_AI_Agent) C:\Users\worka\PycharmProjects\How_To_Build_A_Task_Oriented_AI_Agent>python AgentLite\example\SearchManager.py
    ```
   




