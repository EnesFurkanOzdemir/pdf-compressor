import subprocess
import os
import sys
from tkinter import filedialog, messagebox, Tk

def compress_pdf(input_path, output_path, max_size_mb=10):
    try:
        exe_dir = os.path.dirname(sys.executable)
        gs_path = os.path.join(exe_dir, "gswin64c.exe")

        gs_command = [
            gs_path,
            "-sDEVICE=pdfwrite",
            "-dCompatibilityLevel=1.4",
            "-dNOPAUSE",
            "-dQUIET",
            "-dBATCH",
            "-dPDFSETTINGS=/ebook",
            "-dDownsampleColorImages=true",
            "-dColorImageResolution=150",
            "-dDownsampleGrayImages=true",
            "-dGrayImageResolution=150",
            "-dDownsampleMonoImages=true",
            "-dMonoImageResolution=150",
            f"-sOutputFile={output_path}",
            input_path
        ]

        subprocess.run(gs_command, check=True)

        size_mb = os.path.getsize(output_path) / (1024 * 1024)
        message = f"Sıkıştırılan dosya boyutu: {size_mb:.2f} MB\n"

        if size_mb > max_size_mb:
            message += f"⚠ Dosya {size_mb:.2f} MB oldu, 10 MB sınırını geçti!"
        else:
            message += f"✅ Başarılı! {size_mb:.2f} MB, sınırın altında."

        messagebox.showinfo("PDF Sıkıştırıcı", message)

    except subprocess.CalledProcessError as e:
        messagebox.showerror("Hata", f"Ghostscript hata verdi.\nKomut:\n{' '.join(gs_command)}\nHata kodu: {e.returncode}")
    except Exception as e:
        messagebox.showerror("Hata", f"Beklenmeyen hata oluştu:\n{e}")

if __name__ == "__main__":
    root = Tk()
    root.withdraw()

    input_path = filedialog.askopenfilename(title="Sıkıştırılacak PDF'yi seç", filetypes=[("PDF files", "*.pdf")])
    if not input_path:
        exit()

    base, ext = os.path.splitext(input_path)
    output_path = base + "_compressed" + ext

    compress_pdf(input_path, output_path)
