# Weather App (PyQt6)

A simple desktop weather application built with **PyQt6** and **WeatherAPI**.

The application allows users to search for a city and view:

- Current weather condition
- Weather icon
- Wind speed (kph)
- Humidity (%)

---

## Features

- Modern PyQt6 GUI
- Search weather by city name
- Display live weather data from WeatherAPI
- Show weather condition icons
- Error handling for API/network issues
- Lightweight and easy to extend

---

## Project Structure

```text
weatherApp/
├── main.py
├── config.txt
├── requirements.txt
├── service/
│   └── weather_service.py
├── ui/
│   └── weather_ui.py
└── README.md
```

---

## Requirements

- Python 3.10+
- Internet connection
- WeatherAPI key

---

## Installation

Clone the repository:

```bash
git clone <repository-url>
cd weatherApp
```

Create and activate a virtual environment:

```bash
python -m venv venv

# Linux / macOS
source venv/bin/activate

# Windows
venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## API Key Configuration

Create a file named `config.txt` in the project root directory.

Add your WeatherAPI key on the first line:

```text
YOUR_API_KEY
```


You can obtain a free API key from:

https://www.weatherapi.com/

---

## Running the Application

```bash
python main.py
```

Enter a city name and click **Search** or press **Enter**.

---

## Example

Input:

```text
London
```

Output:


![image info](app.png)


```text
Condition: Partly Cloudy
Wind: 10.4 kph
Humidity: 58%
```

A weather icon will also be displayed in the application window.

---

## Technologies Used

- Python
- PyQt6
- Requests
- WeatherAPI

---

## Future Improvements

- Use QThread to prevent UI freezing during API requests
- Display temperature (°C / °F)
- Add weather forecast support
- Show pressure, visibility, and UV index
- Implement dark mode
- Cache downloaded weather icons
- Improve error handling and user feedback

---

## License

This project is intended for educational and learning purposes.