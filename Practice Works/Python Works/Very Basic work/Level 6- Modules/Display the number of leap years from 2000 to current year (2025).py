#Q Display the number of leap years from 2000 to current year (2025)

import calendar
leap_years = [year for year in range(2000, 2026) if calendar.isleap(year)]
print("Leap years from 2000 to 2025:", leap_years)
print("Number of leap years:", len(leap_years))
