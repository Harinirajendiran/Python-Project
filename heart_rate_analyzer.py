#sample heart rate data(beats per  mminute)
heart_rates=[40,32,80,62,100,150,200,72,95]
#step 1:basic statistics
avg_rate=sum(heart_rates)/len(heart_rates)
print("Heart Rate Report")
print(".................................")
print("average HR:",round(avg_rate,2),"bpm")
print("Max HR:",max(heart_rates),"bpm")
print("Min HR:",min(heart_rates),"bpm")

#step 2:classification
print("\nclassification of reading:")
for rate in heart_rates:
    if rate < 60:
        print(rate,"->Bradycardia(low)")
    elif rate > 100:
        print(rate,"->Trachycardia(high)")
    else:
        print(rate,"->Normal")

#step 3: summary
high=len([rate for rate in heart_rates if rate > 100])
low=len([rate for rate in heart_rates if rate < 60])
normal=len(heart_rates)-high-low

print("\nsummary:")
print("Normal raeding:",normal)
print("High reading:",high)
print("Low reading:",low)