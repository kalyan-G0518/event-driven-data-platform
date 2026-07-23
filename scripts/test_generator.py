from src.ingestion.simulator.generator import generate_session

for event in generate_session(user_id=1):
    print(event.model_dump_json(indent=2))