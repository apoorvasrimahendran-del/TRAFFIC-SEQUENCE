# 🚦 Traffic Light Sequence using Arduino Uno
A traffic light sequence project built using Arduino Uno and C/C++-based programming. It controls red, yellow, and green LEDs connected to digital pins 5, 6, and 7, using timed delays to simulate traffic signal operation. This project helped me explore LED interfacing and the fundamentals of embedded systems.

## 🛠️ Components Used
- Arduino Uno
- Red LED
- Yellow LED
- Green LED
- Resistors
- Breadboard
- Jumper Wires

## 🔌 Pin Connections

| LED | Arduino Pin |
|---|---|
| Red LED | 5 |
| Yellow LED | 6 |
| Green LED | 7 |

## ⚙️ Working Sequence
1. Red LED turns ON for 3 seconds.
2. Yellow LED turns ON for 1 second.
3. Green LED turns ON for 3 seconds.
4. The sequence repeats continuously.

## 💻 Programming Language
- Arduino (C/C++-based)

## 📚 Concepts Used
- `pinMode()`
- `digitalWrite()`
- `delay()`
- Digital output control
- LED interfacing

## 📂 Project Structure
```text
traffic-light-sequence/
├── traffic_light.ino
└── README.md
```

## 🚀 Future Improvements
- Add a pedestrian crossing signal.
- Implement a countdown timer.
- Simulate a more realistic traffic signal.

## ✅ Project Status
Completed

[View Arduino Code](trafficlight.ino)

![Traffic Light Output](Traffic%20Light%20Output.jpeg)
