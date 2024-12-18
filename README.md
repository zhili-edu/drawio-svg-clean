# drawio-svg-clean

> [!NOTE]
> 使用draw.io工具绘制矢量图，在载入Typst项目中时，会发现Typst@0.12对`<foreignObject>`标签进行警告。同时draw.io导出svg时会存放大量的无用数据。

清理draw.io导出SVG图片的小工具。

> 在通义千问的帮助下实现。

## 使用

```bash
python process_svg.py input.svg
```

- 唯一参数：输入svg图片的目录。
- 会在同目录下生成一个增加-trans后缀的文件。

## 主要功能

1. 删除所有的`<foreignObject>`标签
2. 删除第一个标签中content属性（draw.io生成的信息）

---

领导再也不用担心draw.io在我们书里拉了！
