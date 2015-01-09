import ghfunctions as gh

profiles = gh.loadProfile()

while True:
    gh.saveProfile(profiles)
