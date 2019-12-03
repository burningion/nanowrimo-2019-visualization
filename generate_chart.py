import cairocffi as cairo
import math

import glob

days = {} 

# first, count the number of words in every md file
for filename in glob.glob('*.md'):
    processname = f"wc -w {filename}".split()
    process = subprocess.Popen(processname, stdout=subprocess.PIPE)
    for line in process.stdout:
        if b"the" in line:
            continue
        days[int(filename[:2])] = int(line.decode('utf-8').split()[0])

# color scheme from https://colorhunt.co/palette/164242
surface = cairo.ImageSurface(cairo.FORMAT_ARGB32, 2048, 2448)
cr = cairo.Context(surface)
cr.set_source_rgb(.984,.89,.725)
cr.paint()
cr.scale(2048, 2048)

count = 0

for y in range(5):
    for x in range(6):
        rg = cairo.RadialGradient(.07 + (x / 5.8), .075 + (y / 4.8),
                                  .024,
                                  .07 + (x / 5.8), .075 + (y / 4.8),
                                  .05)
        rg.add_color_stop_rgba(1, 0.98, .714, .588, .8)
        rg.add_color_stop_rgba(1, 0.3, 0.3, 0.3, .9)
        cr.set_source(rg)
        cr.arc(.07 + (x / 5.8), .075 + (y / 4.8), .033, 0., 2 * math.pi)
        cr.fill()

        if count in days.keys():
            cr.set_line_cap(0)
            cr.set_source_rgba(0.176,.2,.29,1)
            cr.arc(.07 + (x / 5.8), .075 + (y / 4.8), .03, 
                   1.5 * math.pi, (days[count] / 2972.0) * 2 * math.pi + (1.5 * math.pi))
            cr.set_line_width(.015)
            cr.stroke()
            
        cr.select_font_face("Sans", cairo.FONT_SLANT_NORMAL,
                            cairo.FONT_WEIGHT_BOLD)
        cr.set_font_size(0.03)
        cr.set_source_rgba(0.176,.2,.29,1)
        cr.move_to(.01 + (x / 5.8), .145 + (y / 4.8))
        cr.show_text(f"day {count:02}")
        cr.set_font_size(0.018)
        cr.move_to(.01 + (x / 5.8), .185 + (y / 4.8))
        
        if count in days.keys():
            cr.show_text(f"{days[count]} words")
        else:
            # grey out the days I didn't write
            cr.set_source_rgba(0.176,.2,.29,.7)
            cr.show_text("0 words")
        count += 1

# add title for graphic
cr.set_font_size(0.05)
cr.move_to(.25, 1.125)
cr.show_text("NaNoWriMo 2019")
cr.set_font_size(0.02)
cr.move_to(.35, 1.16)
cr.set_source(rg)
cr.select_font_face("Sans", cairo.FONT_SLANT_ITALIC,
                            cairo.FONT_WEIGHT_BOLD)
# and my site name 
cr.show_text("makeartwithpython.com")
surface.write_to_png('out.png')
