my_name = 'Zed A. Shaw'
my_age = 35
my_height = 74.0 # inches
my_weight = 180 # lbs
my_eyes = 'Blue'
my_teeth = 'White'
my_hair = 'Brown'

conv_inch_to_cm = 2.54
conv_lb_to_kg =0.4536

print "Let's talk about %s." % my_name
print "He's %d inches tall." % my_height
print ". . .or %d cm." % (my_height * conv_inch_to_cm)
print "He's %d pounds heavy." % my_weight
print ". . .or %f kg." % (my_weight * conv_lb_to_kg)
print "Actually that's not too heavy."
print "He's got %s eyes and %s hair." % (my_eyes, my_hair)
print "His teeth are usually %s depending on the coffee." % my_teeth

# this line is tricky
print "If I add %d, %d, and %d I get %d." % (my_age, my_height, my_weight, my_age + my_height + my_weight)