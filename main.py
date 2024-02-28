seconds = int(input('Enter the number of seconds (integer): '))

#original
# minutes = seconds // 60
# seconds -= minutes * 60
# hours = minutes // 60
# minutes -= hours * 60


minutes, seconds = divmod(seconds, 60)
hours, minutes = divmod(minutes, 60)
# e.g. The duration is X hours, X minutes, and X seconds.
print(f"The duration is {hours} hours, {minutes} minutes, and {seconds} seconds.")