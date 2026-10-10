"""
Take a number of seconds, for example 3725, and print it as hours, minutes, and seconds. For 3725 the answer is 1 hour, 2 minutes, 5 seconds.
"""
total_seconds=int(input("Enter total number of seconds to see time in hours min seconds : "))
seconds=total_seconds % 60
total_minutes=total_seconds - seconds
total_hour=total_minutes//60
minutes=total_hour % 60
hour=(total_hour-minutes)//60

print(f"Hour:{hour},Minutes:{minutes},Seconds:{seconds}")