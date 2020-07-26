We have a rectangle region that is 1000000 units along X-axis and 500 units along
the Y-axis.
We assume that the origin (0,0) is at the bottoom-left  corner of the region, so that
the top-left  corner is at (0,500), the bottoom-right at (1000000,0) and the top-right
corner at (1000000,500), We are also given the coordinates of a set of N points inside
this region. The points have only integer coordinates and do not appear along the
X-axis or Y-axis.
We would like to draw a rectangle, with its base on the X-axis, of maximum area
within the region such that it does contain any of the N points in its interior. More
specifically, the points may appear on the boundary but cannot be properly inside
the rectangle.
For example, if there are 5 points:
(1,4),(2,3),(3,2),(5,1) and (5,2). Then the rectangle whose bottoom-left  and top-right
corners are given (0,0) and (2,3) is possibility and its area is 6. Another possibility is
the rectangle with bottoom-left  and top-right corners are (3,0) and (5,500) with area
1000. The rectangle with bottoom-left  at (2,3) and top-right at (1000000,500) is not
valid since its base does not lie on the X-axis. The largest rectangle that meets the
requirements in this case is the one with its bottoom-left  corner at (5,0) and topright at (1000000,500) with area 4909970500.
Your program should take a description of N points and output the size of the
maximum rectangle along with their coordinates, satisfying the above property
that can be drawn within the 1000000 x 500 region.
