# ✈️ Beyond Duration: What Really Drives Airline Prices?

## 📌 Project Overview  
This project explores a **simulated (but realistic) airline dataset** designed to uncover what *actually* drives flight prices.  
While many assume **flight duration** is the dominant pricing factor, this analysis reveals a deeper truth:  

👉 **the number of stops often explains price differences more strongly than duration alone**.

Using Python-based exploratory data analysis and visualization, the project demonstrates how **challenging surface-level assumptions** leads to more actionable insights.

---

## 🎯 Key Questions Explored
- Does longer flight duration always mean higher prices?
- How strongly do **stops** influence ticket pricing?
- What happens when duration, stops, and price interact together?

---

## 🧠 Core Insight 
At first glance, you might expect:
> **Price ↔ Duration** to be the strongest relationship.

However, once durations are properly normalized, the data shows:
- **Price ↔ Stops** → consistently strong correlation  
- **Duration ↔ Stops** → structural relationship  
- **Price ↔ Duration** → weaker relationship than intuition suggests  

---

## 🔧 What the Code Does (Overview)
### 1. Data Preparation
- Reads a realistic airline dataset with prices in USD  
- Parses dates, times, and categorical fields  
- Converts complex duration strings (`1d 2h 30m`) into **numeric hours**

### 2. Feature Creation
- Transforms `Total_Stops` into numeric form  
- Extracts:
  - Month & weekday  
  - Departure and arrival hours  
- Renames key analytical fields for clarity:
  - `Price_USD`  
  - `Duration_in_Hours`

### 3. Correlation Analysis
- Heatmaps of numeric variables **before and after feature creation**  

### 4. Visual Storytelling
- Scatter plots of **Price vs Duration**  
- Faceted by airline  
- Colored by number of stops  
➡️ making hidden patterns immediately visible

---

## 📊 Visuals That Matter
- **Correlation Heatmaps**  
  Reveal how relationships evolve after transforming raw data.
- **Airline-Level Scatter Plots**  
  Show how pricing strategies differ even for similar durations — once stops are considered.

---

## 🚀 Why does all of this matters?
This project demonstrates:

- Why **EDA beats assumptions**  
- How **feature generation changes conclusions**  
- The importance of questioning “obvious” relationships  
- How to turn raw operational data into strategic insight  

## 🧩 Tech Stack
- Python  
- Pandas & NumPy  
- Matplotlib & Seaborn  
- Exploratory Data Analysis (EDA)

## 🏁 Final Takeaway
> **Good analysis challenge intuition.**

This dataset teaches us that pricing in aviation (at least based on this sample dataset) is more related to how many times you stop during your trip than the total duration of it. 
This contradicts basic intuition, which highlights the importance of deeper analysis to really uncover hidden patterns.


