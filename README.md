# AI App Basics
Ravin Kumar, Hugo Bowne Anderson

In this tutorial we are going to go through the absolute basics of building applications using AI systems.

# Coding environment
We'll be using Gemma with Ollama locally and a python environment.
If you are unable to run things locally, parts of this tutorial can be performed with Gemini API and AIStudio.

## Ollama setup
**This is most critical**
This will take the longest amount of time and take a lot of internet bandwidth. 

To setup this you'll need to
1. Download Ollama https://ollama.com/
2. Run the following commands to pull our gemma models
   * `ollama pull gemma:2b`
   * `ollama pull gemma2:2b-instruct-fp16`
   * `ollama pull gemma2:2b-instruct-q2_K`

**Note**: This is going to take up about 10 gigs of space on your computer. Depending on your hardware some of these models may not even load. Consider this part of this tutorial. AI models, while becoming easier and cheaper to use, still require you to grapple with the model, if not you someone else. 

## Python
**Note**: This tutorial must be run locally. It will not work in colab or any other cloud environment due to the ollama dependency.

For python use your package manager of choice and install the packages in `requirements.txt`s