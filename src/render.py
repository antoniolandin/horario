from PIL import ImageFont
from PIL import Image
from PIL import ImageDraw

import os
import random

base_img = Image.open("assets/base.png")

box_width = 602
box_height = 272

x0 = 267
y0 = 420


def draw_box(day, hour, draw):
    x = x0 + (box_width * day + 6 * day)
    y = y0 + (box_height * hour + 3 * hour)

    draw.rectangle([x, y, x + box_width, y + box_height],
                   fill="#cacaca",
                   outline=(0, 0, 0))


def draw_lecture(lecture, draw):
    lecture_start = 9 + lecture.hour * 2
    lecture_end = lecture_start + 2

    # we put the start and end time in the format HH:MM 
    lecture_start = str(lecture_start) + ":00"
    lecture_end = str(lecture_end) + ":00"

    x = x0 + (box_width * lecture.day + 6 * lecture.day)
    y = y0 + (box_height * lecture.hour + 3 * lecture.hour)

    # draw box
    draw_box(lecture.day, lecture.hour, draw)

    # draw start and end time
    hour_font = ImageFont.truetype("arial.ttf", 35)
    draw.text((x + 10, y + 10), lecture_start, font=hour_font, fill=(0, 0, 0))
    draw.text((x + box_width - 100, y + box_height - 50),
              lecture_end,
              font=hour_font,
              fill=(0, 0, 0))

    # draw group name
    group_font = ImageFont.truetype("arial.ttf", 35)
    group_name = lecture.group
    _, _, w, h = draw.textbbox((0, 0), group_name, font=group_font)

    draw.text((x + (box_width - w) / 2, y + (box_height - h) / 2 - 30),
              group_name,
              font=group_font,
              fill=(0, 0, 0))

    # draw subject name
    lecture_font = ImageFont.truetype("arial.ttf", 60)
    _, _, w, h = draw.textbbox((0, 0), lecture.subject, font=lecture_font)
    draw.text((x + (box_width - w) / 2, y + (box_height - h) / 2 + 15),
              lecture.subject,
              font=lecture_font,
              fill=(0, 0, 0))

    # draw teacher name
    teacher_font = ImageFont.truetype("arial.ttf", 25)
    _, _, w, h = draw.textbbox((0, 0), lecture.teacher, font=teacher_font)
    draw.text((x + (box_width - w) / 2, y + (box_height - h) / 2 + 60),
              lecture.teacher,
              font=teacher_font,
              fill=(0, 0, 0))


def get_schedule_img(lectures):
    img = base_img.copy()

    draw = ImageDraw.Draw(img)

    for lecture in lectures:
        draw_lecture(lecture, draw)

    return img


def save_schedule_img(lectures):
    img = get_schedule_img(lectures)

    random_string = ''.join(random.choices("ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789",
                                           k=10))
    # check if the out folder exists
    if not os.path.exists("out"):
        os.makedirs("out")

    img.save(f"out/{random_string}.png")
