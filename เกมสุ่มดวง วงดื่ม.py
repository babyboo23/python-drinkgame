import random
print('----------เกมสุ่มวัดดวง----------')
print('วิธีการใส่ชื่อรายการสุ่ม : (พิมพ์ชื่อรายการสุ่มกดเว้นวรรคเพื่อเพิ่มรายการสุ่ม)')
type_items = [item for item in input('ใส่ชื่อรายการสุ่ม :').split()]
players = int(input('ใส่จำนวนผู้เล่น :'))
print('คนแรกเริ่มสุ่มได้เลยยย')
nums = 1
for i in range(players):
    input('press enter to continue....')
    type = random.choice(type_items)
    print('คนที่',nums,'ได้ :',type)
    nums = nums +1
print('----------จบเกมแล้วน้าาา----------')

    
