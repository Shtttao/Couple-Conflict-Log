"""
Couple Conflict Log - Asset Builder
Generates: cartoon avatar photos + PWA app icons (various sizes)
"""
from PIL import Image, ImageDraw, ImageFilter
import math

OUT = '/workspace/public'
AVATAR_DIR = f'{OUT}/images'
ICON_DIR = f'{OUT}/icons'

def create_avatar_boy(size=600):
    """卡通男生头像 - 短黑发、大眼睛、蓝色上衣、浅蓝背景"""
    img = Image.new('RGBA', (size, size), (219, 232, 245, 255))
    d = ImageDraw.Draw(img)
    cx, cy = size // 2, size // 2

    # ---- 上衣（肩膀部分）----
    top_y = cy + int(size * 0.22)
    d.pieslice((cx - int(size*0.55), top_y - int(size*0.35),
                cx + int(size*0.55), top_y + int(size*0.35)),
               180, 360, fill=(107, 139, 168, 255))
    d.rectangle((cx - int(size*0.55), top_y, cx + int(size*0.55), size),
                fill=(107, 139, 168, 255))

    # 领口小三角阴影
    collar_w = int(size * 0.10)
    collar_h = int(size * 0.05)
    d.polygon([(cx - collar_w, top_y), (cx + collar_w, top_y),
               (cx, top_y + collar_h)], fill=(90, 120, 150, 255))

    # 颈部
    neck_w = int(size * 0.11)
    neck_h = int(size * 0.08)
    d.rectangle((cx - neck_w, top_y - neck_h, cx + neck_w, top_y),
                fill=(245, 208, 184, 255))

    # ---- 头部（脸）----
    face_rx = int(size * 0.28)
    face_ry = int(size * 0.32)
    face_top = cy - int(size * 0.25)
    face_bottom = cy + int(size * 0.22)
    d.ellipse((cx - face_rx, face_top, cx + face_rx, face_bottom),
              fill=(245, 208, 184, 255))

    # 耳朵
    ear_w = int(size * 0.05)
    ear_h = int(size * 0.085)
    ear_y = cy - int(size * 0.05)
    d.ellipse((cx - face_rx - ear_w, ear_y - ear_h,
               cx - face_rx + ear_w, ear_y + ear_h),
              fill=(245, 208, 184, 255))
    d.ellipse((cx + face_rx - ear_w, ear_y - ear_h,
               cx + face_rx + ear_w, ear_y + ear_h),
              fill=(245, 208, 184, 255))

    # ---- 头发（头顶蓬松）----
    # 主体圆帽状
    hair_top = face_top - int(size * 0.10)
    hair_bottom_y = face_top + int(size * 0.14)
    d.ellipse((cx - int(size*0.32), hair_top,
               cx + int(size*0.32), hair_bottom_y + int(size*0.05)),
              fill=(45, 45, 45, 255))

    # 蓬松的两侧（圆形堆叠营造蓬松感）
    puff_r = int(size * 0.08)
    for (dx, dy, r_factor) in [
        (-0.28, -0.12, 1.0), (-0.22, -0.20, 0.95), (-0.15, -0.25, 0.9),
        (0.0, -0.28, 0.95), (0.15, -0.25, 0.9), (0.22, -0.20, 0.95),
        (0.28, -0.12, 1.0), (-0.30, 0.0, 0.85), (0.30, 0.0, 0.85),
        (-0.08, -0.30, 0.85), (0.08, -0.30, 0.85),
    ]:
        px = cx + int(size * dx)
        py = hair_bottom_y + int(size * dy)
        r = int(puff_r * r_factor)
        d.ellipse((px - r, py - r, px + r, py + r), fill=(45, 45, 45, 255))

    # 刘海（覆盖额头，中间略短两侧略长）
    bang_bot_y = face_top + int(size * 0.14)
    # 主刘海
    d.ellipse((cx - int(size*0.28), face_top - int(size*0.02),
               cx + int(size*0.28), bang_bot_y),
              fill=(38, 38, 38, 255))
    # 刘海发梢细节（波浪形）
    for i in range(-3, 4):
        bx = cx + int(size * 0.09 * i)
        by = bang_bot_y - int(size * 0.01)
        br = int(size * 0.035)
        d.ellipse((bx - br, by - br, bx + br, by + br), fill=(42, 42, 42, 255))

    # 头顶高光（几个小亮点表现光泽）
    hl_color = (70, 70, 70, 160)
    for (dx, dy) in [(-0.15, -0.18), (-0.08, -0.22), (0.05, -0.20),
                     (0.12, -0.17), (-0.20, -0.10), (0.18, -0.08)]:
        hx = cx + int(size * dx)
        hy = hair_bottom_y + int(size * dy)
        hr = int(size * 0.012)
        d.ellipse((hx - hr, hy - hr, hx + hr, hy + hr), fill=hl_color)

    # ---- 眉毛 ----
    brow_y = face_top + int(size * 0.14)
    brow_dist = int(size * 0.12)
    brow_w = int(size * 0.08)
    brow_thick = int(size * 0.012)
    # 左眉
    d.ellipse((cx - brow_dist - brow_w, brow_y - brow_thick,
               cx - brow_dist + brow_w, brow_y + brow_thick),
              fill=(38, 38, 38, 255))
    # 右眉
    d.ellipse((cx + brow_dist - brow_w, brow_y - brow_thick,
               cx + brow_dist + brow_w, brow_y + brow_thick),
              fill=(38, 38, 38, 255))

    # ---- 眼睛（大圆可爱眼）----
    eye_cx_dist = int(size * 0.12)
    eye_y = face_top + int(size * 0.22)
    eye_rx = int(size * 0.045)
    eye_ry = int(size * 0.050)

    for sign in [-1, 1]:
        ex = cx + sign * eye_cx_dist
        # 眼球（黑色）
        d.ellipse((ex - eye_rx, eye_y - eye_ry,
                   ex + eye_rx, eye_y + eye_ry),
                  fill=(38, 38, 38, 255))
        # 下半部深灰/蓝阴影（让眼睛有层次）
        d.ellipse((ex - eye_rx + int(size*0.005), eye_y - eye_ry + int(size*0.005),
                   ex + eye_rx - int(size*0.005), eye_y + int(size*0.015)),
                  fill=(58, 58, 58, 255))
        # 主高光（白色大圆）
        hl1_rx = int(size * 0.018)
        hl1_ry = int(size * 0.022)
        hl1_x = ex - int(size * 0.012)
        hl1_y = eye_y - int(size * 0.022)
        d.ellipse((hl1_x - hl1_rx, hl1_y - hl1_ry,
                   hl1_x + hl1_rx, hl1_y + hl1_ry),
                  fill=(255, 255, 255, 255))
        # 小高光
        hl2_r = int(size * 0.008)
        hl2_x = ex + int(size * 0.015)
        hl2_y = eye_y + int(size * 0.015)
        d.ellipse((hl2_x - hl2_r, hl2_y - hl2_r,
                   hl2_x + hl2_r, hl2_y + hl2_r),
                  fill=(255, 255, 255, 240))

    # ---- 腮红 ----
    blush_rx = int(size * 0.055)
    blush_ry = int(size * 0.028)
    blush_y = eye_y + int(size * 0.05)
    blush_dist = int(size * 0.17)
    # 用淡粉色半透明实现
    blush_img = Image.new('RGBA', (size, size), (0, 0, 0, 0))
    blush_d = ImageDraw.Draw(blush_img)
    blush_d.ellipse((cx - blush_dist - blush_rx, blush_y - blush_ry,
                     cx - blush_dist + blush_rx, blush_y + blush_ry),
                    fill=(255, 184, 184, 140))
    blush_d.ellipse((cx + blush_dist - blush_rx, blush_y - blush_ry,
                     cx + blush_dist + blush_rx, blush_y + blush_ry),
                    fill=(255, 184, 184, 140))
    img = Image.alpha_composite(img, blush_img)
    d = ImageDraw.Draw(img)

    # ---- 微笑嘴巴 ----
    mouth_y = face_top + int(size * 0.36)
    mouth_w = int(size * 0.05)
    mouth_ry = int(size * 0.025)
    d.arc((cx - mouth_w, mouth_y - mouth_ry,
           cx + mouth_w, mouth_y + mouth_ry),
          0, 180, fill=(192, 112, 112, 255), width=int(size*0.01))

    return img


