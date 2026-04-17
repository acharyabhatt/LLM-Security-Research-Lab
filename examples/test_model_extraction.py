from llm_security_lab import ModelExtractionDefense

defense = ModelExtractionDefense(max_requests=2)

for i in range(4):
    print(defense.track_request("user", "architecture?", ""))
