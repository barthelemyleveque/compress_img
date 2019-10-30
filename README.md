# compress_img

The input image is read as a three-dimensional matrix whose first two indices identify the pixel position and whose last index represents Red, Green or Blue color values. 

After finding the top K colors to represent the image, each pixel position is assigned to its closest centroid. This allows to represent the original image using the centroid assignments of each pixel. In this way, the number of bits that are required to describe the image is reduced significantly and we get the resultant compressed image.

## Usage and installation

```
git clone https://github.com/barthelemyleveque/compress_img & cd compress_img
pip install opencv-python pandas numpy pillow opencv-python
```

Then you need an image, and think about the number of colors you want after compression ! This algorithm has a time-complexity of O(n<sup>2</sup>) so the bigger the image and the number of colors, the longer it will take for your computer to execute it.

```
python main.py [image_file] [number_of_colors](optional, 32 by default)
```

For example, with the following image : 


![parrots](https://us.123rf.com/450wm/psstockfoto/psstockfoto1609/psstockfoto160900047/65964562-loro-de-sun-conure-loro-o-amarillo-que-cuelga-en-la-ramificaci%C3%B3n.jpg?ver=6)
