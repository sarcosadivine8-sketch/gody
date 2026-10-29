# Lab

**You will use the tilling_the_soil.py file to write your code.**

A local landscaping company has experienced an explosion in its lawn care business. The company needs your help to streamline their services, and would like you to develop a program to assist their field technicians in calculating quantities relevant to fertilizer applications: They need to know the number of bags of fertilizer needed, the cost of material and labor, and the environmental impact of each application.

Each technician will enter the rectangular dimensions (length and width, in feet) of four lawn areas: front, back and two sides. This is the most common configuration of houses having lawns in the city. It is possible that one or more of those lawn sections will be missing. In the case of missing lawn sections, the user enters dimensions of zero (0).

- Each bag of fertilizer purchased by the company can cover 2000 square feet.
- Each bag costs $27.
- The application of one bag deposits one pound of nitrogen and 0.125 pounds of potassium onto the ground.
- A technician can fertilize 2500 square feet in one hour.
- A technician is paid $20 per hour.

The program will ask for the width and length, in feet, of each of four rectangular lawn sections: front, rear, left, and right. It is possible that one or more of those sections are missing. Your program should calculate and report the following:

1. How many bags (whole numbers only) will be required to complete the application.
2. The cost of fertilizer.
3. The minimum number of hours to complete the job, in whole numbers (round up to the next hour using the `math.ceil()` method).
4. The cost of labor.
5. The total cost.
6. The amount of nitrogen and potassium applied to the soil.

All monetary values should be accompanied by a dollar sign ($) and carried to two decimal points. Application area, bag quantity, and labor hours should be whole numbers. Nitrogen and potassium quantities should be rounded to three decimal points. (Use actual values, not rounded values, of the number of bags of fertilizer used to calculate nitrogen and potassium application).

Click the terminal in the codespace and type `pytest` to test your code.

