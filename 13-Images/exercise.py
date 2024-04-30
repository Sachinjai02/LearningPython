from PIL import Image

matrix = Image.open('word_matrix.png')
mask = Image.open('mask.png')

print(f'size of matrix is {matrix.size} and that of mask is {mask.size}')

mask = mask.resize((1015,559))
mask.putalpha(128)
matrix.paste(im=mask, box = (0,0), mask = mask)

matrix.show()