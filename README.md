# AI-Image-Generator

## 项目简介
AI-Image-Generator 是一个基于 Hugging Face Diffusers 的 AI 图像生成工具，支持根据文本描述生成高质量图片。

## 功能特点
- 文本生成图像
- 命令行和 Web 前端展示
- 图片可保存到本地

## 安装依赖
```bash
pip install -r requirements.txt

## 命令行生成
python generate.py --prompt "一只在月光下的猫" --output images/cat.png

## Web 前端
 python app.py
打开浏览器访问 http://localhost:5000
