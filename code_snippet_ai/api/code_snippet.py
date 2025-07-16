import frappe
import json

@frappe.whitelist(allow_guest=True)
def update_snippet():
    try:
        data = frappe.local.form_dict
        if not data:
            data = json.loads(frappe.request.get_data())
        
        name = data.get("name")
        seo_title = data.get("seo_title")
        seo_description = data.get("seo_description")
        html_content = data.get("html_content")

        if not name:
            return "Missing document name"

        doc = frappe.get_doc("Code Snippet", name)
        doc.seo_title = seo_title
        doc.seo_description = seo_description
        doc.html_content = html_content
        doc.save()
        frappe.db.commit()
        return "Snippet updated successfully ✅"
    
    except Exception as e:
        frappe.log_error(frappe.get_traceback(), "Code Snippet Update Error")
        return {"error": str(e)}
