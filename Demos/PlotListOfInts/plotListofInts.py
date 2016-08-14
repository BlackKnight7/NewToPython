# plot list of ints
import matplotlib.pyplot as pylab

listOfInts = []
for counter in range(10):
    listOfInts.append(counter * 2)

print listOfInts
print len(listOfInts)

# now plot the list
pylab.plot(listOfInts)
pylab.show()
