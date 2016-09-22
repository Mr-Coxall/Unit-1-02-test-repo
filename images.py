# Created by: Mr. Coxall
# Created on: Aug 2016
# Created for: ICS3U
# This program shows images

import ui

# first get a reference to the image you saved in your Python folder
my_pic = ui.Image.named('./sprites/MT_crest.jpg')

# then create an ImageView to show it in
my_image = ui.ImageView(frame=(100, 100, 200, 300))

# then add the image into the ImageView
my_image.image = my_pic


view = ui.load_view()

# lastly, add the Imageview into the existing view
view.add_subview(my_image)
view.present('full_screen')
