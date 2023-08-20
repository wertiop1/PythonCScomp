# taken from https://usaco.guide/bronze/rect-geo 
'''
tr is top right
bl is bottom left
width = tr_x - bl_x

length = tr_y - bl_y

area = width * length
'''
def area(bl_x: int, bl_y: int, tr_x: int, tr_y: int) -> int:
	length = tr_y - bl_y
	width = tr_x - bl_x
	return length * width
'''
non intersection case:
tr_a_y <= bl_b_y or bl_a_y >= tr_b_y
bl_a_x >= tr_b_x or tr_a_x <= bl_b_x

'''
def intersect(s1, s2) -> bool:
	bl_a_x, bl_a_y, tr_a_x, tr_a_y = s1[0], s1[1], s1[2], s1[3]
	bl_b_x, bl_b_y, tr_b_x, tr_b_y = s2[0], s2[1], s2[2], s2[3]

	# no overlap
	if bl_a_x >= tr_b_x or tr_a_x <= bl_b_x or bl_a_y >= tr_b_y or tr_a_y <= bl_b_y:
		return False
	else:
		return True
'''
We'll assume that the shape formed by the intersection of two rectangles is itself a rectangle.

First, we'll find this rectangle's length and width.
width = min(tr_a_x, tr_b_x) - max(bl_a_x, bl_{b_x)
length = min(tr_a_y, tr_b_y) - max(bl_a_y, bl_b_y)

If either of these values are negative, the rectangles do not intersect.
If they are zero, the rectangles intersect at a single point.
Multiply the length and width to find the overlapping area.
'''
def inter_area(s1, s2) -> int:
	bl_a_x, bl_a_y, tr_a_x, tr_a_y = s1[0], s1[1], s1[2], s1[3]
	bl_b_x, bl_b_y, tr_b_x, tr_b_y = s2[0], s2[1], s2[2], s2[3]

	return (min(tr_a_x, tr_b_x) - max(bl_a_x, bl_b_x)) * (
		min(tr_a_y, tr_b_y) - max(bl_a_y, bl_b_y)
	)