import firebase_admin
from firebase_admin import credentials, db
import csv

# Initialize Firebase
cred = credentials.Certificate("C:/Users/SHIVANSH/Downloads/data-capture-9c140-firebase-adminsdk-fw4gn-98fb10dabc.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://data-capture-9c140-default-rtdb.firebaseio.com/gyroscope_data'
})

# Query Firebase data
ref = db.reference('/gyroscope_data')
data = ref.get()

# Check if data was retrieved
if data:
    print("Data retrieved from Firebase:")
    print(data)

    # Save to CSV
    with open('gyroscope_data.csv', mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['timestamp', 'x', 'y', 'z'])  # CSV headers

        for key, value in data.items():
            writer.writerow([value['timestamp'], value['x'], value['y'], value['z']])
    
    print("Data has been successfully written to gyroscope_data.csv.")
else:
    print("No data retrieved from Firebase.")
