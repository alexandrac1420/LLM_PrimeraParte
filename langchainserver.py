#!/usr/bin/env python
import os
from fastapi import FastAPI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_openai import ChatOpenAI
from langserve import add_routes

#0. Define the OPENAI_API_KEY
os.environ["OPENAI_API_KEY"] = "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"

# 1. Create prompt template
system_template = "Translate the following into {language}:"
prompt_template = ChatPromptTemplate.from_messages([
    ('system', system_template),
    ('user', '{text}')
])

# 2. Create model
model = ChatOpenAI()

# 3. Create parser
parser = StrOutputParser()

# 4. Create chain
chain = prompt_template | model | parser

# 5. App definition
app = FastAPI(
  title="LangChain Server",
  version="1.0",
  description="A simple API server using LangChain's Runnable interfaces",
)

# 6. Adding chain route
add_routes(
    app,
    chain,
    path="/chain",
)

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="localhost", port=8000)