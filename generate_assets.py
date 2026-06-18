#!/usr/bin/env python3
"""生成情侣吵架日记项目的所有图片资源：头像照片 + PWA 图标 + favicon"""
from PIL import Image, ImageDraw, ImageFilter
import os

OUT = '/workspace/public'
os.makedirs(f'{OUT}/images', exist_ok=True)
os.makedirs(f'{OUT}/icons', exist_ok=True)

def draw_boy_avatar(size=600):
    """卡通男生头像：黑色短发、大眼睛、蓝色T恤、浅蓝背景"""
    img = Image.new('RGBA', (size, size), (219, 232, 245, 255))
    d = ImageDraw.Draw(img)
    cx, cy = size // 2, size // 2

    # 上衣肩膀
    top_y = cy + int(size * 0.22)
    d.pieslice((cx - int(size*0.58), top_y - int(size*0.38),
                cx + int(size*0.58), top_y + int(size*0.38)),
               180, 360, fill=(107, 139, 168, 255))
    d.rectangle((cx - int(size*0.58), top_y, cx + int(size*0.58), size),
                fill=(107, 139, 168, 255))

    # 领口
    collar_w = int(size * 0.11)
    collar_h = int(size * 0.05)
    d.polygon([(cx - collar_w, top_y), (cx + collar_w, top_y),
               (cx, top_y + collar_h)], fill=(90, 120, 150, 255))

    # 颈部
    neck_w = int(size * 0.11)
    neck_h = int(size * 0.08)
    d.rectangle((cx - neck_w, top_y - neck_h, cx + neck_w, top_y),
                fill=(245, 208, 184, 255))

    # 脸
    face_rx = int(size * 0.28)
    face_ry = int(size * 0.33)
    face_top = cy - int(size * 0.25)
    face_bot = cy + int(size * 0.22)
    d.ellipse((cx - face_rx, face_top, cx + face_rx, face_bot),
              fill=(245, 208, 184, 255))

    # 头发主体
    hair_top = face_top - int(size * 0.12)
    hair_bot = face_top + int(size * 0.14)
    d.ellipse((cx - int(size*0.33), hair_top,
               cx + int(size*0.33), hair_bot + int(size*0.06)),
              fill=(42, 42, 48, 255))

    # 蓬松感
    for (dx, dy, r_factor) in [
        (-0.28, -0.12, 1.0), (-0.22, -0.22, 0.95), (-0.12, -0.27, 0.9),
        (0.0, -0.30, 0.9), (0.12, -0.27, 0.9), (0.22, -0.22, 0.95),
        (0.28, -0.12, 1.0), (-0.30, 0.0, 0.85), (0.30, 0.0, 0.85),
        (-0.08, -0.32, 0.82), (0.08, -0.32, 0.82),
    ]:
        px = cx + int(size * dx)
        py = hair_bot + int(size * dy)
        r = int(size * 0.09 * r_factor)
        d.ellipse((px - r, py - r, px + r, py + r), fill=(42, 42, 48, 255))

    # 刘海
    bang_bot = face_top + int(size * 0.14)
    d.ellipse((cx - int(size*0.30), face_top - int(size*0.03),
               cx + int(size*0.30), bang_bot),
              fill=(36, 36, 42, 255))
    # 刘海波浪
    for i in range(-3, 4):
        bx = cx + int(size * 0.09 * i)
        by = bang_bot - int(size * 0.01)
        br = int(size * 0.038)
        d.ellipse((bx - br, by - br, bx + br, by + br), fill=(40, 40, 46, 255))

    # 头发高光
    for (dx, dy, col) in [
        (-0.15, -0.20, (80, 80, 88, 180)),
        (-0.05, -0.26, (90, 90, 98, 160)),
        (0.08, -0.22, (80, 80, 88, 180)),
        (0.18, -0.15, (75, 75, 85, 170)),
    ]:
        hx = cx + int(size * dx)
        hy = hair_bot + int(size * dy)
        hr = int(size * 0.014)
        d.ellipse((hx - hr, hy - hr, hx + hr, hy + hr), fill=col)

    # 眉毛
    brow_y = face_top + int(size * 0.14)
    brow_dist = int(size * 0.12)
    brow_w = int(size * 0.08)
    brow_thick = int(size * 0.014)
    d.ellipse((cx - brow_dist - brow_w, brow_y - brow_thick,
               cx - brow_dist + brow_w, brow_y + brow_thick),
              fill=(36, 36, 42, 255))
    d.ellipse((cx + brow_dist - brow_w, brow_y - brow_thick,
               cx + brow_dist + brow_w, brow_y + brow_thick),
              fill=(36, 36, 42, 255))

    # 眼睛
    eye_cx_dist = int(size * 0.12)
    eye_y = face_top + int(size * 0.22)
    eye_rx = int(size * 0.045)
    eye_ry = int(size * 0.052)
    for sign in [-1, 1]:
        ex = cx + sign * eye_cx_dist
        d.ellipse((ex - eye_rx, eye_y - eye_ry,
                   ex + eye_rx, eye_y + eye_ry),
                  fill=(30, 30, 38, 255))
        d.ellipse((ex - eye_rx + int(size*0.006), eye_y - eye_ry + int(size*0.006),
                   ex + eye_rx - int(size*0.006), eye_y + eye_ry),
                  fill=(55, 55, 62, 255))
        # 主高光
        hl1_rx = int(size * 0.018)
        hl1_ry = int(size * 0.024)
        hl1_x = ex - int(size * 0.012)
        hl1_y = eye_y - int(size * 0.022)
        d.ellipse((hl1_x - hl1_rx, hl1_y - hl1_ry,
                   hl1_x + hl1_rx, hl1_y + hl1_ry),
                  fill=(255, 255, 255, 255))
        # 小高光
        hl2_r = int(size * 0.008)
        hl2_x = ex + int(size * 0.016)
        hl2_y = eye_y + int(size * 0.018)
        d.ellipse((hl2_x - hl2_r, hl2_y - hl2_r,
                   hl2_x + hl2_r, hl2_y + hl2_r),
                  fill=(255, 255, 255, 240))

    # 腮红
    blush_img = Image.new('RGBA', (size, size), (0, 0, 0, 0))
    blush_d = ImageDraw.Draw(blush_img)
    blush_rx = int(size * 0.055)
    blush_ry = int(size * 0.03)
    blush_y = eye_y + int(size * 0.05)
    blush_dist = int(size * 0.17)
    blush_d.ellipse((cx - blush_dist - blush_rx, blush_y - blush_ry,
                     cx - blush_dist + blush_rx, blush_y + blush_ry),
                    fill=(255, 184, 184, 150))
    blush_d.ellipse((cx + blush_dist - blush_rx, blush_y - blush_ry,
                     cx + blush_dist + blush_rx, blush_y + blush_ry),
                    fill=(255, 184, 184, 150))
    img = Image.alpha_composite(img, blush_img)
    d = ImageDraw.Draw(img)

    # 微笑嘴
    mouth_y = face_top + int(size * 0.36)
    mouth_w = int(size * 0.05)
    mouth_ry = int(size * 0.025)
    d.arc((cx - mouth_w, mouth_y - mouth_ry,
           cx + mouth_w, mouth_y + mouth_ry),
          0, 180, fill=(192, 112, 112, 255), width=int(size*0.01))

    # 柔和滤镜
    img = img.filter(ImageFilter.SMOOTH)
    return img


