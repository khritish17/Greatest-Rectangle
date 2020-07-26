import numpy as np

print("The Rectangle provided is of 500x100000 Dimension")
N=int(input("Insert the number of points you want use:"))

points=np.ndarray((N,2)).astype(int) # Points is a 2D array which stores the cordinates of the inserted array; points[x][y]

# Scaning the value from the user 
for i in range(N):
    # First we take the X value
    points[i][0]=int(input("Enter the X value in (X,Y):"))
    # Second we take the Y value
    points[i][1]=int(input("Enter the Y value in (X,Y):"))
# Scanning Complete :D

# Now we sort the points array wrt Y
points_sorted_Y=points[points[:,1].argsort()]

# And also we sort the points array wrt X
points_sorted_X=points[points[:,0].argsort()]

# We will use the above sorted arrays wrt X and Y , very soon in the program



# This functions returns the area of the rectangle whose coordinates are x1,x2,y1,y2: (x2-x1)*(y2-y1)
def compute_area(x1,x2,y1,y2):
    return (abs(x2-x1))*(abs(y2-y1))

# Now we will use the Technique: Sky is the Limit, refer what is "sky is the limit" in pdf
rectangle_x1=0  # These is the x1 cordinates of the test rectangle 
rectangle_x2=0  # These is the x2 cordinates of the test rectangle
rectangle_y1=0  # These is the y1 cordinates of the test rectangle which is always 0, since the rectangle should have the base on x axis
rectangle_y2=0  # These is the y2 cordinates of the test rectangle

max_area=0      # Here we save the maximum area obtained from the test rectangle
best_x1=0       # This is the x1 cordinate od the test rectangle for which we get the max area
best_x2=0       # This is the x2 cordinate od the test rectangle for which we get the max area
best_y1=0       # This is the y1 cordinate od the test rectangle for which we get the max area which is always 0, since the rectangle should have the base on x axis
best_y2=0       # This is the y2 cordinate od the test rectangle for which we get the max area

count_for_y=0
count_for_x=0
for i in range(len(points_sorted_Y)+1):
    if count_for_y==0:
        rectangle_y2=500
        count_for_y=1
        #print(i)
    else:
        i=i-1
        rectangle_y2=points_sorted_Y[len(points_sorted_Y)-i-1][1]
        #print(i)
    for j in range(len(points_sorted_X)+1):
        #print("Y2",rectangle_y2)
        if(j==len(points_sorted_X)):
            #print("checked")
            rectangle_x1=points_sorted_X[j-1][0]
            rectangle_x2=100000
            rectangle_area=abs(rectangle_y2-rectangle_y1)*abs(rectangle_x2-rectangle_x1)
            if(rectangle_area>max_area):
                max_area=rectangle_area
                best_x1=rectangle_x1
                best_x2=rectangle_x2
                best_y1=rectangle_y1
                best_y2=rectangle_y2
            continue
        rectangle_x2=points_sorted_X[j][0]
        if(points_sorted_X[j][1]>=rectangle_y2):
            continue
        # Now we compute the area
        rectangle_area=abs(rectangle_y2-rectangle_y1)*abs(rectangle_x2-rectangle_x1)
        # Now we update the x1 cordiate of the rectangle
        rectangle_x1=rectangle_x2
        
        # Now we choose the maximum of the area along with its cordinates
        if(rectangle_area>max_area):
            max_area=rectangle_area
            best_x1=rectangle_x1
            best_x2=rectangle_x2
            best_y1=rectangle_y1
            best_y2=rectangle_y2



print("Max Area:",max_area)
print("(",best_x1,",",best_y1,")")
print("(",best_x1,",",best_y2,")")
print("(",best_x2,",",best_y2,")")
print("(",best_x2,",",best_y1,")")
    
    
