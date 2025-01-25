import pandas as pd
import matplotlib.pyplot as plt

# Load data
df = pd.read_csv("ESBL_cases.csv", parse_dates=["Statistikdatum"], encoding="latin-1")

# Data cleaning
# Handle age (convert 95+ to 95 and make numeric)
df["Ålder"] = df["Ålder"].replace("95+", "95").astype(float)

# Clean pathogen names and split multi-pathogen entries
df["Smittämne"] = df["Smittämne"].str.replace("_x000D_<br>", "").str.strip()
df["Smittämne"] = df["Smittämne"].str.split(",")

# Convert ESBL columns to binary (1 for positive, 0 otherwise)
esbl_cols = ["ESBL-A", "ESBL-CARBA", "ESBL-M"]
for col in esbl_cols:
    df[col] = df[col].apply(lambda x: 1 if str(x).lower() == "positiv" else 0)

# Create visualization
plt.figure(figsize=(16, 20))
plt.suptitle("ESBL Case Analysis", y=1.02, fontsize=16)

# Plot 1: Cases over time
plt.subplot(4, 2, 1)
daily_cases = df.resample("D", on="Statistikdatum").size()
daily_cases.plot(title="Daily Reported Cases", color="#2c7fb8")
plt.ylabel("Number of Cases")
plt.grid(True, alpha=0.3)

# Plot 2: Age distribution
plt.subplot(4, 2, 2)
bins = [0, 18, 50, 70, 100]
labels = ["0-18", "19-50", "51-70", "71+"]
df["Age Group"] = pd.cut(df["Ålder"], bins=bins, labels=labels)
age_dist = df["Age Group"].value_counts().sort_index()
age_dist.plot(kind="bar", color="#7fcdbb", title="Age Distribution")
plt.ylabel("Number of Cases")

# Plot 3: Gender distribution
plt.subplot(4, 2, 3)
gender_dist = df["Juridiskt kön"].value_counts()
gender_dist.plot(
    kind="pie",
    autopct="%1.1f%%",
    colors=["#fdae6b", "#3182bd"],
    title="Gender Distribution",
)

# Plot 4: Top pathogens
plt.subplot(4, 2, 4)
top_pathogens = df["Smittämne"].value_counts().head(5)
top_pathogens.plot(kind="barh", color="#31a354", title="Top 5 Pathogens")
plt.xlabel("Number of Cases")

# Plot 5: ESBL positivity
plt.subplot(4, 2, 5)
esbl_positivity = df[esbl_cols].sum()
esbl_positivity.plot(
    kind="bar", color=["#e6550d", "#756bb1", "#9ecae1"], title="ESBL Type Positivity"
)
plt.ylabel("Positive Cases")

# Plot 6: SME distribution
plt.subplot(4, 2, 6)
top_sme = df["Statistikgrundande SME"].value_counts().head(10)
top_sme.plot(kind="bar", color="#6baed6", title="Top 10 SME Categories")
plt.ylabel("Number of Cases")

# Plot 7: Resistance over time
plt.subplot(4, 2, 7)
carba_cases = df[df["ESBL-CARBA"] == 1].resample("D", on="Statistikdatum").size()
carba_cases.plot(color="#d94801", title="ESBL-CARBA Cases Over Time")
plt.ylabel("Number of Cases")
plt.grid(True, alpha=0.3)

plt.tight_layout()
plt.show()
