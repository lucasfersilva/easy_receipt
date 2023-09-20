import jinja2
import pdfkit
import datetime


def generate_pdf_invoice(context):
    template_loader = jinja2.FileSystemLoader('pdf_generation/')
    template_env = jinja2.Environment(loader=template_loader)

    template = template_env.get_template('invoice.html')

    # Get the items from the context
    items = context.get('items', {})
    print(items)
    # Convert items to a list of dictionaries for easy iteration in the template
    items_list = [{'item_name': item, 'item_value': value} for item, value in items.items()]

    # Add the items_list to the context
    context['items_list'] = items_list

    output_text = template.render(context)

    config = pdfkit.configuration(wkhtmltopdf="/usr/local/bin/wkhtmltopdf")
    pdfkit.from_string(output_text, 'invoice_generated.pdf', configuration=config, css='pdf_generation/invoice.css')
    return 200
