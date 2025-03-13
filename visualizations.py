import matplotlib.pyplot as plt
import seaborn as sns

def plot_shot_efficiency(df):
    
    if 'Distance' not in df.columns:
        print("Warning: 'Distance' column is missing.")
        return

    
    total_shots = df['Goal'].count()
    total_goals = df['Goal'].sum()
    shooting_efficiency = (total_goals / total_shots) * 100

    print(f"Total shots: {total_shots}")
    print(f"Total goals: {total_goals}")
    print(f"Shooting efficiency: {shooting_efficiency:.2f}%")
    
    
    sns.barplot(x=df['Distance'].unique(), y=df.groupby('Distance')['Goal'].mean() * 100)
    plt.xlabel('Shot Distance')
    plt.ylabel('Shot Efficiency (%)')
    plt.title('Shot Efficiency by Distance')
    plt.show()
