import random
import pandas as pd

def generate_match_data(num_shots=50):
    
    data = {
        'Shot ID': [i+1 for i in range(num_shots)],
        'Player': [f'Player {random.randint(1, 5)}' for _ in range(num_shots)],
        'Goal': [random.randint(0, 1) for _ in range(num_shots)],
        'Shot Type': [random.choice(['Foot', 'Header']) for _ in range(num_shots)],
        'Distance': [random.randint(5, 30) for _ in range(num_shots)],  
    }
    
    
    df = pd.DataFrame(data)
    
    
    df.to_csv('match_data.csv', index=False)
    print("Data saved as 'match_data.csv'")

def save_data():
    generate_match_data()  
