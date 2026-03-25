# XTTS Project

## 功能
- 从 PDF 表格提取第一列
- 按页生成语音
- 该版本仅生成英音语音，调用XTTS开源模型
- 仅个人使用，不发布release版本

## 流程
PDF → 表格解析 → 文本 → XTTS → 音频

## 使用方法
```bash
pip install -r requirements.txt
python main.py
```

---

## 冻结依赖

```bash
pip freeze > requirements.txt
```
