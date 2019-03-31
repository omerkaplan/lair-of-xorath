import datetime


# global variables that are shared across all implementations and not module specific

game_version = "1.1" # game version

done = False #done governs the span of the session. True is game over

xorath_is_dead = False # for end of game checks

# player initial position on map (assuming 7x7 grid)

col = 3
row = 0

# session stats

session_start_time = datetime.datetime.now()
session_end_time = datetime.datetime.now()
session_duration = session_end_time-session_start_time
rooms_visited = 0
monsters_killed = 0
monsters_avoided = 0
traps_disarmed = 0
traps_triggered = 0
times_rested = 0
loot_found = 0
cheats_used = "No"
