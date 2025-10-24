@echo off
echo Starting AR Greeting Card Server...
echo.
echo Current directory: %CD%
echo Files in directory:
dir /b *.html
echo.
echo Starting server on port 8000...
echo.
echo Access URLs:
echo - AR Marker: http://localhost:8000/ar-marker.html
echo - AR Greeting Card: http://localhost:8000/ar-greeting-card.html
echo.
echo Press Ctrl+C to stop the server
echo.
python -m http.server 8000
