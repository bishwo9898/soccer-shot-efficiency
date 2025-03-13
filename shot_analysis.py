def shot_efficiency(df):
    print("Columns in DataFrame:", df.columns)  

    total_shots = len(df)
    total_goals = df['Goal'].sum()
    efficiency = (total_goals / total_shots) * 100
    
    print(f"Total shots: {total_shots}")
    print(f"Total goals: {total_goals}")
    print(f"Shooting efficiency: {efficiency:.2f}%")
    
    
    if 'ShotDistance' in df.columns:  
        distance_efficiency = df.groupby('ShotDistance')['Goal'].mean() * 100
        print("\nShot efficiency by distance:")
        print(distance_efficiency)
    else:
        print("\nWarning: 'ShotDistance' column is missing.")

    
    print("\nNo angle data available to analyze.")
