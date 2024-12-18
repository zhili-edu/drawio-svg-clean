import xml.etree.ElementTree as ET
import argparse
import os

def remove_foreign_objects(svg_input_path, svg_output_path):
    # 解析SVG文件
    tree = ET.parse(svg_input_path)
    root = tree.getroot()

    # 定义SVG命名空间（如果存在的话）
    svg_namespace = 'http://www.w3.org/2000/svg'
    namespaces = {'svg': svg_namespace }

    # 创建一个字典来存储每个节点的父节点
    parent_map = {c: p for p in tree.iter() for c in p}

    # 查找所有的<foreignObject>标签并删除它们
    for foreign_object in root.findall('.//svg:foreignObject', namespaces):
        parent = parent_map.get(foreign_object)
        if parent is not None:
            parent.remove(foreign_object)

    # 移除命名空间前缀
    def remove_namespace(tag):
        return tag.split('}', 1)[1] if '}' in tag else tag

    # 遍历所有元素并移除命名空间前缀
    for elem in tree.iter():
        elem.tag = remove_namespace(elem.tag)
        elem.attrib = {remove_namespace(k): v for k, v in elem.attrib.items()}

    # 删除第一个标签中的content属性（如果有）
    if 'content' in root.attrib:
        del root.attrib['content']

    # 确保根元素包含正确的命名空间声明
    if 'xmlns' not in root.attrib:
        root.set('xmlns', svg_namespace)

    # 将修改后的SVG写入到新的文件中
    tree.write(svg_output_path, encoding='utf-8')

def main():
    # 创建ArgumentParser对象
    parser = argparse.ArgumentParser(description='Process an SVG file by removing foreignObject tags and the content attribute from the root.')
    parser.add_argument('input_svg', type=str, help='Path to the input SVG file')

    # 解析命令行参数
    args = parser.parse_args()

    # 获取输入文件路径
    input_svg_file = args.input_svg

    # 检查输入文件是否存在
    if not os.path.isfile(input_svg_file):
        print(f"Error: The input file '{input_svg_file}' does not exist.")
        return

    # 获取输入文件的目录和文件名
    input_dir = os.path.dirname(input_svg_file)
    input_filename = os.path.basename(input_svg_file)

    # 构建输出文件路径
    output_filename = os.path.splitext(input_filename)[0] + '-trans.svg'
    output_svg_file = os.path.join(input_dir, output_filename)

    # 处理SVG文件
    remove_foreign_objects(input_svg_file, output_svg_file)
    print(f"Processed SVG saved to '{output_svg_file}'")

if __name__ == '__main__':
    main()