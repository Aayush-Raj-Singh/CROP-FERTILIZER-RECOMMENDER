# ✅ Fertilizer recommendation function
def recommend_fertilizer(crop_name, N, P, K):
    # Example nutrient requirements for crops (values can be adjusted/tuned)
    crop_requirements = {
        "rice":  {"N": 90, "P": 40, "K": 40},
        "wheat": {"N": 80, "P": 35, "K": 35},
        "maize": {"N": 85, "P": 40, "K": 40},
        "mango": {"N": 50, "P": 30, "K": 30},
        "cotton": {"N": 75, "P": 30, "K": 35},
        "sugarcane": {"N": 120, "P": 50, "K": 60},
        # 👉 add more crops as needed
    }

    if crop_name not in crop_requirements:
        return "No fertilizer data available for this crop."

    # Target values for the crop
    req = crop_requirements[crop_name]

    # Differences between required and current
    n_diff = req["N"] - N
    p_diff = req["P"] - P
    k_diff = req["K"] - K

    recommendations = []

    if n_diff > 0:
        recommendations.append(f"Add {n_diff} units of Nitrogen (N)")
    if p_diff > 0:
        recommendations.append(f"Add {p_diff} units of Phosphorus (P)")
    if k_diff > 0:
        recommendations.append(f"Add {k_diff} units of Potassium (K)")

    if not recommendations:
        return "Your soil already has sufficient nutrients for this crop ✅"
    else:
        return "; ".join(recommendations)