def create_avatar_girl(size=600):
    """卡通女生头像 - 长卷发、大眼睛、白色上衣+心形项链、米色背景"""
    img = Image.new('RGBA', (size, size), (245, 235, 220, 255))
    d = ImageDraw.Draw(img)
    cx, cy = size // 2, size // 2

    # ---- 背后的长发（先画，在身体之后被覆盖）----
    # 左侧大量头发
    left_hair_x = cx - int(size * 0.10)
    for (dx, dy, w, h) in [
        (-0.18, -0.05, 0.15, 0.30),
        (-0.28, 0.05, 0.12, 0.40),
        (-0.25, 0.25, 0.14, 0.28),
        (-0.18, 0.40, 0.15, 0.22),
        (-0.08, 0.45, 0.10, 0.18),
    ]:
        px = cx + int(size * dx)
        py = cy + int(size * dy)
        pw = int(size * w)
        ph = int(size * h)
        d.ellipse((px - pw, py - ph, px + pw, py + ph), fill=(74, 58, 58, 255))

    # 右侧大量头发
    for (dx, dy, w, h) in [
        (0.18, -0.05, 0.15, 0.30),
        (0.28, 0.05, 0.12, 0.40),
        (0.25, 0.25, 0.14, 0.28),
        (0.18, 0.40, 0.15, 0.22),
        (0.08, 0.45, 0.10, 0.18),
    ]:
        px = cx + int(size * dx)
        py = cy + int(size * dy)
        pw = int(size * w)
        ph = int(size * h)
        d.ellipse((px - pw, py - ph, px + pw, py + ph), fill=(74, 58, 58, 255))

    # ---- 上衣 ----
    top_y = cy + int(size * 0.22)
    # 肩膀/身体
    d.pieslice((cx - int(size*0.55), top_y - int(size*0.32),
                cx + int(size*0.55), top_y + int(size*0.35)),
               180, 360, fill=(232, 220, 200, 255))
    d.rectangle((cx - int(size*0.55), top_y, cx + int(size*0.55), size),
                fill=(232, 220, 200, 255))

    # 领口三角
    collar_w = int(size * 0.10)
    collar_h = int(size * 0.045)
    d.polygon([(cx - collar_w, top_y), (cx + collar_w, top_y),
               (cx, top_y + collar_h)], fill=(210, 195, 175, 255))

    # 心形项链
    heart_cx = cx
    heart_cy = top_y + int(size * 0.12)
    heart_size = int(size * 0.035)
    # 心形：两个圆 + 三角
    heart_img = Image.new('RGBA', (size, size), (0, 0, 0, 0))
    hd = ImageDraw.Draw(heart_img)
    # 左上圆
    hr = heart_size
    hd.ellipse((heart_cx - hr*2 - 2, heart_cy - hr,
                heart_cx - 2, heart_cy + hr),
               fill=(255, 156, 181, 255))
    # 右上圆
    hd.ellipse((heart_cx + 2, heart_cy - hr,
                heart_cx + hr*2 + 2, heart_cy + hr),
               fill=(255, 156, 181, 255))
    # 三角下半
    hd.polygon([(heart_cx - hr*2, heart_cy + hr//2),
                (heart_cx + hr*2, heart_cy + hr//2),
                (heart_cx, heart_cy + hr*2 + int(size*0.008))],
               fill=(255, 156, 181, 255))
    # 心形边框
    hd.ellipse((heart_cx - hr*2 - 2, heart_cy - hr,
                heart_cx - 2, heart_cy + hr),
               outline=(216, 120, 150, 255), width=int(size*0.004))
    hd.ellipse((heart_cx + 2, heart_cy - hr,
                heart_cx + hr*2 + 2, heart_cy + hr),
               outline=(216, 120, 150, 255), width=int(size*0.004))
    img = Image.alpha_composite(img, heart_img)
    d = ImageDraw.Draw(img)

    # 颈部
    neck_w = int(size * 0.10)
    neck_h = int(size * 0.08)
    d.rectangle((cx - neck_w, top_y - neck_h, cx + neck_w, top_y),
                fill=(245, 216, 192, 255))

    # ---- 头部（脸）----
    face_rx = int(size * 0.27)
    face_ry = int(size * 0.31)
    face_top = cy - int(size * 0.24)
    face_bottom = cy + int(size * 0.21)
    d.ellipse((cx - face_rx, face_top, cx + face_rx, face_bottom),
              fill=(245, 216, 192, 255))

    # 耳朵
    ear_w = int(size * 0.05)
    ear_h = int(size * 0.08)
    ear_y = cy - int(size * 0.04)
    d.ellipse((cx - face_rx - ear_w, ear_y - ear_h,
               cx - face_rx + ear_w, ear_y + ear_h),
              fill=(245, 216, 192, 255))
    d.ellipse((cx + face_rx - ear_w, ear_y - ear_h,
               cx + face_rx + ear_w, ear_y + ear_h),
              fill=(245, 216, 192, 255))

    # ---- 头发（顶部蓬松）----
    hair_top = face_top - int(size * 0.14)
    hair_bot = face_top + int(size * 0.15)
    d.ellipse((cx - int(size*0.34), hair_top,
               cx + int(size*0.34), hair_bot + int(size*0.04)),
              fill=(74, 58, 58, 255))

    # 蓬松堆叠
    for (dx, dy, r_factor) in [
        (-0.30, -0.12, 1.05), (-0.24, -0.22, 0.98), (-0.15, -0.28, 0.92),
        (0.0, -0.32, 0.92), (0.15, -0.28, 0.92), (0.24, -0.22, 0.98),
        (0.30, -0.12, 1.05), (-0.32, -0.02, 0.88), (0.32, -0.02, 0.88),
        (-0.08, -0.34, 0.82), (0.08, -0.34, 0.82),
        (-0.34, 0.08, 0.78), (0.34, 0.08, 0.78),
    ]:
        px = cx + int(size * dx)
        py = hair_bot + int(size * dy)
        r = int(size * 0.085 * r_factor)
        d.ellipse((px - r, py - r, px + r, py + r), fill=(74, 58, 58, 255))

    # ---- 刘海（覆盖额头）----
    bang_bot = face_top + int(size * 0.15)
    d.ellipse((cx - int(size*0.30), face_top - int(size*0.04),
               cx + int(size*0.30), bang_bot),
              fill=(58, 42, 42, 255))
    # 刘海波浪发梢
    for i in range(-4, 5):
        bx = cx + int(size * 0.075 * i)
        by = bang_bot - int(size * 0.005)
        br = int(size * 0.032)
        d.ellipse((bx - br, by - br, bx + br, by + br), fill=(58, 42, 42, 255))

    # 头顶高光
    hl_color = (120, 110, 110, 150)
    for (dx, dy) in [(-0.15, -0.22), (-0.05, -0.28), (0.08, -0.24),
                     (0.18, -0.18), (-0.22, -0.12), (0.22, -0.10),
                     (-0.30, 0.02), (0.28, 0.04)]:
        hx = cx + int(size * dx)
        hy = hair_bot + int(size * dy)
        hr = int(size * 0.012)
        d.ellipse((hx - hr, hy - hr, hx + hr, hy + hr), fill=hl_color)

    # ---- 眉毛 ----
    brow_y = face_top + int(size * 0.14)
    brow_dist = int(size * 0.12)
    brow_w = int(size * 0.075)
    brow_thick = int(size * 0.012)
    d.ellipse((cx - brow_dist - brow_w, brow_y - brow_thick,
               cx - brow_dist + brow_w, brow_y + brow_thick),
              fill=(58, 42, 42, 255))
    d.ellipse((cx + brow_dist - brow_w, brow_y - brow_thick,
               cx + brow_dist + brow_w, brow_y + brow_thick),
              fill=(58, 42, 42, 255))

    # ---- 眼睛 ----
    eye_cx_dist = int(size * 0.115)
    eye_y = face_top + int(size * 0.22)
    eye_rx = int(size * 0.045)
    eye_ry = int(size * 0.052)

    for sign in [-1, 1]:
        ex = cx + sign * eye_cx_dist
        # 眼球
        d.ellipse((ex - eye_rx, eye_y - eye_ry,
                   ex + eye_rx, eye_y + eye_ry),
                  fill=(42, 42, 42, 255))
        # 内层阴影
        d.ellipse((ex - eye_rx + int(size*0.005), eye_y - eye_ry + int(size*0.005),
                   ex + eye_rx - int(size*0.005), eye_y + eye_ry),
                  fill=(60, 52, 52, 255))
        # 主高光
        hl1_rx = int(size * 0.018)
        hl1_ry = int(size * 0.024)
        hl1_x = ex - int(size * 0.014)
        hl1_y = eye_y - int(size * 0.024)
        d.ellipse((hl1_x - hl1_rx, hl1_y - hl1_ry,
                   hl1_x + hl1_rx, hl1_y + hl1_ry),
                  fill=(255, 255, 255, 255))
        # 小高光
        hl2_r = int(size * 0.009)
        hl2_x = ex + int(size * 0.014)
        hl2_y = eye_y + int(size * 0.016)
        d.ellipse((hl2_x - hl2_r, hl2_y - hl2_r,
                   hl2_x + hl2_r, hl2_y + hl2_r),
                  fill=(255, 255, 255, 230))

    # ---- 腮红 ----
    blush_rx = int(size * 0.06)
    blush_ry = int(size * 0.03)
    blush_y = eye_y + int(size * 0.05)
    blush_dist = int(size * 0.17)

    blush_img = Image.new('RGBA', (size, size), (0, 0, 0, 0))
    blush_d = ImageDraw.Draw(blush_img)
    blush_d.ellipse((cx - blush_dist - blush_rx, blush_y - blush_ry,
                     cx - blush_dist + blush_rx, blush_y + blush_ry),
                    fill=(255, 184, 184, 150))
    blush_d.ellipse((cx + blush_dist - blush_rx, blush_y - blush_ry,
                     cx + blush_dist + blush_rx, blush_y + blush_ry),
                    fill=(255, 184, 184, 150))
    img = Image.alpha_composite(img, blush_img)
    d = ImageDraw.Draw(img)

    # ---- 微笑嘴 ----
    mouth_y = face_top + int(size * 0.36)
    mouth_w = int(size * 0.048)
    mouth_ry = int(size * 0.022)
    d.arc((cx - mouth_w, mouth_y - mouth_ry,
           cx + mouth_w, mouth_y + mouth_ry),
          0, 180, fill=(192, 112, 112, 255), width=int(size*0.01))

    return img


def create_app_icon(size=512):
    """PWA应用图标 - 粉色圆背景+双人头像+心形"""
    img = Image.new('RGBA', (size, size), (0, 0, 0, 0))
    d = ImageDraw.Draw(img)

    # 圆形渐变背景（模拟）
    # 外层粉色圆
    bg_r = int(size * 0.48)
    cx, cy = size // 2, size // 2
    # 径向渐变由多层圆实现
    layers = 18
    for i in range(layers):
        t = i / (layers - 1)
        # 从浅粉到淡紫
        r = int(255 - t * 40)
        g = int(192 - t * 30)
        b = int(220 + t * 20)
        radius = int(bg_r * (1 - t * 0.02))
        d.ellipse((cx - radius, cy - radius, cx + radius, cy + radius),
                  fill=(r, g, b, 255))

    # 绘制迷你双人头像（简化版）
    # 男生头（左侧，小）
    mini_size = int(size * 0.22)
    boy_cx = cx - int(size * 0.14)
    boy_cy = cy - int(size * 0.02)
    # 男生脸
    d.ellipse((boy_cx - mini_size, boy_cy - mini_size,
               boy_cx + mini_size, boy_cy + mini_size),
              fill=(245, 208, 184, 255))
    # 男生头发
    d.ellipse((boy_cx - mini_size, boy_cy - mini_size - int(size*0.01),
               boy_cx + mini_size, boy_cy + int(size*0.02)),
              fill=(45, 45, 45, 255))

    # 女生头（右侧，小）
    girl_cx = cx + int(size * 0.14)
    girl_cy = cy - int(size * 0.02)
    d.ellipse((girl_cx - mini_size, girl_cy - mini_size,
               girl_cx + mini_size, girl_cy + mini_size),
              fill=(245, 216, 192, 255))
    # 女生头发（更多）
    d.ellipse((girl_cx - mini_size, girl_cy - mini_size - int(size*0.02),
               girl_cx + mini_size, girl_cy + int(size*0.03)),
              fill=(74, 58, 58, 255))
    # 女生长发两侧
    hair_side_r = int(size * 0.07)
    d.ellipse((girl_cx - mini_size - int(size*0.03), girl_cy + int(size*0.03),
               girl_cx - mini_size + int(size*0.02), girl_cy + mini_size + int(size*0.04)),
              fill=(74, 58, 58, 255))
    d.ellipse((girl_cx + mini_size - int(size*0.02), girl_cy + int(size*0.03),
               girl_cx + mini_size + int(size*0.03), girl_cy + mini_size + int(size*0.04)),
              fill=(74, 58, 58, 255))

    # 中间的心形
    heart_size = int(size * 0.08)
    hcx, hcy = cx, cy + int(size * 0.12)
    # 心形：两圆+三角
    hr = heart_size // 3
    d.ellipse((hcx - hr*2 - 2, hcy - hr, hcx - 2, hcy + hr), fill=(255, 120, 160, 255))
    d.ellipse((hcx + 2, hcy - hr, hcx + hr*2 + 2, hcy + hr), fill=(255, 120, 160, 255))
    d.polygon([(hcx - hr*2, hcy), (hcx + hr*2, hcy),
               (hcx, hcy + hr*3)], fill=(255, 120, 160, 255))

    # 心形高光
    hl_r = int(size * 0.012)
    d.ellipse((hcx - hr, hcy - hr//2, hcx - hr + hl_r*2, hcy - hr//2 + hl_r*2),
              fill=(255, 220, 235, 255))

    # 边框白色描边
    border_w = int(size * 0.025)
    for i in range(border_w):
        r = bg_r - i
        d.ellipse((cx - r, cy - r, cx + r, cy + r), outline=(255, 255, 255, 255))

    # 添加一点柔和模糊效果
    img = img.filter(ImageFilter.SMOOTH)
    return img


def save_resized(img, path, size):
    """将图片缩放到指定尺寸并保存为PNG"""
    resized = img.resize((size, size), Image.LANCZOS)
    resized.save(path, 'PNG', optimize=True)
    print(f"  saved: {path} ({size}x{size})")


if __name__ == '__main__':
    import os
    os.makedirs(AVATAR_DIR, exist_ok=True)
    os.makedirs(ICON_DIR, exist_ok=True)

    # 1. 生成头像照片
    print("=== 生成卡通头像照片 ===")
    boy = create_avatar_boy(600)
    save_resized(boy, f'{AVATAR_DIR}/couple-boy.png', 600)

    girl = create_avatar_girl(600)
    save_resized(girl, f'{AVATAR_DIR}/couple-girl.png', 600)

    # 2. 生成 PWA 图标
    print("\n=== 生成 PWA 应用图标 ===")
    icon_master = create_app_icon(512)
    for sz in [512, 384, 256, 192, 144, 96, 72, 48]:
        save_resized(icon_master, f'{ICON_DIR}/icon-{sz}.png', sz)

    # 3. 生成适配 iOS/maskable 的图标（带更多外边距）
    print("\n=== 生成 maskable 图标 ===")
    # 在 512 基础上，中心裁剪后外围加透明边距（通过 resize 到更小的位置）
    maskable = Image.new('RGBA', (512, 512), (0, 0, 0, 0))
    inner = create_app_icon(int(512 * 0.8))
    px = (512 - inner.width) // 2
    py = (512 - inner.height) // 2
    maskable.paste(inner, (px, py), inner)
    for sz in [512, 192]:
        save_resized(maskable, f'{ICON_DIR}/maskable-{sz}.png', sz)

    # 4. 生成 favicon
    print("\n=== 生成 favicon ===")
    favicon = create_app_icon(64)
    favicon.save(f'{OUT}/favicon.png', 'PNG', optimize=True)
    print(f"  saved: {OUT}/favicon.png (64x64)")

    print("\n✅ 所有资源生成完成！")
