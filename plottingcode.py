data= """60668	110701	113857
43879	59118	57847
19067	30063	40485"""

int_data =[i.split("\t") for i in data.split("\n")]

##https://data.gov.in/sites/default/files/datafile/enrolment02_1.xls
print(int_data)
int_data = [[int(i) for i in j ]for j in int_data ]

int_data

labels = """Primary
Middle
Secondary""".split("\n")

labels
int_data = np.array(int_data)

barWidth = 0.2
fig = plt.subplots(figsize =(12, 8)) 
   
# set height of bar 
Primary = int_data[:3,0]
Middle = int_data[:3,1]
Secondary = int_data[:3,2] 

# Set position of bar on X axis 
br1 = np.arange(3) 
br2 = [x + barWidth for x in br1] 
br3 = [x + barWidth for x in br2] 
br4 = [x + barWidth for x in br3] 
   
# Make the plot 
plt.bar(br1, Primary, color ='r', width = barWidth, 
        edgecolor ='grey', label ='Primary') 
plt.bar(br2, Middle, color ='g', width = barWidth, 
        edgecolor ='grey', label ='Middle') 
plt.bar(br3, Secondary, color ='b', width = barWidth, 
        edgecolor ='grey', label ='Secondary') 
   
# Adding Xticks  
plt.xlabel('Level', fontweight ='bold') 
plt.ylabel('Enrollment (all figures in \'000)', fontweight ='bold') 
plt.xticks([r + barWidth for r in range(len(Primary))], 
           ['Primary', 'Middle', 'Secondary']) 
plt.legend(['1995-1996', '2007-2008', '2009-2010'])
  
plt.show()

#https://data.gov.in/sites/default/files/GDP_and_growth_rate_curr-04-05.csv


per_capita_income = "21763	24143	27131	31206	35825	40775	46249	54021	61855	67839	74380".split("\t")
pci = [int(i) for i in per_capita_income]

gdp = "2625819\t2971465	3390503	3953276	4582086	5303566	6108903	7248860	8391691	9388876	10472807".split("\t")
gdp = [int(i) for i in gdp]
print(len(gdp))

years = "2004	2005	2006	2007	2008	2009	2010	2011	2012	2013	2014".split("\t")

years = [int(i) for i in years]

# plt.scatter(years, pci)
# plt.scatter(years, gdp)
# plt.xlabel("Years")
# plt.ylabel("Per Capita Income")

fig, ax1 = plt.subplots()

color = 'tab:red'
ax1.set_xlabel('time (s)')
ax1.set_ylabel('Per Capita Income', color=color)
ax1.scatter(years, pci, color=color)
ax1.tick_params(axis='y', labelcolor=color)

ax2 = ax1.twinx()  # instantiate a second axes that shares the same x-axis

color = 'tab:blue'
ax2.set_ylabel('GDP', color=color)  # we already handled the x-label with ax1
ax2.scatter(years, gdp, color=color)
ax2.tick_params(axis='y', labelcolor=color)

plt.title('Relation of GDP with Per Capita Income')
fig.tight_layout()  # otherwise the right y-label is slightly clipped
plt.show()

gdp = """6.4	-1.7	8.9	-5.5	2.3	18.9	2.9	11.3	5.2	9.1	5.9	7.4	14.9	16.5	5.5	13.1	17.1	6	10.1	6.8	7.1	10.2	21.8	18.3	7.7""".split("\t")

gdp = [float(i) for i in gdp]

gdp_list = [gdp[i:i+5] for i in range(0, len(gdp), 5)]

fig = plt.figure(figsize =(10, 7)) 
ax = fig.add_subplot(111) 

# Creating axes instance 
bp = ax.boxplot(gdp_list, patch_artist = True, vert = 1, labels = ["1951-1955", "1955-1960", "1960 - 1965", "1965-1970", " 1970-1975"]) 

plt.xlabel("Duaration in Years (In groups of 5)")
plt.ylabel("GDP Growth Rate(in %)")
