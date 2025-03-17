from langchain_openai import ChatOpenAI
from langchain_anthropic import ChatAnthropic
from langchain_google_genai import ChatGoogleGenerativeAI

from langchain_core.messages import SystemMessage, HumanMessage, AIMessage, ToolMessage
from langchain.memory import ConversationBufferMemory
from langchain.prompts import ChatPromptTemplate, MessagesPlaceholder

from langgraph.prebuilt import create_react_agent

import asyncio

import os
import sys
from dotenv import load_dotenv

sys.path.append(os.path.join(os.path.dirname(__file__), '../../langchain-tools'))

# Import tools here
from math_tool import (
    multiply, add, subtract, divide
)


load_dotenv()

class LangChainController:
    """Controller for handling LangChain operations with different models."""
    
    def __init__(self):
        self.openai_api_key = os.getenv("OPENAI_API_KEY")
        self.anthropic_api_key = os.getenv("ANTHROPIC_API_KEY")
        self.google_api_key = os.getenv("GOOGLE_API_KEY")
        
        # Initialize tool collections
        self.tools = {
            "math": [
                multiply, add, subtract, divide
            ],
            # Add more tool categories here 
        }
        
        # Model configurations
        self.models = {
            "claude-3-7-sonnet-20250219": {
                "provider": "anthropic",
                "name": "claude-3-7-sonnet-20250219"
            },
            "claude-3-5-haiku-20241022": {
                "provider": "anthropic",
                "name": "claude-3-5-haiku-20241022"
            },
            "claude-3-5-sonnet-20241022": {
                "provider": "anthropic",
                "name": "claude-3-5-sonnet-20241022"
            },
            # add more models here
        }
    
    def get_model_instance(self, model_id):
        """Get the appropriate model instance based on the model ID."""
        if model_id not in self.models:
            raise ValueError(f"Model {model_id} not supported")
        
        model_config = self.models[model_id]
        provider = model_config["provider"]
        model_name = model_config["name"]
        
        if provider == "openai":
            if not self.openai_api_key:
                raise ValueError("OpenAI API key not found")
            return ChatOpenAI(
                model_name=model_name,
                openai_api_key=self.openai_api_key,
                temperature=0.7
            )
        
        elif provider == "anthropic":
            if not self.anthropic_api_key:
                raise ValueError("Anthropic API key not found")
            return ChatAnthropic(
                model_name=model_name,
                anthropic_api_key=self.anthropic_api_key,
                temperature=0.7
            )
        
        elif provider == "google":
            if not self.google_api_key:
                raise ValueError("Google API key not found")
            return ChatGoogleGenerativeAI(
                model=model_name,
                google_api_key=self.google_api_key,
                temperature=0.7
            )
        
        raise ValueError(f"Provider {provider} not supported")
    
 
    def ask_question(self, question, model_id="claude-3-5-haiku-20241022"):
        """Ask a question to the specified model and return the answer."""
        try:
            model = self.get_model_instance(model_id)
            message = HumanMessage(content=question)
            response = model.invoke([message])
            
            return {
                "answer": response.content,
                "model": model_id
            }
        
        except Exception as e:
            print(f"Error in ask_question: {str(e)}")
            raise Exception(f"Failed to get answer: {str(e)}")
    
    def parse_agent_response(self, raw_response):
        """
        Parses the response from a Claude LangGraph ReAct agent into structured JSON.

        :param raw_response: The raw output from agent.ainvoke()
        :return: A dictionary containing structured steps and the final answer
        """
        steps = []
        final_answer = ""

        if isinstance(raw_response, dict) and "messages" in raw_response:
            messages = raw_response["messages"]
        else:
            messages = [raw_response] if isinstance(raw_response, (HumanMessage, AIMessage, ToolMessage)) else []

        step_description = None  

        for message in messages:
            if isinstance(message, AIMessage):
                if isinstance(message.content, list):  
                    for content in message.content:
                        if content.get("type") == "text":
                            step_description = content["text"]
                        elif content.get("type") == "tool_use":
                            steps.append({
                                "step": f"Step {len(steps) + 1}",
                                "description": step_description,
                                "tool_used": content["name"],
                                "input": content["input"],
                                "output": None 
                            })
                else:
                    final_answer = message.content  
                
            elif isinstance(message, ToolMessage):
                for step in steps:
                    if step["tool_used"] == message.name and step["output"] is None:
                        try:
                            step["output"] = float(message.content)
                        except ValueError:
                            step["output"] = message.content 

        return {
            "steps": steps,
            "final_answer": final_answer
        }

    def ask_agent(self, question, model_id="claude-3-5-haiku-20241022", tool_categories=None):
            """
            Use LangGraph's ReAct agent approach to answer a question with multi-step reasoning.
            The agent decides if it needs any of the provided tools.
            
            :param question: The user's query
            :param model_id: The ID of the model to use (default: 'claude-3-5-haiku-20241022')
            :param tool_categories: (Optional) List of tool category names to enable (e.g. ["math"])
                                If None, all available tools are used.
            :return: dict with steps and final answer
            """
            try:
                model = self.get_model_instance(model_id)
                
                if tool_categories:
                    selected_tools = []
                    for cat in tool_categories:
                        selected_tools.extend(self.tools.get(cat, []))
                else:
                    selected_tools = []
                    for cat_tools in self.tools.values():
                        selected_tools.extend(cat_tools)
                
                # 3. Create a ReAct agent using LangGraph
                agent = create_react_agent(
                    model=model,
                    tools=selected_tools,
                    prompt= (
                        "You are a helpful assistant. \n\n"
                        "You have access to specialized tools to help you answer the question. \n\n"
                        "However, you do not need to use these tools if you can answer the question directly."
                        "You don't need to specify that you used a tool, just answer the question."
                    )
                )
                
                async def _run_agent():
                    result = await agent.ainvoke({"messages": question})
                    return result

                raw_response = asyncio.run(_run_agent())
                parsed_response = self.parse_agent_response(raw_response)

                print(parsed_response)
                
                return parsed_response
            
            except Exception as e:
                print(f"Error in ask_agent: {str(e)}")
                raise Exception(f"Failed to process query: {str(e)}")