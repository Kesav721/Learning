#Q Print the weekday of 15th August 2024

import calendar
weekday = calendar.weekday(2024, 8, 15)
days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
print("15th August 2024 is a", days[weekday])

