
# # генерация случайной позиции по х и по y
#   # random.seed(5)
#   x = np.random.randint(0, screen_width )
#   y = np.random.razdint(0, screen_height)
#   read_number = number_pix.take(x, axis=0)[y] # взятие числа
#       в матрице по координатам
#   number_pix[x, y] = read_number + step   # увеличение яркости цвета
#       на step(от чёрного к белому) при повторном попадании пикселя,
#       на одно и тоже место
#   if read_number > 255:
#       pix.fill((255, 0, 255))
#   else:
#       pix.fill((read_number, read_number, read_number))

#   window.blit(pix, (x, y))


# 1
# x += int(x / y * 4)
# y += int(y / x * 4)
# #2
# x += x / 100
# y += y / 100
# #3?
# x += int(2 - (math.sqrt(y)))
# y += int(2 - (math.sqrt(x)))
# 4
# x += math.sin(x) * 5
# y += -math.cos(y) * 5
