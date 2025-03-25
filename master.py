Total = 10000
Effort = input("Enter daily effort ") 
Effort = int(Effort)


Days = Total // Effort
Hours = Total % Effort
Months = Days // 30
Days = Days % 30
Years = Months // 12 
Months = Months % 12

print(Years, "years", Months, "months", Days, "days", Hours, "hours")
