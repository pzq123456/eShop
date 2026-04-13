from pathlib import Path
from docling.datamodel.base_models import InputFormat
from docling.datamodel.pipeline_options import PdfPipelineOptions
from docling.document_converter import DocumentConverter, PdfFormatOption

def main():
    # 1. 配置路径
    source = "data/test.pdf"
    output_dir = Path("output")
    output_dir.mkdir(parents=True, exist_ok=True)

    # 2. 配置转换选项
    # 启用 OCR 和 图片提取功能
    pipeline_options = PdfPipelineOptions()
    pipeline_options.do_ocr = True  # 开启 OCR
    pipeline_options.do_table_structure = True  # 优化表格识别
    pipeline_options.images_scale = 2.0  # 设置图片缩放比例，提高清晰度
    pipeline_options.generate_page_images = False # 是否生成全页扫描图（通常不需要）

    # 3. 初始化转换器
    # 显式指定针对 PDF 的处理选项
    converter = DocumentConverter(
        format_options={
            InputFormat.PDF: PdfFormatOption(pipeline_options=pipeline_options)
        }
    )

    print(f"正在转换文件: {source} ...")

    # 4. 执行转换
    result = converter.convert(source)

    # 5. 导出 Markdown
    md_content = result.document.export_to_markdown()
    
    # 保存结果到文件
    output_path = output_dir / "test.md"
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(md_content)

    print(f"转换成功！Markdown 已保存至: {output_path}")

if __name__ == "__main__":
    main()