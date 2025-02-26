# Exercise 4
## 4.1
### Imagine there is a new engineering building on Ucalgary campus (“Engineering Y”). You enter the building on the ground floor and you need to attend a lab in EY128. As you enter, you find the sign below: 
### (Image from lab02.pdf, pg. 16)
![alt text](image-2.png)

## 4.2
### The floorplan of the first floor is described in the below:
### (Image from lab02.pdf, pg. 17)
![alt text](image-1.png)

## 4.3
### 1. Describe the algorithm you will use to find the room. Assume all the information you have is the one given by the sign; you have no knowledge of the floor plan.
#### Check which room the right side ends with (EY138). Note that the starting room of the left side which was shown to be EY100 via the sign. Distinguish that EY128 is closer to EY138 than EY100. Enter through the right side. Iterate through each room (in this case backwards) until EY128 is found. Attend the lab.

### 2. How many ”steps” it will take to find room EY128? And what is a “step” in this case.
#### It would take a total of 6 steps. In this case, a "step" would be considered to be the amount of tasks carried out until I am officially attending the lab.

### 3. Is this a best-case scenario, worst-case scenario, or neither?
#### This is neither. This would be considered an average-case scenario.

### 4. With this particular sign and floor layout, explain what a worst-case or best-case scenario would look like.
#### The best case scenario is that the left side starts with EY128. The reason it would be best for it to be on the left side instead of the right, is that the sign tells us the exact room that the left side starts with, whereas if the right side ended with EY128, we'd still have to go physically check what room it is since it wasn't specified directly by the sign. The worst case scenario would be that EY128 is dead centre of both sides.

### 5. Suppose after a few weeks in the term you amemorize the layout of the floor. How would you improve the algorithm to make it more efficient?
#### Enter through the right side. Locate EY128. Attend the lab.