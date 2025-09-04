# CROP-FERTILIZER-RECOMMENDER
# 🌾 Crop & Fertilizer Recommendation System  

## 📌 Overview  
This project is a **Machine Learning + Web App** solution that helps farmers and agricultural enthusiasts determine:  
- ✅ The **most suitable crop** based on soil nutrients & weather conditions  
- ✅ The **right fertilizer suggestions** (based on nutrient balance)  
- ✅ Interactive **charts & visualizations** for soil composition and environment  

The frontend is built with **Streamlit**, an intuitive UI.  

---

## 🛠️ Tech Stack  
- **Python 3.9+**  
- **Pandas, NumPy** – Data wrangling  
- **Scikit-learn** – Random Forest model for crop prediction  
- **Joblib** – Model persistence  
- **Streamlit** – Interactive web interface  
- **Matplotlib / Plotly** – Data visualization  

---

## 📂 Project Structure  
```bash
Crop-Fertilizer-Recommender/
│
│── app/
│   ├── _pycache                       # cache file
│   ├── fertilizer_rules.py            # Avg NPK targets per crop
│   └── streamlit_app.py               # Main Web App (with theme + charts)
│
│── data/
│   └── crop_recommendation.csv        # Dataset
│
│── models/
│   ├── crop_model.joblib              # Trained model
│   ├── crop_targets.json              # Avg NPK targets per crop
│   └── training_report.txt            # Training evaluation
│
│── notebooks/                         # (optional) Jupyter experiments
│    └── run.txt                       # Important notes And instructions    
│── train_crop_model.py                # Script to train & save model      
│── requirements.txt                   # Python dependencies
│── README.md                          # Documentation

```

---

## 📊 Dataset  
The dataset (`crop_recommendation.csv`) contains:  
- **N** → Nitrogen content in soil  
- **P** → Phosphorus content in soil  
- **K** → Potassium content in soil  
- **temperature** → Temperature (°C)  
- **humidity** → Relative humidity (%)  
- **ph** → Soil pH value  
- **rainfall** → Rainfall (mm)  
- **label** → Recommended crop  

---

## 🚀 Setup & Installation  

### 1️⃣ Clone the Repository  
```bash
git clone https://github.com/Aayush-Raj-Singh/crop-fertilizer-recommender.git
cd crop-fertilizer-recommender
```

### 2️⃣ Create a Virtual Environment  
```bash
python -m venv venv
source venv/bin/activate     # Mac/Linux
venv\Scripts\activate        # Windows
```

### 3️⃣ Install Dependencies  
```bash
pip install -r requirements.txt
```

### 4️⃣ Train the Model (Optional if already trained)  
```bash
python train_crop_model.py
```

### 5️⃣ Run the Web App  
```bash
streamlit run streamlit_app.py
```

---

## 🌟 Features  
- 🔮 **Crop Prediction**: Suggests the best crop based on soil & climate.  
- 🧪 **Fertilizer Recommendation**: Advises on nutrient needs (N, P, K).  
- 📊 **Interactive Charts**:  
  - Soil nutrients bar chart  
  - Rainfall & humidity gauges  
  - Comparison with ideal crop requirements  
- 🎨 **UI Enhancements**:  
  - Clean card-based layout  
  - Light/Dark theme toggle  

---

## 📈 Model Performance  
- **Algorithm**: Random Forest Classifier  
- **Accuracy**: ~97% (depending on dataset split)  
- **Evaluation**: Stored in `models/training_report.txt`  

---

## 🔮 Future Improvements  
- Integrate **real-time weather API**  
- Add **GPS-based soil mapping**  
- Deploy on **Streamlit Cloud / HuggingFace / Heroku**  
- Mobile-friendly UI  

---

## 👨‍💻 Author  
Developed by **[Aayush-Raj-Singh]** ✨  
🔗 GitHub: [Aayush-Raj-Singh](https://github.com/Aayush-Raj-Singh)  

---

## 📜 License  
This project is licensed under the **MIT License** – free to use and modify.  
