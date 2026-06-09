# Flower Insight AI 🌸

A Python-based desktop application that combines Generative AI and botanical classification. Input a flower description, generate a high-quality image, and automatically identify the species using the PlantNet API.

## Features
- **Generative Design:** Uses the GapGPT API to turn text prompts into flower images.
- **Botanical Identification:** Integrates the PlantNet API to classify the generated flowers.
- **Responsive GUI:** Built with PyQt6, featuring real-time status updates and error handling.
- **Clean Architecture:** Modular design separated into UI, API logic, and Application controller.

## Project Structure
- `main.py`: The application orchestrator. Handles user input, logic flow, and data parsing.
- `ui.py`: Contains the `FlowerUI` class, defining the PyQt6 interface layout.
- `api.py`: Manages network communications, image generation requests, and PlantNet API integration.

## Prerequisites
Ensure you have Python installed and the necessary libraries:
```bash
pip install PyQt6 requests
```
## Setup
Clone this repository.
* Set your API Keys as environment variables:
    * OPENAI_API_KEY (for GapGPT image generation)
    * PLANTNET_API_KEY (for identification)
* Run the application:
```
python main.py
```
## How It Works
1- Input: Type a description of a flower (e.g., “Orange lily with dark spots”).
2- Generate: The app sends the prompt to the GapGPT API, which generates an image and saves it locally.
3- Identify: The app sends the generated image file to the PlantNet API.
4- Result: The app parses the JSON response and displays the Scientific Name, Family, and Common Names directly in the UI.