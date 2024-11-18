from fpdf import FPDF, Align


def main():
    # Ask for user name
    name = input("Name: ").strip().title()
    create_shirtificate(name)


def create_shirtificate(name):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("helvetica", "B", 32)
    pdf.cell(100, 30, "CS50 Shirtificate", align="C", center=True)
    pdf.ln(40)
    pdf.image("./shirtificate.png", x=Align.C, w=160)
    pdf.set_font("helvetica", "B", 16)
    pdf.set_text_color(r=255, g=255, b=255)
    pdf.set_y(90)
    pdf.multi_cell(90, 10, f"{name} took CS50", align="C", center=True)
    pdf.output("shirtificate.pdf")


if __name__ == "__main__":
    main()
