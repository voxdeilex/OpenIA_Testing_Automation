from dotenv import load_dotenv
import os
from browser_use import Agent
from browser_use.llm import ChatOpenAI
import pytest

load_dotenv()


@pytest.mark.asyncio
async def test_way2automation():   # <--- nombre correcto, inicia con test_
    agent = Agent(
    

    #"Find the number of stars of the browser-use repo",  # se da la instruccion en lenguaje natural a la IA
   task= """
    Open Site: https://way2automation.com/way2auto_jquery/index.php
    Fill every field slowly so the user can watch the information being typed
    then enter name as Ivan Huerta
    then enter the phone 6861324565
    then enter email as testing@way2automation.com
    then select country as Mexico
    then enter city as Mexicali
    then enter username as trainer@way2automation.com
    then enter password as adminpassword
    then click on submit button
    then verify the message contains "This is just a dummy form, you just clicked SUBMIT BUTTON"
    """,  
        
    llm=ChatOpenAI(model="gpt-4o-mini"),  # Especify Language AI Model
    browser_config={
        "headless": False,
        "slowMo": 1000,
        "type_delay": 150,
    }
)

    await agent.run()

##pytest -s OpenAIPyTest.py
