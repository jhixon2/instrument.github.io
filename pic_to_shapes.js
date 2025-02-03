import sys
from PIL import Image

def getShapes(pixels):
    rows = len(pixels)
    cols = len(rows[0])
    s = 0
    shapes = {}
    neighbors = [pixels[0], pixels[0]]
    for i in range(0, cols):
        for j in range(0, rows):
            if pixels[i][j][3] != -1:
                start = pixels[i][j]
                shapes[[s, [start[0], start[1], start[2]]]] = [[i, j]]
                neighbors.append([i, j + 1, pixels[i][j + 1]])
                neighbors.append([i + 1, j, pixels[i][j]])
                for n in neighbors:
                    if [n[2][0], n[2][1], n[2][2]] == [start[0], start[1], start[2]]:
                        shapes[[s, [start[0], start[1], start[2]]]].append([n[1], n[2]])
                        if n[1] > 0:
                            if pixels[n[1] - 1, n[2]][3] != -1 and pixels[n[1] - 1, n[2]] not in neighbors:
                                    neighbors.append(pixels[n[1] - 1, n[2]])
                            if n[2] > 0:
                                if pixels[n[1] - 1, n[2] - 1][3] != -1 and pixels[n[1] - 1, n[2] - 1] not in neighbors:
                                    neighbors.append(pixels[n[1] - 1, n[2] - 1])
                            if n[2] < cols - 1:
                                if pixels[n[1] - 1, n[2] + 1][3] != -1 and pixels[n[1] - 1, n[2] + 1] not in neighbors:
                                    neighbors.append(pixels[n[1] - 1, n[2] + 1])
                        if n[1] < rows - 1:
                            if pixels[n[1] + 1, n[2]][3] != -1 and pixels[n[1] + 1, n[2]] not in neighbors:
                                    neighbors.append(pixels[n[1] + 1, n[2]])
                            if n[2] > 0:
                                if pixels[n[1] + 1, n[2] - 1][3] != -1 and pixels[n[1] + 1, n[2] - 1] not in neighbors:
                                    neighbors.append(pixels[n[1] + 1, n[2] - 1])
                            if n[2] < cols - 1:
                                if pixels[n[1] + 1, n[2] + 1][3] != -1 and pixels[n[1] + 1, n[2] + 1] not in neighbors:
                                    neighbors.append(pixels[n[1] + 1, n[2] + 1])
                        if n[2] > 0:
                            if pixels[n[1], n[2] - 1][3] != -1 and pixels[n[1], n[2] - 1] not in neighbors:
                                neighbors.append(pixels[n[1], n[2] - 1])
                        if n[2] < cols - 1:
                            if pixels[n[1], n[2] + 1][3] != -1 and pixels[n[1], n[2] + 1] not in neighbors:
                                neighbors.append(pixels[n[1], n[2] + 1])
                        n[2][3] = -1
                start[3] = -1

    return shapes


def process_image(image_path):
    # try:
    with open("New" + image_path + ".txt", "w") as file:
        width = Image.open(frame, "r").getdata().size[0]
        print(str(frameNum) + " / " + str(frameCount))
        frameBrightness = []
        pixels = list(Image.open(frame, "r").getdata())



        img = Image.open(image_path, "r")
        pixelsTuples = list(img.getdata())
        width = img.size[0]
        height = img.size[1]
        newHeight = 64 * width / height
        img = img.resize((64, round(newHeight)))
        rows = []
        row = []
        i = 0
        pixels = []
        for pixel in pixelsTuples:
            if i < width:
                row.append(pixel)
                i += 1
            else:
                rows.append(row)
                i = 1
                row = []
                row.append(pixel)
        for pixel in pixels:
            pixel[0] = round(pixel[0], -1)
            pixel[1] = round(pixel[1], -1)
            pixel[2] = round(pixel[2], -1)

        return getShapes(pixels)

    # except Exception as e:
    #     print(f"Error processing the image: {e}")
        
# image_path = sys.argv[1]
# process_image(image_path)
process_image("Test Images/instrTest1.png")



