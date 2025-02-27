# AI App Basics
Ravin Kumar, Hugo Bowne Anderson

In this tutorial we are going to go through the absolute basics of building applications using AI systems.

# American or Australian Football Detector
We'll be designing an application that can identify if a piece of text talking about an American Football team or an Australian one.

* Resistant to typos
* Multi Team classification
* If unsure indicate so

## Evaluation
* Define eval metrics for quality
* Build a basic eval loop

## Optimization
* Expose lower level inference details 
* Try different settings measure
  * Quality Changes
  * Speedup

## Iteration
* Pick another model and rerun evals
* Make decision if cost/compute expense tradeoff is worth it

# Coding environment
We'll be using Gemma with Ollama locally and a python environment.
If you are unable to run things locally, parts of this tutorial can be performed with Gemini API and AIStudio.

To setup this you'll need to
1. Download Ollama https://ollama.com/
2. Run the following commands to pull our gemma models
   * `ollama pull gemma:2b`
   * `ollama run gemma2:2b-instruct-fp16`
   * `ollama run gemma2:2b-instruct-q2_K`

**Note**: This is going to take up about 10 gigs of space on your computer. Depending on your hardware some of these models may not even load. Consider this part of this tutorial. AI models, while becoming easier and cheaper to use, still require you to grapple with the model, if not you someone else. 

If the model doesn't load we included the finished notebooks in the Secrets repo. Follow along to learn what's going on and still get the takeaways!