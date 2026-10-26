# A company has 100 employees:

# 	          Remote	Office	Total
# Developers	30	      20	50
# Designers	    10	      40	50
# Total	        40	      60	100

# Calculate:

# \(P(Developer)\)
# \(P(Remote)\)
# \(P(Developer \cap Remote)\)
# \(P(Developer \mid Remote)\)
# P(Remote∣Developer)



total = 100

developers = 50
remote = 40
developer_remote = 30

# 1. P(Developer)
p_developer = developers / total

# 2. P(Remote)
p_remote = remote / total

# 3. P(Developer ∩ Remote)
p_developer_remote = developer_remote / total

# 4. P(Developer | Remote)
p_developer_given_remote = developer_remote / remote

# 5. P(Remote | Developer)
p_remote_given_developer = developer_remote / developers

print("P(Developer):", p_developer)
print("P(Remote):", p_remote)
print("P(Developer ∩ Remote):", p_developer_remote)
print("P(Developer | Remote):", p_developer_given_remote)
print("P(Remote | Developer):", p_remote_given_developer)