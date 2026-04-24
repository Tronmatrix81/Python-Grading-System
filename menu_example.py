from pick import pick
from extras import menuOptions

title = "UACH Grading System"
indicator = "=>"
option, index = pick(menuOptions, title, indicator)
print(option)
print(index)