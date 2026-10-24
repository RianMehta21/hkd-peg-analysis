# Hong Kong Dollar Peg Analysis (2005-2025)

**Quantifying the resilience of the Linked Exchange Rate System (LERS) through 20 years including financial crises.**

## Executive Summary
This project analyzes the HKD/USD peg from **May 2005 to Present**, focusing on the "Convertibility Undertaking" (7.75 - 7.85 band). Using Python (Pandas/Matplotlib), I modeled the interaction between **Interest Rate Spreads**, **Capital Flows**, and **HKMA Intervention** over a dataset of 5,000+ trading days.

---

## 🔎 Statistical Analysis & Key Findings

### 1. Peg Stability Metrics (2005-2025)
* **Band Adherence:** The spot rate was strictly inside the 7.75-7.85 band for **91%** of all trading days, and the peg held throughout.
* **Days at a Convertibility Limit:** Recorded 303 days at or above 7.85 (5.94%) and 145 days at or below 7.75 (2.84%), about 9% at or past a limit.
* **Low Volatility:** Annualized volatility was **0.60%**, remarkably low compared to major floating currencies.
* **Precision:** The average deviation was only **0.033 HKD** from the peg center (7.80).

### 2. Monetary Policy Linkage
* **Policy Mirror:** A **0.94 correlation** between HIBOR and the Federal Funds Rate on levels is consistent with Hong Kong importing US monetary policy over long periods. On changes the correlation is only **-0.03** daily and **0.26** monthly, which means the two rates share the same long-run trend but HIBOR does not follow the Fed day to day and only catches up over months.
* **Spread Influence:** The interest rate spread shows a moderate positive correlation (**0.53**) with exchange rate movements.
* **Inverse Balance Relationship:** The Aggregate Balance is inversely correlated (**-0.71**) with Fed rates, confirming that the HKMA drains liquidity when US rates rise.

### 3. HKMA Intervention Scale
* **Liquidity Growth:** The Monetary Base expanded **14.1x** (1,309%) over the 20-year period.
* **Significant Activity:** Significant interventions (>$1 Billion HKD) occurred on **545 days** (10.7% of all days), averaging ~27 days per year.
* **Extreme Defenses:**
    * **Largest Drain:** -$29.6 Billion HKD (July 7, 2025).
    * **Largest Injection:** +$116.7 Billion HKD (May 7, 2025).

### 4. Crisis Window Comparison
* **2008 Financial Crisis:** Peg held perfectly (**0 days at a convertibility limit**), Volatility 0.55%.
* **2020 COVID Pandemic:** Peg held perfectly (**0 days at a convertibility limit**), Volatility 0.85%.
* **2019 HK Protests:** Recorded **31 days at a convertibility limit**, all before the June 9 anchor date, with a +48% volatility spike.
* **2022 Fed Rate Hikes:** Recorded **20 days at a convertibility limit** during aggressive tightening.

---

## Key Visualizations

### 1. Historical Exchange Rate Band Adherence
*Visualizes the spot rate relative to the 7.75-7.85 Convertibility Undertaking. While the rate was strictly inside the band for 91% of the period and at or past a convertibility limit on about 9%, the chart highlights distinct periods of pressure where the rate approached the weak-side limit (7.85) for extended durations.*
![Peg Stability Chart](images/1_peg_stability.png)

### 2. Interest Rate Spread Analysis
*Illustrates the relationship between the US-HK interest rate spread and exchange rate movements r=0.53. While the correlation is not visually noticeable, a positive spread (US rates exceeding HK rates) creates capital outflow pressure, pushing the spot rate toward the 7.85 weak-side limit, while negative spreads tend to strengthen the currency*
![Spread Correlation Chart](images/2_spread_correlation.png)

### 3. Aggregate Balance & Intervention Analysis
*When the rate goes toward the strong side (7.75), liquidity surges as the HKMA sells HKD (to buy USD) which can be seen around 2009-2010 and 2020-2021 with balances exceeding HK$400 billion. Conversely, liquidity drains during weak-side defense (2022-2024).*
![Intervention Chart](images/3_intervention_mechanic.png)

### 4. Interest Rate Transmission Mechanism
*The 0.94 correlation (on levels) is visually evident as HIBOR (blue) tracks Federal Funds Rate (orange) almost perfectly throughout the entire period. This tight relationship validates the linked exchange rate system's effectiveness in transmitting US monetary policy to Hong Kong.*
![HIBOR vs Fed Funds](images/4_rate_correlation.png)

---

## Methodology

### Data Preparation
1. Fetched historical data from HKMA API (2005-present)
2. Merged exchange rates, liquidity, and federal funds data by date
3. Applied forward-fill for missing Saturday HIBOR values
4. Validated data quality through outlier detection (3σ threshold)
5. Corrected data anomaly: September 19, 2019 HIBOR (199.286% → 1.98%)
6. Filtered data to May 18, 2005 onwards (introduction of current band)


### Feature Engineering
- **Spread**: Federal Funds Rate - HIBOR (interest rate differential)
- **Flow**: Daily change in aggregate balance (intervention proxy)
- **USD Change**: Daily percentage change in exchange rate
- **Volatility**: 30-day rolling standard deviation of exchange rate changes

### Data Sources:
* **HKMA Open API:** Daily Exchange Rates, HIBOR, Aggregate Balance.
* **Federal Reserve (FRED):** Effective Federal Funds Rate.

---

## 🛠️ Technologies Used
- **Python 3.10** - Core language
- **pandas** - Data manipulation and analysis
- **matplotlib** - Data visualization
- **numpy** - Statistical calculations

---

## How to Run

1.  **Clone the repository**
    ```bash
    git clone https://github.com/RianMehta21/hkd-peg-analysis.git
    cd hkd-peg-analysis
    ```

2.  **Install dependencies**
    ```bash
    pip install -r requirements.txt
    ```

3.  **Run data collection scripts**
    From the repo root, fetch the latest raw data from the HKMA API:
    ```bash
    python scripts/get_exchange_rates.py
    python scripts/get_liquidity.py
    ```

4.  **Run the analysis**
    * **Data Prep:** Run `notebooks/data_prep.ipynb` to process raw data into `data/master.csv`.
    * **Analysis:** Run `notebooks/analysis.ipynb` to generate charts and statistics.
---

## 📂 Project Structure
```text
hkd-peg-analysis/
│
├── data/                       # Raw CSVs and processed master dataset
├── images/                     # Saved visualization output
├── notebooks/
│   ├── data_prep.ipynb         # ETL and Data Cleaning pipeline
│   └── analysis.ipynb          # Statistical analysis and plotting
├── scripts/
│   ├── get_exchange_rates.py   # Utility script for HKMA API
│   └── get_liquidity.py        # Utility script for HKMA API
├── requirements.txt            # Python dependencies
└── readme.md                   # Project documentation
```