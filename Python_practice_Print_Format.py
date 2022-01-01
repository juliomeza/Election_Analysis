candidate_votes = 3345
total_votes = 23123

message_to_candidate = (
    f"You received {candidate_votes} number of votes.\n"
    f"The total number of votes in the election was {total_votes}.\n"
    f"You received {candidate_votes / total_votes * 100}% of the total votes.\n")
print(message_to_candidate)

# Format Floating Point Decimals
message_to_candidate = (
    f"You received {candidate_votes:,} number of votes.\n"
    f"The total number of votes in the election was {total_votes:,}.\n"
    f"You received {candidate_votes / total_votes * 100:.2f}% of the total votes.\n")
print(message_to_candidate)