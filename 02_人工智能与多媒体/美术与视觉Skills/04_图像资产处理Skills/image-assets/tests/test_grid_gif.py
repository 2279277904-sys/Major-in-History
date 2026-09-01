#!/usr/bin/env python3
import sys
import tempfile
import unittest
from pathlib import Path

import numpy as np
from PIL import Image, ImageDraw

SCRIPTS_DIR = Path(__file__).resolve().parents[1] / "scripts"
sys.path.insert(0, str(SCRIPTS_DIR))

import grid_gif


class GridGifTest(unittest.TestCase):
    def build_sheet(self) -> Image.Image:
        sheet = Image.new("RGB", (41, 41), (0, 13, 47))
        draw = ImageDraw.Draw(sheet)
        separator = (0, 220, 255)
        draw.rectangle((0, 0, 40, 2), fill=separator)
        draw.rectangle((0, 19, 40, 21), fill=separator)
        draw.rectangle((0, 38, 40, 40), fill=separator)
        draw.rectangle((0, 0, 2, 40), fill=separator)
        draw.rectangle((19, 0, 21, 40), fill=separator)
        draw.rectangle((38, 0, 40, 40), fill=separator)
        colors = [(255, 80, 40), (40, 220, 80), (60, 120, 255), (255, 210, 40)]
        for index, color in enumerate(colors):
            column = index % 2
            row = index // 2
            left = 3 + column * 19
            top = 3 + row * 19
            draw.rectangle((left + 4, top + 4, left + 11, top + 11), fill=color)
        return sheet

    def test_split_grid_removes_separator(self) -> None:
        frames, metadata = grid_gif.split_grid(self.build_sheet(), 2, 2, "auto", 8.0, 20.0, "row-major")
        self.assertEqual([(16, 16)] * 4, [frame.size for frame in frames], "切帧尺寸不正确")
        separator = np.array([0, 220, 255], dtype=np.uint8)
        for frame in frames:
            rgb = np.asarray(frame.convert("RGB"), dtype=np.uint8)
            self.assertFalse(np.any(np.all(rgb == separator, axis=2)), "切帧后仍残留分隔线")
        self.assertEqual((19, 21), metadata["vertical_separator_bands"][1], "未识别中间竖线")

    def test_color_cutout_only_removes_edge_background(self) -> None:
        image = Image.new("RGBA", (9, 9), (0, 13, 47, 255))
        draw = ImageDraw.Draw(image)
        draw.rectangle((2, 2, 6, 6), fill=(255, 90, 30, 255))
        draw.point((4, 4), fill=(0, 13, 47, 255))
        cutout = grid_gif.color_cutout(image, (0, 13, 47), 10.0, 0.0)
        alpha = cutout.getchannel("A")
        self.assertEqual(0, alpha.getpixel((0, 0)), "边缘背景没有变透明")
        self.assertEqual(255, alpha.getpixel((4, 4)), "主体内部同色像素被错误抠除")

    def test_conservative_chroma_key_preserves_dark_clothing(self) -> None:
        image = Image.new("RGBA", (24, 24), (0, 13, 47, 255))
        ImageDraw.Draw(image).rectangle((6, 5, 17, 20), fill=(20, 25, 35, 255))
        cutout = grid_gif.color_cutout(image, (0, 13, 47), 12.0, 0.0)
        self.assertEqual(0, cutout.getchannel("A").getpixel((0, 0)), "深蓝背景没有变透明")
        self.assertEqual(255, cutout.getchannel("A").getpixel((10, 10)), "深色衣物被误删")
        self.assertEqual((255, 0, 255), cutout.getpixel((0, 0))[:3], "透明背景没有先替换为键色")

    def test_color_cutout_removes_thin_edge_artifact(self) -> None:
        image = Image.new("RGBA", (32, 32), (0, 13, 47, 255))
        draw = ImageDraw.Draw(image)
        draw.line((0, 0, 31, 0), fill=(0, 0, 0, 255), width=1)
        draw.rectangle((8, 6, 23, 26), fill=(255, 80, 30, 255))
        cutout = grid_gif.color_cutout(image, (0, 13, 47), 12.0, 0.0)
        self.assertEqual(0, cutout.getchannel("A").getpixel((16, 0)), "画布边缘细线没有清理")
        self.assertEqual(255, cutout.getchannel("A").getpixel((16, 16)), "主体被边缘清理误删")

    def test_save_transparent_gif(self) -> None:
        frames = []
        for color in [(255, 0, 0), (0, 255, 0)]:
            frame = Image.new("RGBA", (12, 12), (0, 0, 0, 0))
            ImageDraw.Draw(frame).rectangle((3, 3, 8, 8), fill=(*color, 255))
            frames.append(frame)
        with tempfile.TemporaryDirectory() as temporary_dir:
            output = Path(temporary_dir) / "测试.gif"
            grid_gif.save_gif(frames, output, 90, 0)
            with Image.open(output) as result:
                self.assertEqual(2, result.n_frames, "GIF 帧数不正确")
                self.assertEqual(90, result.info["duration"], "GIF 帧时长不正确")
                self.assertEqual(0, result.convert("RGBA").getchannel("A").getpixel((0, 0)), "GIF 背景不透明")

    def test_feet_anchor_alignment(self) -> None:
        first = Image.new("RGBA", (20, 20), (0, 0, 0, 0))
        second = Image.new("RGBA", (20, 20), (0, 0, 0, 0))
        ImageDraw.Draw(first).rectangle((2, 4, 9, 16), fill=(255, 80, 30, 255))
        ImageDraw.Draw(second).rectangle((8, 1, 15, 13), fill=(255, 80, 30, 255))
        normalized, metadata = grid_gif.normalize_frames([first, second], 1, "feet", 32, 0.2)
        anchors = [grid_gif.detect_anchor(frame, "feet", 32, 0.2) for frame in normalized]
        self.assertEqual(anchors[0], anchors[1], "脚部锚点没有对齐到同一坐标")
        self.assertEqual(tuple(metadata["target_anchor"]), anchors[0], "清单中的目标锚点不正确")

    def test_feet_anchor_ignores_edge_noise_and_tail(self) -> None:
        first = Image.new("RGBA", (32, 32), (0, 0, 0, 0))
        second = Image.new("RGBA", (32, 32), (0, 0, 0, 0))
        first_draw = ImageDraw.Draw(first)
        second_draw = ImageDraw.Draw(second)
        first_draw.rectangle((6, 5, 16, 22), fill=(255, 80, 30, 255))
        first_draw.rectangle((5, 23, 9, 27), fill=(255, 80, 30, 255))
        first_draw.rectangle((13, 23, 17, 27), fill=(255, 80, 30, 255))
        first_draw.rectangle((21, 12, 27, 18), fill=(255, 80, 30, 255))
        first_draw.point((31, 31), fill=(255, 255, 255, 255))
        second_draw.rectangle((10, 5, 20, 22), fill=(255, 80, 30, 255))
        second_draw.rectangle((9, 23, 13, 27), fill=(255, 80, 30, 255))
        second_draw.rectangle((17, 23, 21, 27), fill=(255, 80, 30, 255))
        second_draw.rectangle((25, 12, 31, 18), fill=(255, 80, 30, 255))
        second_draw.point((0, 31), fill=(255, 255, 255, 255))
        self.assertEqual((11, 27), grid_gif.detect_anchor(first, "feet", 32, 0.08), "第一帧脚部锚点错误")
        self.assertEqual((15, 27), grid_gif.detect_anchor(second, "feet", 32, 0.08), "第二帧脚部锚点错误")
        normalized, _ = grid_gif.normalize_frames([first, second], 1, "feet", 32, 0.08)
        body_centers = []
        for frame in normalized:
            alpha = np.asarray(frame.getchannel("A"), dtype=np.uint8)
            ys, xs = np.nonzero(alpha >= 32)
            body_pixels = xs[ys < ys.min() + 18]
            body_centers.append((int(body_pixels.min()) + int(body_pixels.max())) // 2)
        self.assertEqual(body_centers[0], body_centers[1], "横向对齐后主体中心仍在抖动")

    def test_ping_pong_playback_order(self) -> None:
        frames = [Image.new("RGBA", (1, 1), (index, 0, 0, 255)) for index in range(4)]
        playback_frames, playback_order = grid_gif.build_playback_frames(frames, "ping-pong")
        self.assertEqual([1, 2, 3, 4, 3, 2], playback_order, "往返播放序列不正确")
        self.assertEqual(6, len(playback_frames), "往返播放帧数不正确")

    def test_forward_playback_order(self) -> None:
        frames = [Image.new("RGBA", (1, 1), (index, 0, 0, 255)) for index in range(4)]
        _, playback_order = grid_gif.build_playback_frames(frames, "forward")
        self.assertEqual([1, 2, 3, 4], playback_order, "正向播放序列不正确")

    def test_make_alignment_preview(self) -> None:
        frames = [Image.new("RGBA", (20, 20), (0, 0, 0, 0)) for _ in range(4)]
        for frame in frames:
            ImageDraw.Draw(frame).rectangle((7, 5, 12, 17), fill=(255, 80, 30, 255))
        with tempfile.TemporaryDirectory() as temporary_dir:
            output = Path(temporary_dir) / "逐帧检查板.png"
            grid_gif.make_alignment_preview(frames, (9, 17), output)
            self.assertTrue(output.is_file(), "没有生成逐帧对齐检查板")
            with Image.open(output) as preview:
                self.assertEqual((960, 268), preview.size, "逐帧对齐检查板尺寸不正确")

    def test_make_gif_checker_preview(self) -> None:
        frames = []
        for color in [(255, 0, 0), (0, 255, 0)]:
            frame = Image.new("RGBA", (12, 12), (0, 0, 0, 0))
            ImageDraw.Draw(frame).rectangle((3, 3, 8, 8), fill=(*color, 255))
            frames.append(frame)
        with tempfile.TemporaryDirectory() as temporary_dir:
            gif_path = Path(temporary_dir) / "透明.gif"
            preview_path = Path(temporary_dir) / "棋盘格.gif"
            grid_gif.save_gif(frames, gif_path, 90, 0)
            grid_gif.make_gif_checker_preview(gif_path, preview_path)
            with Image.open(preview_path) as preview:
                self.assertEqual(2, preview.n_frames, "棋盘格 GIF 帧数不正确")


if __name__ == "__main__":
    unittest.main()
