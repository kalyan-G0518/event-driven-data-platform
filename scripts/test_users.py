from src.ingestion.simulator.users import generate_user

for i in range(5):
    print(generate_user(i + 1))