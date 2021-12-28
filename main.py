import csv
import plotly.express as px

rows = []
with open("main.csv", "r") as f:
  csv_reader = csv.reader(f)
  for row in csv_reader:
    rows.append(row)

headers = rows[0]
star_data_rows = rows[1:]

headers[0] = "Row_Number"

#print(headers)
#print(star_data_rows[0])

temp_stars_data_rows = list(star_data_rows)

for star_data in temp_stars_data_rows:
    star_mass = star_data[3]
    if star_mass.lower() == "?":
        star_data_rows.remove(star_data)
        continue
    else:
        if (star_mass.find(' ')!=-1):
            star_mass_value = star_mass.split(" ")[0]
        elif (star_mass.find('-')!=-1):
            star_mass_value = star_mass.split("-")[0]
        elif (star_mass.find('<')!=-1):
            star_mass_value = star_mass.split("<")[1]
        else:
            star_mass_value = star_mass

        star_mass_value = float(star_mass_value) * 1.989e+30
        star_data[3] = star_mass_value

    star_radius = star_data[4]
    if star_radius.lower() == "?":
        star_data_rows.remove(star_data)
        continue
    else:
        if (star_radius.find(' ')!=-1):
            star_radius_value = star_radius.split(" ")[0]
        elif (star_radius.find('-')!=-1):
            star_radius_value = star_radius.split("-")[0]
        else:
            star_radius_value = star_radius

        if (star_radius_value.find(',')!=-1):
            star_radius_num1 = star_radius_value.split(",")[0]
            star_radius_num2 = star_radius_value.split(",")[1]
            star_radius_value = float(str(int(star_radius_num1)) + str(int(star_radius_num2)))

        star_radius_value = float(star_radius_value) * 6.957e+8
        star_data[4] = star_radius_value

#print(len(star_data_rows))
#with open("main_v2.csv", "a+") as f:
#    csv_writer = csv.writer(f)
#    csv_writer.writerow(headers)
#    csv_writer.writerows(star_data_rows)

star_masses = []
star_radiuses = []
star_names = []
for star_data in star_data_rows:
  star_masses.append(star_data[3])
  star_radiuses.append(star_data[4])
  star_names.append(star_data[1])

star_gravity = []
for index, name in enumerate(star_names):
    gravity = (float(star_masses[index])) / (float(star_radiuses[index]) * float(star_radiuses[index])) * 6.674e-11
    star_gravity.append(gravity)

print(star_names[0], star_gravity[0])
# Sun is correct as it's about 274
print(star_names[2], star_gravity[2])
# Canopus is not correct as it's about 0.4365 and we got 0.8161
print(star_names[4], star_gravity[4])
# Arcturus is close as it's about 0.4463 and we got 0.4571
print(star_names[5], star_gravity[5])
# Vega is not correct as it's about 0.041 and we got 82.77
print(star_names[9], star_gravity[9])
# Betelgeuse is not correct as it's about 0.003162 and we got 0.006078

# Most of the star's gravity we calculated are not correct

fig = px.scatter(x=star_radiuses, y=star_masses, size=star_gravity, hover_data=[star_names])
fig.show()
