import requests
from datetime import datetime
from typing import Union, Literal, List
from mcp.server import FastMCP
from pydantic import Field
from typing import Annotated
from mcp.server.fastmcp import FastMCP
from fastmcp import FastMCP, Context
import os
from dotenv import load_dotenv
load_dotenv()
rapid_api_key = os.getenv("RAPID_API_KEY")

__rapidapi_url__ = 'https://rapidapi.com/judge0-official/api/judge0-ce'

mcp = FastMCP('judge0-ce')

@mcp.tool()
def get_asubmission(base64_encoded: Annotated[Union[bool, None], Field(description='We recommend that you always set base64_encoded to true and receive Base64 encoded data from Judge0. Just like in creating submission you can receive Base64 encoded data for every text type attribute. By default, this parameter is set to false and Judge0 will send you raw data.')] = None,
                    fields: Annotated[Union[str, None], Field(description='Return only the desired submission attributes. The default value for the fields parameter is stdout,time,memory,stderr,token,compile_output,message,status. Use * to receive all available attributes.')] = None) -> dict: 
    '''Get submission.'''
    url = 'https://judge0-ce.p.rapidapi.com/submissions/2e979232-92fd-4012-97cf-3e9177257d10'
    headers = {'x-rapidapi-host': 'judge0-ce.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'base64_encoded': base64_encoded,
        'fields': fields,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def create_asubmission(data: Annotated[dict, Field(description='')] = None) -> dict: 
    '''Creates new submission. Created submission waits in queue to be processed. On successful creation, you are returned a submission token which can be used to check submission status.'''
    url = 'https://judge0-ce.p.rapidapi.com/submissions'
    headers = {'Content-Type': 'application/json', 'x-rapidapi-host': 'judge0-ce.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    response = requests.post(url, headers=headers, json=data)
    return response.json()

@mcp.tool()
def create_abatched_submission(data: Annotated[dict, Field(description='')] = None) -> dict: 
    '''Create multiple submissions at once.'''
    url = 'https://judge0-ce.p.rapidapi.com/submissions/batch'
    headers = {'Content-Type': 'application/json', 'x-rapidapi-host': 'judge0-ce.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    response = requests.post(url, headers=headers, json=data)
    return response.json()

@mcp.tool()
def get_abatched_submission(tokens: Annotated[str, Field(description='')],
                            base64_encoded: Annotated[Union[bool, None], Field(description='We recommend that you always set base64_encoded to true and receive Base64 encoded data from Judge0. Just like in creating submission you can receive Base64 encoded data for every text type attribute. By default, this parameter is set to false and Judge0 will send you raw data.')] = None,
                            fields: Annotated[Union[str, None], Field(description='Return only the desired submission attributes. The default value for the fields parameter is stdout,time,memory,stderr,token,compile_output,message,status. Use * to receive all available attributes.')] = None) -> dict: 
    '''Get multiple submissions at once.'''
    url = 'https://judge0-ce.p.rapidapi.com/submissions/batch'
    headers = {'x-rapidapi-host': 'judge0-ce.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'tokens': tokens,
        'base64_encoded': base64_encoded,
        'fields': fields,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def get_alanguage(id: Annotated[str, Field(description='')]) -> dict: 
    '''Get a language.'''
    url = 'https://judge0-ce.p.rapidapi.com/languages/52'
    headers = {'x-rapidapi-host': 'judge0-ce.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'id': id,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def get_languages() -> dict: 
    '''Get active languages.'''
    url = 'https://judge0-ce.p.rapidapi.com/languages'
    headers = {'x-rapidapi-host': 'judge0-ce.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def get_statuses() -> dict: 
    '''Get statuses.'''
    url = 'https://judge0-ce.p.rapidapi.com/statuses'
    headers = {'x-rapidapi-host': 'judge0-ce.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def get_configuration() -> dict: 
    '''Configuration information gives you detailed information about the configuration of Judge0.'''
    url = 'https://judge0-ce.p.rapidapi.com/config_info'
    headers = {'x-rapidapi-host': 'judge0-ce.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def about() -> dict: 
    '''Get general information.'''
    url = 'https://judge0-ce.p.rapidapi.com/about'
    headers = {'x-rapidapi-host': 'judge0-ce.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()



if __name__ == '__main__':
    import sys
    port = int(sys.argv[1]) if len(sys.argv) > 1 else 9997
    mcp.run(transport="stdio")
