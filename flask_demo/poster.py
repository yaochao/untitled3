import io

import requests
from PIL import Image, ImageDraw, ImageFont
from uuid import uuid4
from qiniu import Auth, put_file
import os

access_key = 'T89tUhVK006ZCfT2b3oCVWOTvsL6eUHs4loc2bZg'
secret_key = 'nYgc-NLoWkAZRN_ba1hEN-SVar8WKoqZzhzxXPTS'
bucket_name = 'infoxmedpdf2'
bucket_url = 'doc2.infox-med.com'

q = Auth(access_key, secret_key)


def generate_picture_from_url(url, path=None):
    response = requests.get(url=url, stream=True)
    out_file_path = str(uuid4()) + '.png'
    if path:
        out_file_path = os.path.join(path, str(uuid4()) + '.png')
    with open(out_file_path, 'wb') as f:
        for chunk in response.iter_content(chunk_size=32):
            f.write(chunk)

    return out_file_path


def upload_pdf(path):
    if not path:
        return
    new_file_ = f"{str(uuid4())}.png"
    token = q.upload_token(bucket_name, new_file_, 3600)
    ret, info = put_file(token, new_file_, path)
    if not ret:
        os.remove(path)
        raise Exception('七牛云上传失败')
    res_url = 'https://%s/%s' % (bucket_url, ret['key'])
    os.remove(path)
    return res_url


def generate_poster(user_avatar_url=None,
                    backgroud_path='assets/backgroud.png',
                    desciption_img_path=None,
                    user_nickname=None,
                    fish_nums='1000',
                    rank=None,
                    potential=None,
                    love_demand=None,
                    strength=None,
                    time_management=None,
                    font_path='assets/mircosoft.ttf'
                    ) -> bytes:
    """
        backgroud_url:背景图片url,
        desciption_text_url:文案贴图url,不同文案
        user_nickname:用户昵称
        fish_nums:养鱼数量
        rank:段位
        potential:潜力
        love_demand:恋爱需求度
        strength:养鱼实力
        time_management:时间管理
        font_path:字体文件路径
    """
    # 头像url
    user_avatar = generate_picture_from_url(user_avatar_url, path='tmp')

    # 背景图
    bg_img = Image.open(backgroud_path).convert('RGBA')
    bg_img_x, bg_img_y = bg_img.size

    # 需要转成字符串
    fish_nums = str(fish_nums)
    if isinstance(fish_nums, int):
        fish_nums = str(fish_nums)

    # 获取单位 x 375 y 596
    px = bg_img_x / 800
    py = bg_img_y / 1299

    # 获取画笔
    draw = ImageDraw.Draw(bg_img)
    # 用户头像
    user_avatar_img = Image.open(user_avatar).convert('RGBA')
    user_avatar_img_size = (int(215 * px), int(215 * px))
    user_avatar_img = user_avatar_img.resize(user_avatar_img_size)
    user_avatar_img_pos = (int(40 * px), int(165 * py))
    bg_img.paste(user_avatar_img, user_avatar_img_pos)

    # 用户昵称
    font_size = int(30 * px)
    font = ImageFont.truetype(font_path, font_size)
    user_nickname_text_pos = (int(509 * px), int(192 * py))
    font_nickname_color = (0, 0, 0)
    draw.text(user_nickname_text_pos, user_nickname, font_nickname_color, font)

    # 养多少鱼的数量
    font_size = int(30 * px)
    font = ImageFont.truetype(font_path, font_size)
    fish_nums_color = (182, 69, 87)
    fish_width = int(25 * px)
    for i in range(len(fish_nums)):
        fish_nums_text_pos = (int(461 * px) + fish_width * i, int(255 * py))
        draw.text(fish_nums_text_pos, fish_nums[i], fish_nums_color, font)
        if i == len(fish_nums) - 1:
            font_size = int(38 * px)
            font = ImageFont.truetype(font_path, font_size)
            fish_nums_text_pos = (int(461 * px) + fish_width * (i + 1), int(250 * py))
            fish_nums_color = (0, 0, 0)
            draw.text(fish_nums_text_pos, '条鱼', fish_nums_color, font)

    # 段位
    font_size = int(40 * px)
    font = ImageFont.truetype(font_path, font_size)
    rank_text_pos = (int(509 * px), int(310 * py))
    rank_color = (0, 0, 0)
    draw.text(rank_text_pos, rank, rank_color, font)
    # 重复加粗
    font_size = int(40 * px)
    font = ImageFont.truetype(font_path, font_size)
    rank_text_pos = (int(510 * px), int(310 * py))
    rank_color = (0, 0, 0)
    draw.text(rank_text_pos, rank, rank_color, font)

    # 海外潜力
    font_size = int(30 * px)
    font = ImageFont.truetype(font_path, font_size)
    potential_text_pos = (int(222 * px), int(402 * py))
    potential_color = (182, 69, 87)
    draw.text(potential_text_pos, potential, potential_color, font)

    # 恋爱需求度
    font_size = int(30 * px)
    font = ImageFont.truetype(font_path, font_size)
    love_demand_text_pos = (int(599 * px), int(402 * py))
    love_demand_color = (182, 69, 87)
    draw.text(love_demand_text_pos, love_demand, love_demand_color, font)

    # 养鱼实力
    font_size = int(30 * px)
    font = ImageFont.truetype(font_path, font_size)
    strength_text_pos = (int(222 * px), int(460 * py))
    strength_color = (182, 69, 87)
    draw.text(strength_text_pos, strength, strength_color, font)

    # 时间管理能力
    font_size = int(30 * px)
    font = ImageFont.truetype(font_path, font_size)
    time_management_text_pos = (int(597 * px), int(460 * py))
    time_management_color = (182, 69, 87)
    draw.text(time_management_text_pos, time_management, time_management_color, font)

    # 文案贴图
    description_img = Image.open(desciption_img_path).convert('RGBA')
    description_img_size = description_img.size
    description_img_pos = (int(86 * px), int(560 * py))
    mask = Image.new('RGBA', description_img_size, color=(0, 0, 0, 0))
    mask_draw = ImageDraw.Draw(mask)
    mask_draw.ellipse((0, 0, description_img_size[0], description_img_size[1]), fill=(0, 0, 0, 255))
    bg_img.paste(description_img, description_img_pos,mask)

    # out_file_path = str(uuid4()) + '.png'
    # bg_img.save(out_file_path)
    # # 可能需要更换bucket
    # qiniu_url = upload_pdf(out_file_path)

    # 获取字节流
    byte_array = io.BytesIO()
    bg_img = bg_img.resize((int(bg_img_x * 0.7), int(bg_img_y * 0.7)))
    bg_img.save(byte_array, format='PNG')
    byte_array = byte_array.getvalue()
    return byte_array


if __name__ == '__main__':
    """
      backgroud_url:背景图片url,
        desciption_text_url:文案贴图url,不同文案
        user_nickname:用户昵称
        fish_nums:养鱼数量
        rank:段位
        potential:潜力
        love_demand:恋爱需求度
        strength:养鱼实力
        time_management:时间管理
        font_path:字体文件路径"""

    res = generate_poster(
        user_avatar_url='http://www.lrabbit.life/static/img/%E9%AB%98%E6%9C%A8.jpg',
        desciption_img_path='https://lrabbit.oss-cn-beijing.aliyuncs.com/wenan.png',
        user_nickname='小兔子',
        fish_nums='10900',
        rank='顶级寡王',
        potential='-100%',
        love_demand='100%',
        strength='爆表',
        time_management='爆表'
    )
    print(res)
