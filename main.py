from fastapi import FastAPI, HTTPException, Path
from fastapi.responses import JSONResponse
import json
import os

app = FastAPI()


@app.get("/")
async def read_root():
    return {"Alma Dummy API": "v1"}


@app.get("/verify")
async def read_item(school: str, username: str, password: str):
    if school == "test" and username == "test.2025" and password == "test123":
        # Define the path to the JSON file
        verify_response = os.path.join(os.path.dirname(__file__), 'verify_response.json')
        # Open and read the JSON file
        with open(verify_response, 'r') as file:
            data = json.load(file)
        # Return the JSON data as a response
        return JSONResponse(content=data)


@app.get("/grades")
async def read_item(school: str, username: str, password: str):
    if school == "test" and username == "test.2025" and password == "test123":
        # Define the path to the JSON file
        verify_response = os.path.join(os.path.dirname(__file__), 'grades_response.json')
        # Open and read the JSON file
        with open(verify_response, 'r') as file:
            data = json.load(file)
        # Return the JSON data as a response
        return JSONResponse(content=data)


@app.get("/subject")
async def read_item(school: str, username: str, password: str):
    if school == "test" and username == "test.2025" and password == "test123":
        # Define the path to the JSON file
        verify_response = os.path.join(os.path.dirname(__file__), 'classinfo_response.json')
        # Open and read the JSON file
        with open(verify_response, 'r') as file:
            data = json.load(file)
        # Return the JSON data as a response
        return JSONResponse(content=data)


@app.get("/gpa")
async def read_item(school: str, username: str, password: str):
    if school == "test" and username == "test.2025" and password == "test123":
        # Define the path to the JSON file
        verify_response = os.path.join(os.path.dirname(__file__), 'gpa_response.json')
        # Open and read the JSON file
        with open(verify_response, 'r') as file:
            data = json.load(file)
        # Return the JSON data as a response
        return JSONResponse(content=data)


@app.get("/overall-info")
async def read_item(school: str, username: str, password: str):
    if school == "test" and username == "test.2025" and password == "test123":
        # Define the path to the JSON file
        verify_response = os.path.join(os.path.dirname(__file__), 'overall_info_response.json')
        # Open and read the JSON file
        with open(verify_response, 'r') as file:
            data = json.load(file)
        # Return the JSON data as a response
        return JSONResponse(content=data)


@app.get("/personal-info")
async def read_item(school: str, username: str, password: str):
    if school == "test" and username == "test.2025" and password == "test123":
        # Define the path to the JSON file
        verify_response = os.path.join(os.path.dirname(__file__), 'personal_info_response.json')
        # Open and read the JSON file
        with open(verify_response, 'r') as file:
            data = json.load(file)
        # Return the JSON data as a response
        return JSONResponse(content=data)


@app.get("/attendance")
async def read_item(school: str, username: str, password: str):
    if school == "test" and username == "test.2025" and password == "test123":
        # Define the path to the JSON file
        verify_response = os.path.join(os.path.dirname(__file__), 'attendance_response.json')
        # Open and read the JSON file
        with open(verify_response, 'r') as file:
            data = json.load(file)
        # Return the JSON data as a response
        return JSONResponse(content=data)