def draw_girl_avatar(size=600):
    """卡通女生头像：黑色长发、大眼睛、米白衣+心形项链、米色背景"""
    img = Image.new('RGBA', (size, size), (245, 235, 220, 255))
    d = ImageDraw.Draw(img)
    cx, cy = size // 2, size // 2

    # 背后长发
    for (dx, dy, w, h) in [
        (-0.18, -0.05, 0.16, 0.32),
        (-0.28, 0.08, 0.14, 0.42),
        (-0.25, 0.28, 0.15, 0.30),
        (-0.18, 0.42, 0.16, 0.22),
        (-0.08, 0.48, 0.11, 0.18),
    ]:
        px = cx + int(size * dx)
        py = cy + int(size * dy)
        pw = int(size * w)
        ph = int(size * h)
        d.ellipse((px - pw, py - ph, px + pw, py + ph), fill=(74, 58, 58, 255))
    for (dx, dy, w, h) in [
        (0.18, -0.05, 0.16, 0.32),
        (0.28, 0.08, 0.14, 0.42),
        (0.25, 0.28, 0.15, 0.30),
        (0.18, 0.42, 0.16, 0.22),
        (0.08, 0.48, 0.11, 0.18),
    ]:
        px = cx + int(size * dx)
        py = cy + int(size * dy)
        pw = int(size * w)
        ph = int(size * h)
        d.ellipse((px - pw, py - ph, px + pw, py + ph), fill=(74, 58, 58, 255))

    # 上衣
    top_y = cy + int(size * 0.22)
    d.pieslice((cx - int(size*0.58), top_y - int(size*0.38),
                cx + int(size*0.58), top_y + int(size*0.38)),
               180, 360, fill=(232, 220, 200, 255))
    d.rectangle((cx - int(size*0.58), top_y, cx + int(size*0.58), size),
                fill=(232, 220, 200, 255))

    # 领口
    collar_w = int(size * 0.11)
    collar_h = int(size * 0.05)
    d.polygon([(cx - collar_w, top_y), (cx + collar_w, top_y),
               (cx, top_y + collar_h)], fill=(215, 200, 180, 255))

    # 心形项链
    heart_cx = cx
    heart_cy = top_y + int(size * 0.12)
    hr = int(size * 0.018)
    heart_img = Image.new('RGBA', (size, size), (0, 0, 0, 0))
    hd = ImageDraw.Draw(heart_img)
    hd.ellipse((heart_cx - hr*2 - 2, heart_cy - hr,
                heart_cx - 2, heart_cy + hr),
               fill=(255, 156, 181, 255))
    hd.ellipse((heart_cx + 2, heart_cy - hr,
                heart_cx + hr*2 + 2, heart_cy + hr),
               fill=(255, 156, 181, 255))
    hd.polygon([(heart_cx - hr*2, heart_cy + hr//2),
                (heart_cx + hr*2, heart_cy + hr//2),
                (heart_cx, heart_cy + hr*2 + int(size*0.008))],
               fill=(255, 156, 181, 255))
    img = Image.alpha_composite(img, heart_img)
    d = ImageDraw.Draw(img)

    # 颈部
    neck_w = int(size * 0.11)
    neck_h = int(size * 0.08)
    d.rectangle((cx - neck_w, top_y - neck_h, cx + neck_w, top_y),
                fill=(245, 216, 192, 255))

    # 脸
    face_rx = int(size * 0.28)
    face_ry = int(size * 0.33)
    face_top = cy - int(size * 0.25)
    face_bot = cy + int(size * 0.22)
    d.ellipse((cx - face_rx, face_top, cx + face_rx, face_bot),
              fill=(245, 216, 192, 255))

    # 头顶头发
    hair_top = face_top - int(size * 0.14)
    hair_bot = face_top + int(size * 0.15)
    d.ellipse((cx - int(size*0.35), hair_top,
               cx + int(size*0.35), hair_bot + int(size*0.05)),
              fill=(74, 58, 58, 255))

    # 蓬松感
    for (dx, dy, r_factor) in [
        (-0.30, -0.12, 1.05), (-0.22, -0.22, 0.98), (-0.12, -0.28, 0.92),
        (0.0, -0.32, 0.92), (0.12, -0.28, 0.92), (0.22, -0.22, 0.98),
        (0.30, -0.12, 1.05), (-0.32, 0.0, 0.88), (0.32, 0.0, 0.88),
        (-0.08, -0.34, 0.82), (0.08, -0.34, 0.82),
        (-0.34, 0.10, 0.78), (0.34, 0.10, 0.78),
    ]:
        px = cx + int(size * dx)
        py = hair_bot + int(size * dy)
        r = int(size * 0.095 * r_factor)
        d.ellipse((px - r, py - r, px + r, py + r), fill=(74, 58, 58, 255))

    # 刘海
    bang_bot = face_top + int(size * 0.14)
    d.ellipse((cx - int(size*0.31), face_top - int(size*0.04),
               cx + int(size*0.31), bang_bot),
              fill=(58, 42, 42, 255))
    # 刘海波浪
    for i in range(-4, 5):
        bx = cx + int(size * 0.08 * i)
        by = bang_bot - int(size * 0.01)
        br = int(size * 0.035)
        d.ellipse((bx - br, by - br, bx + br, by + br), fill=(58, 42, 42, 255))

    # 头顶高光
    for (dx, dy, col) in [
        (-0.15, -0.22, (120, 110, 110, 150)),
        (-0.05, -0.28, (130, 120, 120, 140)),
        (0.08, -0.24, (120, 110, 110, 150)),
        (0.18, -0.18, (115, 105, 105, 140)),
    ]:
        hx = cx + int(size * dx)
        hy = hair_bot + int(size * dy)
        hr = int(size * 0.013)
        d.ellipse((hx - hr, hy - hr, hx + hr, hy + hr), fill=col)

    # 眉毛
    brow_y = face_top + int(size * 0.14)
    brow_dist = int(size * 0.12)
    brow_w = int(size * 0.08)
    brow_thick = int(size * 0.014)
    d.ellipse((cx - brow_dist - brow_w, brow_y - brow_thick,
               cx - brow_dist + brow_w, brow_y + brow_thick),
              fill=(58, 42, 42, 255))
    d.ellipse((cx + brow_dist - brow_w, brow_y - brow_thick,
               cx + brow_dist + brow_w, brow_y + brow_thick),
              fill=(58, 42, 42, 255))

    # 眼睛
    eye_cx_dist = int(size * 0.12)
    eye_y = face_top + int(size * 0.22)
    eye_rx = int(size * 0.048)
    eye_ry = int(size * 0.055)
    for sign in [-1, 1]:
        ex = cx + sign * eye_cx_dist
        d.ellipse((ex - eye_rx, eye_y - eye_ry,
                   ex + eye_rx, eye_y + eye_ry),
                  fill=(40, 40, 48, 255))
        d.ellipse((ex - eye_rx + int(size*0.006), eye_y - eye_ry + int(size*0.006),
                   ex + eye_rx - int(size*0.006), eye_y + eye_ry),
                  fill=(65, 55, 55, 255))
        # 主高光
        hl1_rx = int(size * 0.020)
        hl1_ry = int(size * 0.026)
        hl1_x = ex - int(size * 0.014)
        hl1_y = eye_y - int(size * 0.024)
        d.ellipse((hl1_x - hl1_rx, hl1_y - hl1_ry,
                   hl1_x + hl1_rx, hl1_y + hl1_ry),
                  fill=(255, 255, 255, 255))
        # 小高光
        hl2_r = int(size * 0.009)
        hl2_x = ex + int(size * 0.016)
        hl2_y = eye_y + int(size * 0.018)
        d.ellipse((hl2_x - hl2_r, hl2_y - hl2_r,
                   hl2_x + hl2_r, hl2_y + hl2_r),
                  fill=(255, 255, 255, 240))

    # 腮红
    blush_img = Image.new('RGBA', (size, size), (0, 0, 0, 0))
    blush_d = ImageDraw.Draw(blush_img)
    blush_rx = int(size * 0.06)
    blush_ry = int(size * 0.032)
    blush_y = eye_y + int(size * 0.05)
    blush_dist = int(size * 0.17)
    blush_d.ellipse((cx - blush_dist - blush_rx, blush_y - blush_ry,
                     cx - blush_dist + blush_rx, blush_y + blush_ry),
                    fill=(255, 184, 184, 160))
    blush_d.ellipse((cx + blush_dist - blush_rx, blush_y - blush_ry,
                     cx + blush_dist + blush_rx, blush_y + blush_ry),
                    fill=(255, 184, 184, 160))
    img = Image.alpha_composite(img, blush_img)
    d = ImageDraw.Draw(img)

    # 微笑嘴
    mouth_y = face_top + int(size * 0.36)
    mouth_w = int(size * 0.05)
    mouth_ry = int(size * 0.025)
    d.arc((cx - mouth_w, mouth_y - mouth_ry,
           cx + mouth_w, mouth_y + mouth_ry),
          0, 180, fill=(192, 112, 112, 255), width=int(size*0.01))

    img = img.filter(ImageFilter.SMOOTH)
    return img


def draw_app_icon(size=512, with_border=True):
    """PWA图标：粉色圆形背景+双人头像+心形"""
    img = Image.new('RGBA', (size, size), (0, 0, 0, 0))
    d = ImageDraw.Draw(img)
    cx, cy = size // 2, size // 2
    bg_r = int(size * 0.48)

    # 背景渐变（多层圆）
    layers = 18
    for i in range(layers):
        t = i / (layers - 1)
        r = int(255 - t * 20)
        g = int(192 - t * 20)
        b = int(220 + t * 20)
        radius = int(bg_r * (1 - t * 0.02))
        d.ellipse((cx - radius, cy - radius, cx + radius, cy + radius),
                  fill=(r, g, b, 255))

    # 男生头像（左）
    boy_cx = cx - int(size * 0.14)
    boy_cy = cy - int(size * 0.03)
    boy_r = int(size * 0.18)
    d.ellipse((boy_cx - boy_r, boy_cy - boy_r, boy_cx + boy_r, boy_cy + boy_r),
              fill=(245, 208, 184, 255))
    # 男生头发
    hair_r = int(size * 0.18)
    d.ellipse((boy_cx - hair_r, boy_cy - hair_r - int(size*0.01),
               boy_cx + hair_r, boy_cy + int(size*0.02)),
              fill=(45, 45, 50, 255))

    # 女生头像（右）
    girl_cx = cx + int(size * 0.14)
    girl_cy = cy - int(size * 0.03)
    girl_r = int(size * 0.18)
    d.ellipse((girl_cx - girl_r, girl_cy - girl_r, girl_cx + girl_r, girl_cy + girl_r),
              fill=(245, 216, 192, 255))
    # 女生头发
    d.ellipse((girl_cx - hair_r, girl_cy - hair_r - int(size*0.02),
               girl_cx + hair_r, girl_cy + int(size*0.03)),
              fill=(74, 58, 58, 255))
    # 女生侧发
    side_r = int(size * 0.07)
    d.ellipse((girl_cx - girl_r - int(size*0.01), girl_cy + int(size*0.03),
               girl_cx - girl_r + int(size*0.02), girl_cy + girl_r + int(size*0.04)),
              fill=(74, 58, 58, 255))
    d.ellipse((girl_cx + girl_r - int(size*0.02), girl_cy + int(size*0.03),
               girl_cx + girl_r + int(size*0.01), girl_cy + girl_r + int(size*0.04)),
              fill=(74, 58, 58, 255))

    # 心形
    heart_cx = cx
    heart_cy = cy + int(size * 0.18)
    hr = int(size * 0.035)
    d.ellipse((heart_cx - hr*2 - 2, heart_cy - hr,
               heart_cx - 2, heart_cy + hr),
              fill=(255, 130, 170, 255))
    d.ellipse((heart_cx + 2, heart_cy - hr,
               heart_cx + hr*2 + 2, heart_cy + hr),
              fill=(255, 130, 170, 255))
    d.polygon([(heart_cx - hr*2, heart_cy + hr//2),
               (heart_cx + hr*2, heart_cy + hr//2),
               (heart_cx, heart_cy + hr*3)],
              fill=(255, 130, 170, 255))

    # 心形高光
    hl_r = int(size * 0.012)
    d.ellipse((heart_cx - hr, heart_cy - hr//2 - hl_r//2,
               heart_cx - hr + hl_r, heart_cy - hr//2 + hl_r//2),
              fill=(255, 225, 235, 255))

    if with_border:
        border_w = int(size * 0.025)
        for i in range(border_w):
            r = bg_r - i
            d.ellipse((cx - r, cy - r, cx + r, cy + r), outline=(255, 255, 255, 255))

    img = img.filter(ImageFilter.SMOOTH)
    return img


def save_resized(img, path, size):
    resized = img.resize((size, size), Image.LANCZOS)
    resized.save(path, 'PNG', optimize=True)
    print(f'  saved: {path} ({size}x{size})')


if __name__ == '__main__':
    print('=== 生成卡通情侣头像照片 ===')
    boy = draw_boy_avatar(600)
    boy.save(f'{OUT}/images/couple-boy.png', 'PNG', optimize=True)
    print(f'  saved: {OUT}/images/couple-boy.png (600x600)')

    girl = draw_girl_avatar(600)
    girl.save(f'{OUT}/images/couple-girl.png', 'PNG', optimize=True)
    print(f'  saved: {OUT}/images/couple-girl.png (600x600)')

    print('\n=== 生成 PWA 图标 ===')
    icon_master = draw_app_icon(512)
    for sz in [512, 384, 256, 192, 144, 96, 72, 48]:
        save_resized(icon_master, f'{OUT}/icons/icon-{sz}.png', sz)

    # maskable 图标：外边距更大
    maskable = Image.new('RGBA', (512, 512), (0, 0, 0, 0))
    inner = draw_app_icon(int(512 * 0.8), with_border=True)
    px = (512 - inner.width) // 2
    py = (512 - inner.height) // 2
    maskable.paste(inner, (px, py), inner)
    for sz in [512, 192]:
        save_resized(maskable, f'{OUT}/icons/maskable-{sz}.png', sz)

    # favicon
    print('\n=== 生成 favicon ===')
    favicon = draw_app_icon(64, with_border=False)
    favicon.save(f'{OUT}/favicon.png', 'PNG', optimize=True)
    print(f'  saved: {OUT}/favicon.png (64x64)')

    print('\n✅ 所有图片资源生成完成！')
