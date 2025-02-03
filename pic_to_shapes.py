import sys
from PIL import Image

newPath = "Test Outputs/test7.png"
path = "Test Outputs/scaled7.png"
roundTo = 100
scaleTo = 100

def getShapes(pixels):
    rows = len(pixels)
    cols = len(pixels[0])
    s = 0
    shapes = {}
    neighbors = [[0, 1, pixels[0][1]], [1, 0, pixels[1][0]]]
    for i in range(0, rows):
        for j in range(0, cols):
            if pixels[i][j][3] != -1:
                start = pixels[i][j]
                shapes[s] = [[start[0], start[1], start[2], start[3]], [i, j]]
                neighborCount = 0
                if j < cols - 1 and pixels[i][j + 1][3] != -1:
                    neighbors.append([i, j + 1, pixels[i][j + 1]])
                    neighborCount += 1
                if i < rows - 1 and pixels[i + 1][j][3] != -1:
                    neighbors.append([i + 1, j, pixels[i][j]])
                    neighborCount += 1
                while neighborCount > 0:
                    n = neighbors[neighborCount]
                    nPix = n[2]
                    pixels[n[0]][n[1]] = (nPix[0], nPix[1], nPix[2], -1)
                    neighbors.remove(n)
                    neighborCount -= 1
                    if [n[2][0], n[2][1], n[2][2]] == [start[0], start[1], start[2]]:
                        shapes[s].append([n[0], n[1]])
                        if n[0] > 0:
                            if pixels[n[0] - 1][n[1]][3] != -1 and pixels[n[0] - 1][n[1]] not in neighbors:
                                neighbors.append([n[0] - 1, n[1], pixels[n[0] - 1][n[1]]])
                                neighborCount += 1
                            if n[1] > 0:
                                if pixels[n[0] - 1][n[1] - 1][3] != -1 and pixels[n[0] - 1][n[1] - 1] not in neighbors:
                                    neighbors.append([n[0] - 1, n[1] - 1, pixels[n[0] - 1][n[1] - 1]])
                                    neighborCount += 1
                            if n[1] < cols - 1:
                                if pixels[n[0] - 1][n[1] + 1][3] != -1 and pixels[n[0] - 1][n[1] + 1] not in neighbors:
                                    neighbors.append([n[0] - 1, n[1] + 1, pixels[n[0] - 1][n[1] + 1]])
                                    neighborCount += 1
                        if n[0] < rows - 1:
                            if pixels[n[0] + 1][n[1]][3] != -1 and pixels[n[0] + 1][n[1]] not in neighbors:
                                    neighbors.append([n[0] + 1, n[1], pixels[n[0] + 1][n[1]]])
                                    neighborCount += 1
                            if n[1] > 0:
                                if pixels[n[0] + 1][n[1] - 1][3] != -1 and pixels[n[0] + 1][n[1] - 1] not in neighbors:
                                    neighbors.append([n[0] + 1, n[1] - 1, pixels[n[0] + 1][n[1] - 1]])
                                    neighborCount += 1
                            if n[1] < cols - 1:
                                if pixels[n[0] + 1][n[1] + 1][3] != -1 and pixels[n[0] + 1][n[1] + 1] not in neighbors:
                                    neighbors.append([n[0] + 1, n[1] + 1, pixels[n[0] + 1][n[1] + 1]])
                                    neighborCount += 1
                        if n[1] > 0:
                            if pixels[n[0]][n[1] - 1][3] != -1 and pixels[n[0]][n[1] - 1] not in neighbors:
                                neighbors.append([n[0], n[1] - 1, pixels[n[0]][n[1] - 1]])
                                neighborCount += 1
                        if n[1] < cols - 1:
                            if pixels[n[0]][n[1] + 1][3] != -1 and pixels[n[0]][n[1] + 1] not in neighbors:
                                neighbors.append([n[0], n[1] + 1, pixels[n[0]][n[1] + 1]])
                                neighborCount += 1
                pixels[i][j] = (start[0], start[1], start[2], -1)
                s += 1

    return shapes


def process_image(image_path):
    try:
        rawImg = Image.open(image_path)
        originalWidth = rawImg.size[0]
        originalHeight = rawImg.size[1]
        newHeight = scaleTo * originalHeight / originalWidth
        img = rawImg.resize((scaleTo, round(newHeight)))
        img.save(path)
        width = img.size[0]
        height = img.size[1]
        tuplePixels = list(Image.open(path, "r").getdata())
        rows = []
        row = []
        i = 0
        for pixel in tuplePixels:
            if i < width:
                row.append(pixel)
                i += 1
            else:
                rows.append(row)
                i = 1
                row = []
                row.append(pixel)
        pixels = []
        for row in rows:
            newrow = []
            for pixel in row:
                newrow.append([round(pixel[0] / roundTo) * roundTo, round(pixel[1] / roundTo) * roundTo,
                               round(pixel[2] / roundTo) * roundTo, pixel[3]])
            pixels.append(newrow)

        newImage = Image.new(img.mode,img.size)
        data = []
        for i in range(0, len(pixels)):
            for j in range(0, len(pixels[0])):
                p = pixels[i][j]
                data.append((p[0], p[1], p[2], p[3]))
        newImage.putdata(data)
        newImage = newImage.resize((originalWidth, originalHeight))
        newImage.save(newPath)

        shapeDict = getShapes(pixels)

        return [shapeDict, newPath]

    except Exception as e:
        print(f"Error processing the image: {e}")
        
image_path = sys.argv[1]
process_image(image_path)
# print(process_image("Test Images/TestImage4.png"))



