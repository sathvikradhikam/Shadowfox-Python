# Initial list of Justice League members
justice_league = ["Superman", "Batman", "Wonder Woman", "Flash", "Aquaman", "Green Lantern"]

# 1. Calculate the number of members in the Justice League
num_members = len(justice_league)
print("Number of members in the Justice League:", num_members)

# 2. Add Batgirl and Nightwing to the list
justice_league.append("Batgirl")
justice_league.append("Nightwing")
print("After adding Batgirl and Nightwing:", justice_league)

# 3. Move Wonder Woman to the beginning of the list
justice_league.remove("Wonder Woman")  # Remove Wonder Woman from her current position
justice_league.insert(0, "Wonder Woman")  # Insert her at the beginning
print("After moving Wonder Woman to the beginning:", justice_league)

# 4. Move either "Green Lantern" or "Superman" between Aquaman and Flash
# Let's choose "Green Lantern"
justice_league.remove("Green Lantern")  # Remove Green Lantern from his current position
# Find the index of Aquaman and insert Green Lantern after him
aquaman_index = justice_league.index("Aquaman")
justice_league.insert(aquaman_index + 1, "Green Lantern")
print("After moving Green Lantern between Aquaman and Flash:", justice_league)

# 5. Replace the existing list with new members
justice_league = ["Cyborg", "Shazam", "Hawkgirl", "Martian Manhunter", "Green Arrow"]
print("After replacing with new members:", justice_league)

# 6. Sort the Justice League alphabetically
justice_league.sort()
print("After sorting alphabetically:", justice_league)

# The hero at the 0th index will become the new leader
new_leader = justice_league[0]
print("The new leader of the Justice League is:", new_leader)

# BONUS: Predicting the new leader
# The new leader will be the first member in the sorted list