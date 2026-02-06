AI-Powered FinOps Cost Anomaly Detection

Problem  
Startups often realize too late that their spending is increasing and their runway is shrinking.
Cloud costs, SaaS tools, and marketing spend can quietly grow month by month without clear warnings.

Founders need an early signal when spending becomes unusual — before it becomes dangerous.

Solution  
This project builds an AI-powered FinOps system that learns normal startup spending behavior
and automatically detects unusual cost anomalies.

Instead of just showing numbers, the system explains why a cost spike happened in clear,
human-readable language.

Features  
- Monthly burn rate calculation  
- Cost trend visualization  
- Automatic cost anomaly detection  
- Plain-English AI explanations for spending spikes  

How It Works  
- Load monthly startup expense data  
- Learn normal spending patterns  
- Detect unusually high cost months  
- Explain anomalies using recent history  

Tech Stack  
- Python  
- pandas  
- matplotlib  

Example Insight  
In 2023-04, total costs increased by 67.6% compared to the previous 3-month average.

This helps founders understand spending changes without digging through raw numbers.

How to Run  
- Clone the repository  
- Keep `startup_costs.csv` in the same folder  
- Run:  
  python finops_step2.py
