# Website Traffic Analysis & Prediction

This project demonstrates **synthetic website traffic analysis** and **short-term prediction** using Python.  
It shows how to visualize traffic trends, detect spikes, and predict future traffic using a simple Linear Regression model.

> **Note:** All data is synthetic, generated for learning and demonstration purposes.

---

## **Project Structure**

- `generate_data.py` : Generates synthetic traffic data per minute with random spikes.
- `analysis.py` : Plots traffic over time to visualize trends.
- `new_analysis.py` : Detects spikes in traffic using statistical thresholds.
- `pred_analysis.py` : Predicts future traffic and potential spikes using Linear Regression.
- `traffic_data.csv` : Sample generated dataset (can be created using `generate_data.py`).
- `requirements.txt` : Python libraries needed to run the project.

---

## **How to Run**

1️⃣ **Install dependencies:**

```bash
pip install -r requirements.txt
```
2️⃣ **Generate synthetic traffic data:**
This will create traffic_data.csv.
```bash
python generate_data.py
```
3️⃣ **Run analysis scripts:**
```bash 
python analysis.py
python new_analysis.py
python pred_analysis.py
```


## License

This project is open-source and free to use for learning purposes.



